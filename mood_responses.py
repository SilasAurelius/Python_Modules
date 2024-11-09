def mood_response(mood):
        if mood == "happy":
            return ("I'm happy when reading a good book!")
        elif mood == "sad":
            return ("Head pats for you. Chocolate don't heal the hurt but it helps!")
        elif mood == "excited":
            return ("I'm excited too, let's wrestle a bear!")
        elif mood == "sleepy":
            return ("Time for a nap!")
        else:
            return ("I don't know that mood. Try (happy/sad/excited/sleepy)")