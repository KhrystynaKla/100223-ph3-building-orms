############## IMPORTS ##############

# the . stands for our __init__.py
from . import CONN, CURSOR


############## COURSE ##############

class Course:

    # --- MAGIC METHODS --- #

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def __repr__(self):
        return f"Course(id={self.id}, name={self.name})"

    # --- SQL CLASS METHODS --- #

    @classmethod
    def create_table(cls):
        sql = '''CREATE TABLE IF NOT EXISTS courses(
            id INTEGER PRIMARY KEY,
            name Text
        )'''
        CURSOR.execute(sql)
        #GIT ADD
        CONN.commit()
        #GIT COMMIT

        # creates the table if it doesn't exist

    @classmethod
    def get_all(cls):
        sql='''SELECT * fROM courses;
        '''
        read_all_tuples=CURSOR.execute(sql).fetchall()
        all_courses =[]
        for tup in read_all_tuples:
            all_courses.append(Course(name=tup[1], id=[0]))
        return all_courses
        # creates a new instance for each row in the db

    @classmethod
    def get_by_id(cls, id):
        sql ='''SELECT * FROM courses WHERE id=?'''

        found_course_tuple=CURSOR.execute(sql, id).fetchall()
        if found_course_tuple:
            return Course(name=found_course_tuple[1], id=found_course_tuple[0])

        # finds by id and if found instantiates a new instance


    # --- SQL INSTANCE METHODS --- #

    def create(self):
        sql ='''INSERT INTO courses (name)
        VALUE (?)
        '''
        CURSOR.execute(sql, [self.name])
        #GIT ADD
        CONN.commit()
        #GIT COMMIT
        # creates in the db and updates instance with the new id
        last_row_sql = 'SELECT * FROM courses ORDER BY DESC LIMIT 1'
        last_row_tuple = CURSOR.execute(last_row_sql).fetchone()
        self.id=last_row_tuple[0]


    def update(self):
        sql = '''UPDATE courses SET name=?
        WHERE id= ?
        '''
        CURSOR.execute(sql, [self.name, self.id])
        #GIT ADD
        CONN.commit()
        # updates the row based on current attributes 


    def save(self):
        if not self.id:
            self.create()
        else:
            self.update()
        # creates if it doesn't exist
        # updates if it does exist

    
    def destroy(self):
        sql = '''DELETE FROM courses Where id=?'''
        CURSOR.execute(sql, [self.id])
        #GIT ADD
        CONN.commit()
        self.id=None
        # deletes the instance from the db and removes the id

    # --- JOIN METHODS --- #

    def students(self):
        sql ='''
        SELECT * FROM students WHERE course_id = ?'''
        student_tuple=CURSOR.execute(sql, [self.id]).fetchall()
        return [Student(id=student_tuple[0], name=student_tuple[1], grade=student_tuple[2], course_id=student_tuple[3]) for student in student_tuple]
        # return a list of instances of each student

############## END COURSE ##############



############## STUDENT ##############

class Student:

    # --- MAGIC METHODS --- #

    def __init__(self, name, grade, course_id, id=None):
        self.name = name
        self.grade = grade
        self.id = id
        self.course_id = course_id

    def __repr__(self):
        return f'Student(id={self.id}, name={self.name}, course_id={self.course_id})'
    

    # --- CLASS SQL METHODS --- #

    # make a table if it doesn't exist
    @classmethod
    def create_table(cls):
        pass
        # create table with proper columns if not exists


    # --- SQL METHODS --- #

    def create(self):
        pass
        # add to the database

    def update(self):
        pass
        # update based on current instance attributes

    # remove from the database
    def destroy(self):
        pass
        # destroy row in the db based on id


    # --- SQL CLASS METHODS --- #

    @classmethod
    def get_by_id(cls, id):
        pass
        # find and return instance based on id
        
    # BONUS #
    @classmethod
    def get_by_name(cls, name):
        pass
        # find and return instance based on name
    
    @classmethod
    def get_all(cls):
        pass
        # return all instances from the database


    # --- JOIN METHODS --- #

    def course(self):
        pass
        # get the course by course_id


############## END STUDENT ##############