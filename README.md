# nzpc-2018
New zealand programming contest 2018

- Robert King (E.py 10pt, L.py 30pt, O.py 100pt)

- Ralph Verstegeen (K.py 30pt, P.py 100pt)

- Antony Phillips (G.py 10pt, M.py 100pt, N.py 100pt)

Having won the NZPC a few times previously, i took a hiatus for a few years, this year we made a last minute decision to enter. With Tom having a prior commitment, Antony joined the team.

If we hadn't have spent the initial contest time on the 10 and 30 point problems, we likely would have solved all of the 100 point problems. It's hard to know the tradeoff between making early use of the computer solving easy problems, or gathering debug information ASAP for the harder problems. Often the 100 point problems are fairly straight forward but one is very hard and not worth the trouble, but this year all 4 problems were "solvable" - this meant we really did have a lot of time pressure in the last hour of the contest, trying to finish all of them.

a better strategy for this contest that makes early use of the computer and also yields early debug information on the hard problems is - everyone focus first on the hard problems, see which of them require known algorithms,
and then have someone start typing in code for the known algorithm while others on the team prepare code to type in. That way - knowing more about the harder problems early on, allows you to plan the contest more. You will then know how much time you have for easier problems at the end and can use the score board as an indicator of which ones you should focus on.

I was very happy with my solution to problem L, in which you're given 100,000 buildings and their heights. You are told the angle of the Sun, and you need to put all the buildings in a line in such a way that the amount of buildings completly shadowed by other buildings is maximised. It feels like a DP or Greedy problem, but actually has a nice binary search & priority queue solution that iterates over all possible shadows generated by the tallest buildings which each protect their own pocket of buildings.

N & P timed out, requiring slight optimisations to fit the time-limit. Ralph & Antony say they needed another 10-30 minutes to finish these two.

problem O (snakes and ladders) had one edge case that i din't have time to think about, and I probably would have needed another 10-15 minutes for. This problem asked what the expeceted number of dice rolls is to get to the finish of snakes and ladders. The cells range from 1 to 100, and there can be ladders and snakes between. My approach was to create a system of equations, e.g. The expected value of cell 1 (X1) is equal to the average of the expected values of the next 6 cells plus one.
e.g. x1 = (x2+x3..+x7)/6 + 1
however if cell 3 has a ladder going to cell 20 for example, we would say x1 = (x2+x20...+x7)/6+1.
This can be put into a matrix, row reduced and solved (taking care the numbers get very very large, so we need to use modulo arithmatic). The quesiton guaranteed there is always a solution so I assumed my matrix was always invertable I.e. the equations always have a solution. However the problem is, for example, if you have 6 ladders in a row going upwards, you can there are certain cells that the player could never get to, Inside the cells that are unreachable, there can be infinit loops where it's impossible to progress (which is fine because you can never get stuck in there), but it meant my system was indeterminate. A very easy fix for this is to simply ignore any cells that aren't reachable, in hind site we could have easily solved this problem if our focus wasn't spread between the 2 other 100 point problems. 

with N,P and O solved, we would have had 480 points! instead we ended up with 180 points. It turned out in the end that 220 points would have been enough to win, so perhaps we were aiming too high.


EDIT:
I pushed a Fix for problem O.py, it now solves the 100 point problem.

UPDATE:
>rob: I pushed a fix for problem O, look how close I was


>ralph: Ah, too bad! I wish we'd just picked 3 of the 100 point problems and focused on them instead of trying to do all of them simultaneously. Then I could have discussed O more with you.
Honestly I had my doubts about your solution to O, but impressed you got it to work.
Thanks for the writeup.
A correction about problem P: I did manage to solve the time-out issues. By the end I was getting 'Incorrect Answer'. I thought about it a tiny bit more and realised another problem with my solution. Fixing it with brute force would have taken about 30 seconds, but would be way too slow. Fixing it more efficiently would have been more work - it isn't even immediately clear to me how to do that.
Looks like I underestimated both K and P. I had K right from the start, but it required much more code than I expected.
Where's the ANZAC programming contest domjudge?


>rob: http://domarchive.cosc.canterbury.ac.nz/public/ (select nzpc2018 in the top right)


