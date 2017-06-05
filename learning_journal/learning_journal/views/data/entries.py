"""Sample data for learning journal."""
"""
{
    'title': 'Day ',
    'publish_date': '05/15/2017',
    'body': '''.''',
    'author': 'Morgan'
}
"""

ENTRIES = [
    {
        'title': 'Day 1: BACK IN THE HABIT',
        'publish_date': '05/15/2017',
        'body': 'Happily back to the grind after 1 month off, 1 month as a TA, and another 2 weeks off. I really enjoyed the opportunity to be a TA, but by the end of it I was envious of the students - I wanted back into the classroom!Today we got a quick intro to environments, and - if I understand correctly - an environment walls off what packages and variables your code has access to. With that in mind, it sounds like our assignments are supposed to be contained in environments, which should give us finer control. We also talked about more Python-specific features, like using dir to see a list of an object\'s attributes. Every time another student asked a question in lecture, I\'m finding that it was a question I wouldn\'t have thought to ask and was glad to learn the answer.',
        'author': 'Morgan'
    },
    {
        'title': 'Day 2: Formal and natural languages',
        'publish_date': '05/16/2017',
        'body': 'Last night, I started the "How To Think Like a Computer Scientist" reading and found the concept of formal languages (as opposed to natural languages) really interesting. From the book: "Formal languages are languages that are designed by people for specific applications. For example, the notation that mathematicians use is a formal language that is particularly good at denoting relationships among numbers and symbols... Programming languages are formal languages that have been designed to express computations." Formal languages are supposed to be unambiguous and concise, and are likely to be dense.Today\'s lecture was chock full of information. We got deeper into parameters than I\'d been before - I hadn\'t heard of positional or keyword parameters, and I\'m excited to see how we apply them. \'Namespace\' is a term I\'d heard but my understanding of it was vague. Today helped; as I understand it, it\'s where Python thinks something - a value, a function - is defined. The second part of lecture was our introduction into TDD. It makes sense to build out tests before / concurrently with building functionality, but I\'m anticipating the art of writing good tests to be a complex one! We\'ll get our first chance in lab today.',
        'author': 'Morgan'
    },
    {
        'title': 'Day 3: Iteration, recursion, seeing in code',
        'publish_date': '05/17/2017',
        'body': '''Yesterday, we worked on functions that sum a series. My partner and I focused on iterator solutions first and turned our attention to recursion after our three iterative solutions passed tests. Castro shared his recursive solution for the fibonacci sequence, which was pretty different from my initial attempts. As I was watching the Clean Architecture video for today, Brandon Rhodes touched on what he considers a strength of functional programming: the simplicity and cleanliness allows him to visualize what the data looks like at every step. I need more exposure to recursion because I don't yet have that vision! But just five months ago, I was struggling to 'see' how a loop ran and we arrived at our iterative solution quickly - proof that it's very possible to learn that ability to visualize what a function/program is doing.Lecture got a lot deeper into environments and packages, but it made sense and the structure was similar to how we used Node.js in 301. Reading and writing into files is newer for me, so I anticipate needing to do some research in that area. The work we do in the command line makes me realize how little I've really used my computer until now! We talked a lot about collection data types and all the super cool, clean Python methods specific to each. Lab time today made me feel like I was back at Code Fellows for real. The 'how is half this work ever going to get done' feeling is back in full force! Anna and I spent a lot of time on our environment and package set up, which I think will pay off. I was able to clone the repo and install the dependencies without any problems, and we can easily run whatever we put in main from the terminal.''',
        'author': 'Morgan'
    },
    {
        'title': 'Day 4: Lists, dictionaries, tox',
        'publish_date': '05/18/2017',
        'body': '''Today's lecture focused more on lists and dictionaries, including anonymous/lambda functions. We also got more in-depth about shallow and deep copying, which can be used to sort lists and dictionaries.This was our second day in lab setting up our environments and packages, and building a package around our own module. Today we added tox, however, so that added a new level of complexity. We got to see the magic of tox in action when we ran a test on a function that converts our mailroom donor keys into a list - since we hard-coded the expected result, the test didn't pass because the outputted list in the Python2 environment was unpredictible. Tomorrow we're going to do our Day of Code assignment, solving CodeWars katas and writing tests for them. I'm excited to practice writing tests because I need it!''',
        'author': 'Morgan'
    },
    {
        'title': 'Day 5: I melted my brain',
        'publish_date': '05/19/2017',
        'body': '''I was super excited to work on katas today, but it ended up really frying my brain! I like working on them when I have time but I think my solutions got less Pythonic the more of them I wrote. Lots of loops and if/elses. Definitely want to spend more time on comprehensions. The easiest part of this assignment was getting my setup including tox to work. This weekend promises to be pretty crazy, as we're going to try wrapping up our assignments!''',
        'author': 'Morgan'
    },
    {
        'title': 'Day 6: Servers \'n sockets',
        'publish_date': '05/22/2017',
        'body': '''Need sleep in a major way. But in spite of that, today was really fun. Kurt, Ron and I got our socket project up and running, aside from the small (hopefully...?) matter of figuring out why a message that is a multiple of our buffer hangs. We also wrote our required tests before building the client or server, so that was a good feeling - making progress in ye olde TDD. I'm also super excited to work with data structures and was glad we kicked that off today.''',
        'author': 'Morgan'
    },
    {
        'title': 'Day 7: Kicking off data structures',
        'publish_date': '05/23/2017',
        'body': '''I've been excited about learning data structures since I started at Code Fellows, and really enjoyed our first foray into it with linked lists yesterday (and today) and stacks today. I didn't know exactly how we'd be learning data structures, but we'll be building them with Python primitives. Pretty cool! My DS partner and I both have strong opinions but our communication is good and I think we're hitting a rhythm. I'm going to need to re-read the materials on sockets and HTTP requests. I find it difficult to remember facts before I've built up some context. But working on the lab and seeing how information actually gets transmitted is very cool and motivating me to want to learn more.''',
        'author': 'Morgan'
    },
    {
        'title': 'Day 8: Tradeoffs',
        'publish_date': '05/24/2017',
        'body': '''I really enjoyed working on today's gist. It was fun to get a challenge that leveraged our work on linked lists. I started with psuedocode, but Python has such nice syntax, I didn't have to do much to execute it. I made the choice to go to the job fair/speed mentoring event, and it was a zoo. Really loud, really crowded. I talked to four new people and considered it a success. It was kind of my job fair recon, as I've never been before. Don't know why I didn't think to bring my resume! Going to the fair meant leaving school early, which made me feel behind on work. Chris and I had pseudo-coded all of our DLL tests before I left, and Kurt, Ron and I had hashed out a test and an approach to Step 2 of our server, but there's more work to be done on both assignments. Tradeoffs. I really don't know how to conduct a job search while doing this class!''',
        'author': 'Morgan'
    },
    {
        'title': 'Day 9: Try.',
        'publish_date': '05/25/2017',
        'body': '''This was one of those days where my partners and I worked solidly for six hours straight and yesterday's assignments still aren't done! I learned a more about try/except statements and raising errors as Kurt and I worked through Step 2 on our HTTP server, and they seem pretty powerful. There is nothing like needing to use something to deepen your understanding on something!''',
        'author': 'Morgan'
    },
    {
        'title': 'Day 10: Brain drain',
        'publish_date': '05/26/2017',
        'body': '''I really didn't absorb anything this morning - nothing was coming in or going out of my brain, especially during the whiteboard challenge. We had some great 401 Python grads come in to talk to us, and they kept encouraging us to ask questions. I realized the number of questions I ask has dropped off a lot and it's because I don't feel like I have a deep enough grasp on what we've been learning to get into the details. I thought the rest of the day would be shot, but my brain was working again by the time Kurt and I picked up our server assignment. We hit a couple of small snags but mostly we were making steady progress - and got some great help from Munir. I guessing I'm going to hit the point where my brain just won't work anymore many more times in this course, so it's nice to see that can turn around in a few hours. I just need to be patient. My weekend plans are to read ahead, read behind, and sleep 10 hours a night!''',
        'author': 'Morgan'
    },
    {
        'title': 'Day 11: Pyramid power',
        'publish_date': '05/30/2017',
        'body': '''We got our start in the Pyramid framework today. (I always find it a little challenging to follow on these setup-intensive days before the steps make sense.) One of the questions I've been wondering about is the difference between a library and a framework. The answer that made the most sense to me was that the code you (the developer) writes calls on the functionality in a library while a framework calls your code. Martin Fowler has a blog post called Inversion of Control (https://martinfowler.com/bliki/InversionOfControl.html) that was pretty interesting. Given that definition, I think Pyramid is the first true framework I've worked with.''',
        'author': 'Morgan'
    },
    {
        'title': 'Day 12: A heapish heap',
        'publish_date': '05/31/2017',
        'body': '''Long day yesterday. Feeling pretty good about using Pyramid; it's pretty similar to the kind of structure we working up to in our 301 projects, but, you know, Python. I think testing is the most challenging aspect, however, because I don't yet have a lot of insight into how it works. On the DS front, Chris and I started ours pretty late and our solution is the opposite of DRY - mostly because the binary heap seems pretty complex at this point. Whiteboarding helped us quickly get on the same page.''',
        'author': 'Morgan'
    },
    {
        'title': 'Day 13: Data structure revisions',
        'publish_date': '06/01/2017',
        'body': '''Well, my post is here and not yet on my learning journal. Chris and I finished our binheap, then I spent some time tackling subtle bugs in DLL that were screwing up our queue and dequeue. Then we both spent another hour or so on other DS stuff so we could resubmit all at once. It was an investment, but I feel good that we could leverage our current DS in future assignments if needed. I didn't have much time last night but I got most of my pyramid project configured to work with a database. It worked with one entry but I'm getting an error when I try using the for loop approach.''',
        'author': 'Morgan'
    },
    {
        'title': 'Day 14: Beginnings of project week',
        'publish_date': '06/02/2017',
        'body': '''My learning journal connects to a database now! Our group sorted out our project direction, and we've got some interesting research ahead of us. We're going to build a Chrome extension that analyzes written page content for tone. It's less ambitious than my vague initial idea, but very meaty and a good intro to building skills in an area I'm interested in. Pyramid stuff came together for me in the past couple of days. It's truly crazy what it enables us to do, and routing/dynamic serving makes more sense to me than it did in 301. After lecture and lab today, I think I've got a better handle on some of the new test functionality as well. I will say the errors produced by a failing test or deployment are a lot more difficult to trace because they involve so many levels of Pyramid. Fun fact - our data structure assignment for the day is a graph, and turns out the abstract drawing I made for my blog logo just happens to be one.''',
        'author': 'Morgan'
    }
]
