def create_course_dict(title, mentors, duration):
    return {"title": title, "mentors": mentors, "duration": duration}

def group_courses_by_duration(courses_list):
    durations_dict = {}
    for idx, course in enumerate(courses_list):
        key = course["duration"]
        if key in durations_dict:
            durations_dict[key].append(idx)
        else:
            durations_dict[key] = [idx]
    return dict(sorted(durations_dict.items()))

def format_sorted_courses(courses_list, durations_dict):
    result = []
    for duration, course_ids in durations_dict.items():
        for course_id in course_ids:
            course = courses_list[course_id]
            result.append(f'{course["title"]} - {duration} месяцев')
    return result

def main():
    courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
               "Frontend-разработчик с нуля"]

    mentors = [
        ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
         "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
         "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
         "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
         "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
         "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
         "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
         "Роман Гордиенко"],
        ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
         "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
    ]

    durations = [14, 20, 12, 20]

    courses_list = [create_course_dict(title, mentor, duration) for title, mentor, duration in zip(courses, mentors, durations)]
    durations_dict = group_courses_by_duration(courses_list)
    sorted_courses = format_sorted_courses(courses_list, durations_dict)

    return sorted_courses

if __name__ == "__main__":
    result = main()
    for course in result:
        print(course)
