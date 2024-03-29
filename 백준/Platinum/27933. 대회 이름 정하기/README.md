# [Platinum IV] 대회 이름 정하기 - 27933 

[문제 링크](https://www.acmicpc.net/problem/27933) 

### 성능 요약

메모리: 1679852 KB, 시간: 2244 ms

### 분류

구현, 자료 구조, 그리디 알고리즘, 세그먼트 트리, 누적 합

### 문제 설명

<p>연세대학교와 고려대학교가 매년 벌이는 정기전에는 공식 명칭을 정하는 규칙이 있다. 주최측 학교를 뒤로 가게 하여, 연세대가 주최할 때는 "고연전", 고려대가 주최할 때는 "연고전"이 공식 명칭이 된다. 그러나 이와 관계없이 연세대학교 학생은 "연고전", 고려대학교 학생은 "고연전"이라고 부르는 것이 일반적이다. 이 대회의 공식 명칭을 정할 때도 각 학교의 운영진은 각자 다니는 학교의 이름을 앞에 쓰고 싶어했다. 결국 다음과 같은 게임으로 대회 이름을 정하기로 하였고, 연세대측 출제자 Y와 고려대측 출제자 K가 맞붙었다. </p>

<p>$N$장의 카드가 일렬로 놓여 있다. 각 카드에는 '연' 또는 '고'와 $10^9$ 이하의 자연수가 써져 있다. 가장 왼쪽에 있는 카드부터 $1$번, $2$번, ... ,$N$번 카드라고 할 때, $l$번부터 $r$까지의 카드 중에서 몇 개의 카드를 순서대로 고른다. 이때, Y와 K는 각각 "연고"와 "고연"이 반복되도록 고른다. 즉 같은 글자가 써진 카드를 연속해서 고를 수 없으며, Y는 처음에 '연', 마지막에 '고'가 써진 카드를 고르고 K는 처음에 '고', 마지막에 '연'이 써진 카드를 고른다. 각자 고른 카드에 써진 수의 합이 각자의 점수가 되고, 그 점수가 큰 사람이 이긴다. 카드를 고를 수 없을 때의 점수 0점이다. </p>

<p>이 게임은 $T$번 진행되고, 각 게임에서 Y와 K가 같은 카드를 고르는 것이 허용된다. 게임에서 더 많이 이긴 학교의 이름을 앞에 쓰기로 하였으므로, Y와 K는 학교의 자존심을 걸고 최선의 전략으로 게임에 임한다. 이때, 각 게임에서 승자와 그의 점수를 출력하는 프로그램을 작성하시오. </p>

### 입력 

 <p>첫째 줄에 카드의 개수 $N$이 주어진다.</p>

<p>둘째 줄에 카드에 써진 글자가 하나의 문자열로 주어진다. '연'이 써진 카드는 <span style="color:#e74c3c;"><code>Y</code></span>로, '고'가 써진 카드는 <span style="color:#e74c3c;"><code>K</code></span>로 주어진다.</p>

<p>셋째 줄에 각 카드에 써진 자연수 $a_i$가 공백으로 구분되어 주어진다. $(1 \leq i \leq N)$</p>

<p>넷째 줄에 게임의 횟수 $T$가 주어진다.</p>

<p>다섯 번째 줄부터 $T$줄에 걸쳐 카드를 고를 수 있는 구간 $[l_i, r_i]$이 주어진다. $(1 \leq i \leq T)$</p>

### 출력 

 <p>각 줄마다 게임의 승자와 그의 점수를 공백으로 구분하여 출력한다. 무승부일 때는 <span style="color:#e74c3c;"><code>YK</code></span>와 그들의 점수를 공백으로 구분하여 출력한다. </p>

