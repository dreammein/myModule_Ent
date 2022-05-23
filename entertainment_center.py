import media
import fresh_tomatoes

The_Abyss = media.Movie("The Abyss",
                        "A civilian diving team is enlisted to search for a lost nuclear submarine and faces danger while encountering an alien aquatic species.",
                        "https://upload.wikimedia.org/wikipedia/en/a/ad/TheAbyss.jpg",
                        "https://www.youtube.com/watch?v=4zbpL3LeW7k")

#print(toy_story.storyline)

Sphere = media.Movie("Sphere", 
                             "A spaceship is discovered under three hundred years' worth of coral growth at the bottom of the ocean.",
                             "https://upload.wikimedia.org/wikipedia/en/a/ac/Spheremovieposter.jpg",
                             "https://www.youtube.com/watch?v=GJvKLetIV20")

Event_Horizon = media.Movie("Event Horizon",
                          "A rescue crew investigates a spaceship that disappeared into a black hole and has now returned...with someone or something new on-board.",
                          "https://upload.wikimedia.org/wikipedia/en/8/8c/Event_horizon_ver1.jpg",
                          "https://www.youtube.com/watch?v=2nlkEY-3CMI")



movies = [The_Abyss, Sphere, Event_Horizon]
fresh_tomatoes.open_movies_page(movies)
