import json
import os


# 2. 核心功能模块
# 功能一：添加学生信息
# 输入学生基本信息
# 自动计算总分和平均分
# 使用异常处理确保输入合法性

class StudentScoreAnalyzer:
    def __init__(self, student_data="student_data.json"):
        self.data = student_data      # 数据文件路径
        self.students = []        # 存储所有学生信息的列表
        self.load_data()       #   初始化时加载数据

    def load_data(self):
        '''从数据文件中加载学生信息'''
        try:
            if os.path.exists(self.data):
                with open(self.data, "r", encoding="utf-8") as f:
                    self.students = json.loads(f.read())  # 将json数据转换为Python对象
                    print(f"成功加载{len(self.students)}条学生记录")
            else:
                print("数据文件不存在，将创建文件")
        except Exception as e:   # 捕获所有异常
            print(f"加载数据文件时出错：{e}")  # 打印错误信息
            self.students = []

    def calculate_score(self, scores):
            '''计算学生成绩的平均分和总分 '''
            total_score = sum(scores.values())  # 使用.values()获取字典中的值
            average_score = total_score / len(scores) if scores else 0
            return total_score, average_score

    def add_student(self):
        '''  增加学生信息   '''
        try:
             print("\n----- 请输入学生信息-----")
             student_id = input("请输入学号: ").strip()

             #  检查该学号是否存在
             if any(s['id'] == student_id for s in self.students):
                 print("该学号已存在")
                 return
             name = input('请输入姓名:').strip()
             if not name:
                 print("姓名不能为空")
                 return
              # 输入各科成绩
             subjects = ['语文', '数学', '英语']
             scores = {}

             for subject in subjects:
                 while True:
                     try:
                         score = float(input(f'请输入成绩{subject}(0-100):'))
                         if  0 <= score <= 100:
                             print('输入成绩有效')
                             scores[subject] = score
                             break
                         else:
                             print("输入成绩无效，请重新输入")
                     except ValueError:
                         print("请输入有效数字")

             # 计算平均分和总分
             total, avg = self.calculate_score(scores)
             # 创建学生记录
             student = {'id': student_id,
                       'name': name,
                       'scores': scores,
                       'total': total,
                       'avg': avg
             }

             # 添加到学生列表
             self.students.append(student)

             # 保存数据
             self.save_data()

             # 打印成功信息
             print(f"学生{name}信息添加成功！")
             print(f"总分:{total:.1f},平均分:{avg:.1f}")

        except Exception as e:
            print(f"添加学生信息时出错:{e}")

    def save_data(self):
        '''保存数据到文件'''
        try:
            with open(self.data, 'w', encoding='utf-8') as f:
                json.dump(self.students, f, ensure_ascii=False, indent=2)
            print("数据已成功保存")
        except Exception as e:
            print(f"保存数据时出错:{e}")

# 测试代码
if __name__ == '__main__':
    analyzer = StudentScoreAnalyzer()
    analyzer.add_student()
































