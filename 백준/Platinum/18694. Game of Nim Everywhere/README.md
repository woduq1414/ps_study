# [Platinum I] Game of Nim Everywhere - 18694 

[문제 링크](https://www.acmicpc.net/problem/18694) 

### 성능 요약

메모리: 119896 KB, 시간: 704 ms

### 분류

다이나믹 프로그래밍(dp), 게임 이론(game_theory), 수학(math), 누적 합(prefix_sum), 스프라그–그런디 정리(sprague_grundy)

### 문제 설명

<p>Yes, this game comes again and again. Nim is a mathematical game of strategy in which two players take turns removing objects from distinct heaps. On each turn, a player must remove at least one object, and may remove any number of objects provided they all come from the same heap. The winner of the game is the player who removes the last object.</p>

<p>In this problem we will play with only 3 heaps, and the initial state also will be special, it will always be in the following format (N, 2 × N, 3 × N) where N is a positive integer. For example if N is 3, the 3 heaps will initially start with 3, 6 and 9 objects.</p>

<p>A winning state is a state of the heaps where there’s always a strategy for the player who is about to play, to win the game regardless what the other player does.</p>

<p>In this problem you are given two integers L and R, and your task is to find how many different values for N (L ≤ N ≤ R) such that if we use N to get the initial state as described above, it will be a winning state for the first player.</p>

### 입력 

 <p>Your program will be tested on one or more test cases. The first line of the input will be a single integer T (1 ≤ T ≤ 10<sup>5</sup>) representing the number of test cases. Followed by T test cases.</p>

<p>Each test case will be just one line containing 2 integers separated by a space, L and R (1 ≤ L ≤ R ≤ 2<sup>61</sup>), which are the range as described above.</p>

### 출력 

 <p>For each test case, print a single line with the number of different values of N which satisfy the condition described above.</p>

