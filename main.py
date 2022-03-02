sf = ""
Things_to_pack = {
    "General": ["Pencil Pouch", "Diary", "Rough Notebook", "Sanitizer"],
    "English": ["NEG", "English Notebook", "Stories occasionally"],
    "Science": ["Science Notebook", "Science Resource Book"],
    "Math": ["Math Notebook", "Math Homework book", "Math Textbook"],
    "Computers": ["Computer Science Notebook"],
    "Kannada": ["Kannada Textbook", "Kannada Notebook"],
    "Hindi": ["Hindi Notebook", "Hindi Vyaakaran Book", "Hindi Sunehari Dhoop book"],
    "History/Civics": ["History/Civics Notebook", "History/Civics textbook"],
    "Geography": ["Geography Notebook", "Geography textbook"]
}

tuesday = ["General", "Science", "English", "Kannada", "Math"]
thursday = ["General", "Math", "Hindi", "Computers", "History/Civics"]

a = input("What day is it today?")
if a == "tue":
    for i in tuesday:
        for f in Things_to_pack[i]:
            sf+=f
            sf += ", "
    print(sf)
elif a == "thu":
    for i in thursday:
        for f in Things_to_pack[i]:
            sf+=f
            sf += ", "
    print(sf)
