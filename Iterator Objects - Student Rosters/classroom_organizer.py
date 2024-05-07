from roster import student_roster
import itertools

class ClassroomOrganizer:
    """
    ######################################################################################################################################
    # This is a class designed to manage and organize student data in a classroom setting. It provides functionalities such as adding    #
    # and removing students, tracking student attendance, managing student grades, and generating reports. The class aims to streamline  #
    # the process of managing large amounts of student data, making it easier for educators to focus on teaching and student interaction # 
    # rather than administrative tasks.                                                                                                  #
    ######################################################################################################################################

    Attributes
    ----------
    sorted_names : list
        a list of student names sorted alphabetically
    index : int
        the current index for the iterator

    Methods
    -------
    _sort_alphabetically(students)
        Returns the list of student names sorted alphabetically.
    get_students_with_subject(subject)
        Returns the list of students who have the given subject as their favorite.
    __iter__()
        Returns the iterator object (self).
    __next__()
        Returns the next student name in the sorted list.
    get_table_arrangements()
        Returns all possible pairs of students.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the ClassroomOrganizer object.

        Parameters
        ----------
        None
        """
        self.sorted_names = self._sort_alphabetically(student_roster)
        self.index = 0

    def _sort_alphabetically(self,students):
        """
        Sorts the student names alphabetically.

        Parameters
        ----------
        students : list
            The list of students.

        Returns
        -------
        list
            The list of student names sorted alphabetically.
        """
        names = []
        for student_info in students:
            name = student_info['name']
            names.append(name)
        return sorted(names)

    def get_students_with_subject(self, subject):
        """
        Gets the students who have the given subject as their favorite.

        Parameters
        ----------
        subject : str
            The subject to match.

        Returns
        -------
        list
            The list of students who have the given subject as their favorite.
        """
        selected_students = []
        for student in student_roster:
            if student['favorite_subject'] == subject:
                selected_students.append((student['name'], subject))
        return selected_students

    def __iter__(self):
        """
        Returns the iterator object (self).

        Parameters
        ----------
        None

        Returns
        -------
        ClassroomOrganizer
            The iterator object.
        """
        return self

    def __next__(self):
        """
        Returns the next student name in the sorted list.

        Parameters
        ----------
        None

        Returns
        -------
        str
            The next student name in the sorted list.

        Raises
        ------
        StopIteration
            If there are no more student names in the sorted list.
        """
        if self.index >= len(self.sorted_names):
            raise StopIteration 
        result = self.sorted_names[self.index]
        self.index += 1
        return result
    
    def get_table_arrangements(self):
        """
        Gets all possible pairs of students.
        
        Parameters
        ----------
        None

        Returns
        -------
        list
            The list of all possible pairs of students.
        """
        return list(itertools.combinations(self.sorted_names, 2))
    
# Example using the custom iterators
if __name__ == '__main__':
    # Create an instance of ClassroomOrganizer
    classroom = ClassroomOrganizer()

    # Get students who love Math
    math_lovers = classroom.get_students_with_subject("Math")
    print("Students who love Math:", math_lovers)

    # Iterate over the sorted names
    print("Student names in alphabetical order:")
    for student in classroom:
        print(student)

    # Get all possible pairs of students
    pairs = classroom.get_table_arrangements()
    print("All possible pairs of students:", pairs)