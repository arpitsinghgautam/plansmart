def convert_to_dict(course_input):
    courses = course_input.split('\n\n')

    course_dict = {}

    for course in courses:
        lines = course.strip().split('\n')
        course_name = lines[0].strip()
        topic = lines[1].strip()
        course_content = [line.strip() for line in lines[2:]]

        course_entry = {
            course_name: {
                'topic': topic,
                'course_content': course_content
            }
        }

        course_dict.update(course_entry)

    return course_dict


input_string = '''
MA2101: ENGINEERING MATHEMATICS III
topic: Boolean Algebra
Partial ordering relations, Poset, Lattices, Basic Properties of Lattices. Distributive and complemented lattices, Boolean lattices, and Boolean Algebra. Propositional and Predicate 

Calculus
topic: Calculus
Well-formed formula, connectives, quantifications, Inference theory of propositional and predicate calculus.

Elementary configuration
topic: Elementary configuration
Permutations and Combinations, Generating function, Principle of inclusion and exclusion Partitions, compositions.
'''

course_dict = convert_to_dict(input_string)
print(course_dict)

for course_name, course_info in course_dict.items():
        print(course_name)
        print("Topic:", course_info['topic'])
        print("Course Content:")
        for content in course_info['course_content']:
            print("- " + content)
