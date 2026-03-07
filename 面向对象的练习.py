import json
import os

class student:
    # 初始化学生信息
    def __init__(self, id, name, scores):
        self.id = id
        self.name = name
        self.scores = scores

    #   计算总分
    def calculate_total(self):
        total = sum(self.scores.values())
        return total

    # 计算平均分
    def calculate_avg(self):
        avg = self.calculate_total() / len(self.scores)
        return avg
    
    # 显示学生信息
    def display_info(self):
        print(f'学号:{self.id}')
        print(f'姓名:{self.name}')
        print(f'分数:{self.scores}')
        print(f'总分:{self.calculate_total()}')
        print(f'平均分:{self.calculate_avg():.2f}')

    def get_grade(self):
        '''根据平均分返回等级'''
        if self.calculate_avg() >= 90:
            return '优秀'
        elif self.calculate_avg() >= 80:
            return '良好'
        elif self.calculate_avg() >= 60:
            return '及格'
        else:
            return '不及格'

    def __str__(self):
        '''返回学生信息的字符串表示'''
        return f'学号:{self.id}, 姓名：{self.name}, 总分:{self.calculate_total()}, 平均分:{self.calculate_avg():.2f}, 成绩等级:{self.get_grade()}'


class StudentManager:
    def __init__(self, students_file):
        self.students_file = students_file
        self.students = []
        self.load_data()

    def load_data(self):
        '''从文件中加载学生信息'''
        try:
            if os.path.exists(self.students_file):
                with open(self.students_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    print(f'成功加载{len(data)}条学生信息')
                    for item in data:
                        s = student(item['id'], item['name'], item['scores'])
                        self.students.append(s)
            else:
                print('数据文件不存在，将创建文件')
        except Exception as e:
            print(f'加载数据文件时出错：{e}')
            self.students = []

    def save_data(self):
        '''保存学生数据到文件'''
        try:
            data = []
            for s in self.students:
                data.append({
                    'id': s.id,
                    'name': s.name,
                    'scores': s.scores
                })
            with open(self.students_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print('数据已保存')
        except Exception as e:
            print(f'保存数据时出错：{e}')

    def add_student(self):
        '''添加学生'''
        try:
            print("\n----- 添加学生 -----")
            student_id = input("请输入学号:").strip()
            
            # 判断学号是否已经存在
            if any(s.id == student_id for s in self.students):
                print('该学号已存在')
                return
                
            name = input("请输入姓名：").strip()
            if not name:
                print('请输入有效的姓名')
                return
                
            subjects = ['语文', '数学', '英语']
            scores = {}
            for subject in subjects:
                while True:
                    try:
                        score = float(input(f'请输入{subject}成绩（0-100）：'))
                        if 0 <= score <= 100:
                            scores[subject] = score
                            break
                        else:
                            print('请输入有效成绩')
                    except ValueError:
                        print('请输入有效的数字')
                        
            new_student = student(student_id, name, scores)
            self.students.append(new_student)
            print(f'添加学生成功：{new_student}')
            new_student.display_info()
            self.save_data()
        except Exception as e:
            print(f'添加学生时出错：{e}')

    def show_all_students(self):
        '''显示所有学生信息'''
        if not self.students:
            print("暂无学生信息")
            return
        
        print("\n" + "="*50)
        print("所有学生信息：")
        print("="*50)
        for s in self.students:
            s.display_info()
            print("-" * 50)

    def search_student(self):
        '''根据学号查找学生'''
        student_id = input("请输入要查找的学号：").strip()
        for s in self.students:
            if s.id == student_id:
                print("\n✅ 找到学生：")
                s.display_info()
                return
        print("❌ 未找到该学号的学生")

    def delete_student(self):
        '''删除学生'''
        student_id = input("请输入要删除的学号：").strip()
        for i, s in enumerate(self.students):
            if s.id == student_id:
                del self.students[i]
                print("✅ 删除成功")
                self.save_data()
                return
        print("❌ 未找到该学号的学生")

    def menu(self):
        '''显示菜单'''
        while True:
            print("\n" + "="*50)
            print("学生管理系统")
            print("="*50)
            print("1. 添加学生")
            print("2. 显示所有学生")
            print("3. 查找学生")
            print("4. 删除学生")
            print("0. 退出系统")
            
            choice = input("请选择操作（0-4）：").strip()
            
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.show_all_students()
            elif choice == '3':
                self.search_student()
            elif choice == '4':
                self.delete_student()
            elif choice == '0':
                print("感谢使用，再见！")
                break
            else:
                print("输入无效，请重新选择")


# 程序入口
if __name__ == "__main__":
    manager = StudentManager("student_data.json")
    manager.menu()












