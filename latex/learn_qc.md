---
bibliography:
- q.bib
title: Quantum computing notes
---

# Concepts and notions

## Fundamentals {#fundamentals .unnumbered}

::: concept
**Concept 1** (Quantum function evaluation). *Consider some kind of
quantum cirquit and a function. I define the *(basic)* quantum function
evaluation by the circuit given below:*
:::

<figure id="fig:function_evaluation">
<p>@C=1em @R=1em<span> &amp; &amp; &amp;<br />
&amp; &amp; &amp;<br />
&amp; &amp; &amp;<br />
</span> <span id="fig:function_evaluation"
label="fig:function_evaluation"></span></p>
<figcaption>Quantum function evaluation.</figcaption>
</figure>

What the binary algorithm does is to *evaluate the function of the
target cubit*.

## Main Circuits {#main-circuits .unnumbered}

Let's discuss main representation of the circuits.

::: tabular
\|c\|c\|c\|c\|c\| Operator & & Matrix & & Qiskit\
& & $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$ &
$\forall \ket{\psi} \in V , \mathbbm{1}\ket{\psi}=\ket{\psi}$ &\
& & $\frac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$ &
&\
& $\sigma_z \equiv \ket{0}\bra{1} - \ket{1}\bra{1}$ &
$\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$ & &\
& & $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ & &\
& $P(\phi)\equiv \ket{0}\bra{0} + e^{i\phi}\ket{1}\ket{1}$ &
$\begin{bmatrix} 1&0\\0&e^{i\phi} \end{bmatrix}$ & &\
& & $\begin{bmatrix}
    1&0&0&0\\
    0&1&0&0\\
    0&0&0&1\\
    0&0&1&0
  \end{bmatrix}$ & &\
:::

# Deutsch-Jozsa algorithm

The Deutsch-Jozsa algorithm was the first algorithm to be proposed. The
goal of the Deutsch's quantum algorithm is to determine a concrete
property of a funciton. In this case, we use the quantum algorithm, to
determine the properties of the function. In the case of the

::: definition
**Definition 1** (Constant and balanced). The function used here is a
function from $\{0,1\}^N \mapsto \{0,1\}$. The outputs of it can be
either constant or balanced. We say that the function is *constant* if
for [any]{.underline} input the output is constant, that is, whether all
ones or all zeroes. We say that the function is *balanced* if it outputs
ones half of the times and zeroes half of the other times (that is, out
of all possible inputs, it will output a `1` in the half of the input
cases and `0` in the other).
:::

We will consider the case where $n$ (the number of inputs) is equal to
one. That is, the function $f(x)$ has one input bit. $f(x)$, with
$x \in \{0,1\}$. Let's see an example of a constant or balanced
functions. Let $f_1(x)$. The function happens to output the following:
$f_1(0)=0$ and $f_1(1)=0$. We see that the function has zeroes for any
inputs. Therefore, we can conclude that the function $f_1$ is constant.
Consider now the function $f_2$, satisfying the following: $f_2(0)=1$
and $f_2(1)=0$. As there are 2 kinds of inputs (`0` and `1`), there are
only 2 possible outputs (2 different outputs for 2 different inputs). We
see that for the function $f_2$, half of the outputs (i.e. only one out
of two) is `0` and half of the inputs is `1`. Therefore, the function
$f_2$ is balanced.

The example was a simple case, where the input was simply either `0` or
`1`. The definition of this constant/balanced can be extended to a more
complex case of an input $\{0,1\}^n$, which is the Deutsch-Jozsa
algorithm.

## Deutsch's algorithm {#deutschs-algorithm .unnumbered}

Let's first consider the Deutsch's algorithm
[@noauthor_deutschjozsa_2022], that is, with one input bit. The circuit
is *postulated* to be. In order for it to have a working mechanism, we
need to prepare the initial states.

<figure id="cirq:deutsch_start">
<figure>
<p>@C=1em @R=1em<span> &amp; &amp; &amp; &amp;<br />
&amp; &amp; &amp; &amp;<br />
</span></p>
<figcaption>Deutsch’s circuit</figcaption>
</figure>
<figure>
<p>@C=1em @R=1em<span> &amp; &amp; &amp; &amp; &amp;&amp; &amp;<br />
&amp; &amp; &amp;&amp; &amp; &amp;&amp;<br />
</span></p>
<figcaption>Initialized states</figcaption>
</figure>
<figcaption>Deutsch’s circuit</figcaption>
</figure>

Having the circuit with prepared initial states
([\[cirq:deutsch_start\]](#cirq:deutsch_start){reference-type="autoref"
reference="cirq:deutsch_start"}) we're now in the situation in carefully
initialize the cirquit. We've identified 2 states of the cirquit: `A`
and `B`, which we'll quickly discuss [^1].

The first register begins with the state $\ket{0}$. As usual, applying
the Hadamard gate $\mathcal{H}$ on the first register gives us
$\ket{0} \xrightarrow{\mathcal{H}}{} \frac{1}{\sqrt{2}} ( \ket{0} + \ket{1} )$
as usual. Thus, the total state at the point **A** is given by the
tensor product of both registers, which is
$(\ket{0}+\ket{1})\otimes (\ket{0} - \ket{1})$.

After the point we apply the *function evaluation* (TODO). Let's
consider the rigourous operation:

$  \text{\textmd{state at \textbf{A}}:\ \ \ } \frac{1}{\sqrt{2}}(\ket{0} + \ket{1}) \otimes \frac{1}{\sqrt{2}}(\ket{0}-\ket{1}) \\ $

Now, the state after the function $f$, using the concept of the
evaluation function, we have the *general* expression of
$\ket{x} \otimes \ket{y} \mapsto \ket{x}\otimes \ket{y \oplus f(x)}$,
which, in the case of our circuit
[\[cirq:deutsch_start\]](#cirq:deutsch_start){reference-type="autoref"
reference="cirq:deutsch_start"}, gives the state
$\ket{y}=\frac{1}{\sqrt{2}}(\ket{0} - \ket{1})$ for $\ket{y}$. Thus, for
the circuit between **A** and **B**: $$\begin{aligned}
\ket{\psi_B}=\bigg| \frac{1}{\sqrt{2}} (\ket{0}+\ket{1}) \bigg \rangle  &\otimes \bigg| f(x) \oplus \frac{1}{\sqrt{2}} (\ket{0}-\ket{1}) \bigg \rangle \\
\frac{1}{2} \bigg| \ket{0}+\ket{1} \bigg \rangle  &\otimes \bigg| \ket{f(x)}-\ket{1\oplus f(x)} \bigg \rangle \\
\frac{1}{2} \bigg| \ket{0}+\ket{1} \bigg \rangle  &\otimes \bigg| (-1)^{f(x)} (\ket{0}-\ket{1}) \bigg \rangle
\label{eq:deutsch_f(x)}
\end{aligned}$$

Now we can expand this further, still for the state at the point B. When
we explicit the expression in order to see the input of the function
$f(x)$. What I mean is that in
[\[eq:deutsch_f(x)\]](#eq:deutsch_f(x)){reference-type="autoref"
reference="eq:deutsch_f(x)"}, the function $f(x)$ it accepts the
superposition, as the input is an entangled state.

$$\begin{aligned}
\ket{\psi_B} = \frac{1}{2} \bigg| \ket{0}+\ket{1} \bigg \rangle  \otimes \bigg| (-1)^{f(x)} (\ket{0}-\ket{1}) \bigg \rangle \\
\ket{\psi_B} = \frac{1}{2} \bigg| (-1)^{f(x)}(\ket{0}+\ket{1})\bigg \rangle \otimes \bigg| \ket{0}-\ket{1} \bigg \rangle \\
\ket{\psi_B} = \frac{1}{2} \bigg| (-1)^{f(0)}\ket{0} + (-1)^{f(1)}\ket{1} \big \rangle \otimes \bigg| \ket{0} - \ket{1} \bigg \rangle
\end{aligned}$$ now we apply an unusual trick is not that simple to see
but simple to check that it is true. What we will use here is the fact
that $$\begin{aligned}
  f(0)\oplus f(0) \oplus f(1) = f(1)
\end{aligned}$$ This can be seen as the term $f(0) \oplus f(0)$ will
always give zero and thus, $0 \oplus f(x)=f(x)$ and therefore,

$$\begin{aligned}
\ket{\psi_B} = \frac{1}{2} \bigg| (-1)^{f(0)}\ket{0} + (-1)^{f(0)\oplus f(0)\oplus f(1)}\ket{1} \bigg \rangle \otimes \bigg| \ket{0} - \ket{1} \bigg \rangle \\
\ket{\psi_B} = \frac{1}{2} (-1)^{f(0)}\bigg| \ket{0} + (-1)^{f(0)\oplus f(1)}\ket{1} \bigg \rangle \otimes \bigg| \ket{0} - \ket{1} \bigg \rangle
\label{eq:deutsch_global_phase}
\end{aligned}$$ We know however that the global phase do not matter at
all. In addition to that, we see that in
[\[cirq:deutsch_start\]](#cirq:deutsch_start){reference-type="autoref"
reference="cirq:deutsch_start"}, after the point **B**, we're not
interested in the state $\ket{y}$ anymore. Thus, we can simply ignore
both the global phase $(-1)^{f(0)}$ and the second state
$\ket{0}-\ket{1}$. Thus, we're left with the state
$\ket{\tilde{\psi_B}}\equiv \ket{0} + (-1)^{f(0)\oplus f(1)}\ket{1}$, on
which we apply the $\mathcal{H}$ operation. This gives us
$$\begin{aligned}
  \mathcal{H} \ket{\tilde{\psi_B}} \stackrel{*}{=} \ket{+} + (-1)^{f(0)\oplus f(1)}\ket{-}=\\
  (1+(-1)^{f(0)\oplus f(1)}) \ket{0} + (1-(-1)^{f(0)\oplus f(1)})\ket{1}
  \label{eq:deutsch_f_last}
\end{aligned}$$ Therefore, we obtain that if ${f(0)\oplus f(1)}=0$, the
measurement of the top qubit will be $\ket{0}$ and if the result
${f(0)\oplus f(1)}=1$, the result of the measurement will be given by
$\ket{1}$. Therefore, we will measure the $\ket{0}$ bit if the value of
the function is constant (either all ones or all zeroes), and similarly,
we will measure the value $\ket{1}$ bit if the value of the function is
balanced. In both cases, we're making the measurements with probability
1.

## Deutsch-Jozsa's algorithm {#deutsch-jozsas-algorithm .unnumbered}

The Deutsch-Josza's algorithm is similar to the Deutsch's one. That is,
it is a generalization from one bit input ( i.e. $\{0,1\}$) to the n bit
input (i.e. $\{0,1\}^n$, which is nothing but a bit string).

::: tblr
l \|\| r \@C=1em \@R=1em && & & & & & &\
&& & & & & & &\
&& & & & & & &\
&& & & & & & &\
&& & & & & & &\
&& & & & & & &\
&& & & & & & &\
& \@C=1em \@R=1.5em & & & & & & &\
& & & & & & &\

\
:::

The working principle of this generalized version is harder to show and
harder to understand. The proof is nicely shown in
[@noauthor_deutschjozsa_2022]. Lets start from the initial state, as
shown in
[\[table:cirq:deutsch_josza\]](#table:cirq:deutsch_josza){reference-type="autoref"
reference="table:cirq:deutsch_josza"}. As usual, we sometimes omit the
global normalization constant (we thus write $\stackrel{*}{=}$).
$$\begin{aligned}
  \ket{\psi_A}\stackrel{*}{=}& (\ket{0}\otimes \ket{0} ... \otimes \ket{0})\otimes (\ket{0}-\ket{1}) = \ket{0}^{\otimes n}\otimes (\ket{0}-\ket{1})\\
  \ket{\psi_B}\stackrel{*}{=}& \bigotimes_{i=0}^{n} \mathcal{H} \ket{\psi_A} \stackrel{*}{=} \mathcal{H}^{\otimes n}\ket{0}^{\otimes n}\otimes (\ket{0}-\ket{1})\\
  \stackrel{*}{=}& \ket{+}^{\otimes n} (\ket{0}+\ket{1}) = \sum_{x}^{2^n} \ket{x}\otimes (\ket{0}-\ket{1})
\end{aligned}$$ Note that $\ket{x}$ here represents a binary string.
Indeed, a $\mathcal{H}$ acting on $\ket{0}$ can represent the sum of
numbers from 0 to 1.
($\mathcal{H}\ket{x}\stackrel{*}{=}\ket{0}+\ket{1}$). When acting on a
2D space,
$(\mathcal{H}\otimes \mathcal{H})(\ket{0}\otimes \ket{0})\stackrel{*}{=}\ket{0}\otimes \ket{0} + \ket{0}\otimes \ket{1} + \ket{1}\otimes \ket{0} + \ket{1}\otimes \ket{1}$.
We therefore see that the Hadamard gate on the n-dimensional space will
give the sum of binary strings ranging from $0$ to $2^n-1$. This is what
is meant in the sum over $\ket{x}$. Then, the quantum function
evaluation, as defined, will create the transformation
$\ket{x}\otimes \ket{y} \xrightarrow{f}{} \ket{x}\otimes \ket{f(x)\oplus y}$,
by definition. Therefore, at the point $C$ (as on
[\[table:cirq:deutsch_josza\]](#table:cirq:deutsch_josza){reference-type="autoref"
reference="table:cirq:deutsch_josza"}), the transformation give:
$$\begin{aligned}
  \ket{\psi_C} &\xleftarrow{f}{} \ket{\psi_B} \\
  \ket{\psi_C} &\stackrel{*}{=} \sum_x^{2^n-1} \ket{x}(\ket{f\oplus 0}-\ket{f \oplus 1}) \\
               &= \sum_x^{2^n-1} \ket{x}(-1)^{f(x)} (\ket{0}-\ket{1})
\label{eq:deutsch_josza_C}
\end{aligned}$$ now, we can \"ignore\" the $\ket{0}-\ket{1}$ part, as
after the C point, we're only applying the $\mathcal{H}$ to the top part
(i.e. without the $\ket{0}-\ket{1}$). We also remember our important
result $$\begin{aligned}
  \matchcal{H} \ket{x} \equiv \bigotimes^n \mathcal{H} \ket{x} = \frac{1}{\sqrt{2^n}} \sum_{y=0}^{2^n-1} (-1)^{x\cdot y}\ket{y}
  \label{eq:hadamard_on_generic}
\end{aligned}$$ with the $x \cdot y$ being the vector product between
two bitstrings. The bitstrings can be represented as vectors, e.g.
$\ket{x}\equiv (0,1,1,0,0,...,1)$ and $\ket{y}\equiv (1,0,1,1,...,1)$.
Their dot product is defined as
$x\cdot y = (x_1 \cdot y_1) \oplus (x_2 \cdot y_2) \oplus (x_3 \cdot x_3) \oplus ... \oplus (x_n \cdot x_n)$.
Therefore, by applying the $\mathcal{H}$ on $\ket{\psi_C}$ given in
[\[eq:deutsch_josza_C\]](#eq:deutsch_josza_C){reference-type="autoref"
reference="eq:deutsch_josza_C"}, $$\begin{aligned}
  \bigotimes ^n \mathcal{H} \ket{\psi_C} &\stackrel{*}{=} \mathcal{H} \sum_x^{2^n-1} \ket{x}(-1)^{f(x)} \\
                                         &= \sum_x^{2^n-1} \mathcal{H}\ket{x}(-1)^{f(x)} \stackrel{\text{\autoref{eq:hadamard_on_generic}}}{=} \\
                                         &= \sum_x^{2^n-1} \sum_y^{2^n-1} \ket{y} (-1)^{f(x)}(-1)^{x\cdot y} \\
                                         &= \sum_y^{2^n-1} \Biggl [\; \; \sum_x^{2^n-1} (-1)^{f(x)}(-1)^{x\cdot y} \; \Biggl ] \ket{y}
\end{aligned}$$ which is the (almost) final result. This is what we get,
when we'll obtain after applying the $\mathcal{H}$ on the $\ket{\psi_C}$
state. Now, we can see that the $\ket{y}$ are linear combinations of
probability amplitudes $\sum_x^{2^n-1} (-1)^{f(x)}(-1)^{x\cdot y}$ for
each $\ket{y}$. We now have a look at the state $\ket{y}=0$, that is,
$\ket{y}=\ket{0,0,...,0}$. The probability of measuring it is given by
$\bigg| \sum_x^{2^n-1} (-1)^{f(x)} \bigg|^2$. The probability of
measuring this $\ket{0}=\ket{y}$ will be given by 1, if the function is
constant. Indeed, if $f(x)$ is constant (either always ones or always
zeroes), then we will make the sum of $-1$ if it is always one, and sum
of all $(-1)^0$ if always zeroes. If it is balanced, then we will make
the sum of $(-1)$ and $1$, which will give us 0 probability if the
function is balanced.

Thus, we've showed that the algorithm can determine, whether the
function is constant or balanced.

### Example {#example .unnumbered}

The \"problem\" with this algorithm is that we need to have a very
specific oracle. To be more precise, one may thing that we constructed
the concept of solving the algorithm, based on the given oracle that
\"comes from nowhere\". This is not false. For an arbitrary function, we
can't construct the algorithm right away.

In order to ckeck the algorithm, one can simply check the algorithm for
specific inputs, and whether it represents the specific outputs.

## Bernstein-Vazirani algorithm {#bernstein-vazirani-algorithm .unnumbered}

The next algorithm is the Bernstein-Vazirani algorithm, which also gives
a speedup over the classical solution. The technique to solve such
problem is similar to the Deutsch-Jozsa's one, that is, uses a phase
kick-back trick.

The problem that the Bernstein-Vazirani algorithm aims to solve is the
following: we have a function $f(x)$ which has the form
$f(x): \{0,1\}^n \rightarrow \{0,1\}$ and
$f(x): x \mapsto s \cdot x=s_1 x_1 \oplus s_2 x_2 \oplus ... \oplus s_n x_n$,
for some \"secret\" string $s$, for which we denote the corresponding
function $f_s(x)$. The goal of the Bernstein-Vazirani problem is to
determine this \"secret\" string $s$.

::: wraptable
l7cm

::: tblr
r \@C=1em \@R=1em & & & & & & &\
& & & & & & &
:::
:::

[]{#cirq:bern_vazirani label="cirq:bern_vazirani"}

As usual, in order to implement this algorithm, we need a quantum oracle
for $f_s(x)$. In this case, the quantum oracle will be defined as for
the Deutsch-Jozsa's algorithm as
$\ket{x}\otimes \ket{y} \xrightarrow{U_{f_s}}{} \ket{x}\otimes \ket{y\oplus f_s(x)}$.
Similar to the case of the Deutsch-Jozsa, the state that will get
through the oracle will be
$\ket{x}\otimes \frac{1}{\sqrt{2}}(\ket{0}-\ket{1})$. The result will be
given by $\ket{x}(-1)^{f_s(x)}$ as shown in
[\[eq:deutsch_josza_C\]](#eq:deutsch_josza_C){reference-type="autoref"
reference="eq:deutsch_josza_C"}, where we decided to \"drop\" the second
part with $\ket{-}$. The circuit is given in
[\[cirq:bern_vazirani\]](#cirq:bern_vazirani){reference-type="autoref"
reference="cirq:bern_vazirani"}.

Let's now show mathematically the Bernstein-Vazirani algorithm:
$$\begin{aligned}
  \ket{0}^{\otimes n} \xrightarrow{\mathcal{H}^{\otimes n}} \sum_x^{2^n} \ket{x}
\end{aligned}$$ which is the state of the top-register before we reach
the quantum function evaluation. Further we write: $$\begin{aligned}
  \sum_x^{2^n} \ket{x}(\ket{0}-\ket{1}) &\xrightarrow{U_f} \sum_x^{2^n} (-1)^{f_s(x)}\ket{x} \\ 
                                        &=\sum_x^{2^n} (-1)^{s\cdot x} \ket{x} 
\end{aligned}$$ Then, we need to apply the Hadamard gate to this state.
We will then write the following: $$\begin{aligned}
  \sum_x^{2^n} (-1)^{s\cdot x} \ket{x} \xrightarrow[\text{\autoref{eq:hadamard_on_generic}}]{\mathcal{H}^{\otimes n}} \sum_x^{2^n} (-1)^{x\cdot s} 
  \sum_y^{2^n} (-1)^{x \cdot y} \ket{y} =\\
\sum_x^{2^n} \sum_y^{2^n} (-1)^{x\cdot s} (-1)^{x \cdot y} \ket{y} =\\
\sum_{x,y}^{2^n} (-1)^{(x\cdot s + x\cdot y)} \ket{y}
\end{aligned}$$ We now claim that the last expression
$\sum_{x,y} (-1)^{x\cdot s + x\cdot y}\ket{y} = \ket{s}$. It is not
straightforward to see so we can try to prove it (as in
[@noauthor_bernsteinvazirani_2022]). We first can rewrite
$x\cdot s + x\cdot y=x\cdot (s\oplus y)$. We can now take one fixed
$\ket{y}$ and sum over the $\ket{x}$'s: $$\begin{aligned}
  \sum_{x} (-1)^{x \cdot (s \oplus y)}
\end{aligned}$$ Now, if the chosen $\ket{y}$ is equal to the $s$, the
term $s\oplus y$ will be clearly zero. Therefore, if the chosen $y$
happens to be the same as $s$, the probability of obtaining it will be
maximum (we're adding all ones, as
$(-1)^{x\cdot(s\oplus y)} = \sum (-1)^{0}$). Consequently the only
non-zero term is associated to the state $\ket{y}=\ket{s}$.

Thus, using this algorithm, we're able to find the state
$\ket{y}=\ket{s}$ related to this \"secret\" string.

## Simons algorithm {#simons-algorithm .unnumbered}

Let's now consider the next algorithm, commonly known as the Simon's
algorithm or the Simon's problem. As usual we will treat the concept
mathematically, where it is nicely shown in Wikipedia
[@noauthor_simons_2023].

We first want to determine the problem statement. We are given some kind
of function $f(x)$ Often, we define this problem through the concept of
the whether this function is *one-to-one* or *two-to-one*. Both of these
notions can be formally related to some function properties, namely
surjection and injection. Anyways, the *one-to-one* function means that
for any input $x$ to the function $f(x)$, there's only one possible
output. The two-to-one means that there's possibly several inputs for
one single output. For example, $f(0)=0, f(1)=1, f(2)=2, f(3)=3$ - which
is a one-to-one function. Now, an example of a two-to-one function is
given by $f(0)=f(1)=0, f(2)=f(3)=1$. Note that for the inputs, they can
be represented as binary strings, representing numbers.

One can define it in another way, which is fully equivalent. Indeed, the
problem now goes as follows: we're given a function $f(x)$ and the
number/binary string $s$. We're now given a promise for $f(x)$: given
$f(x)$ and $s$, $f(x)=f(y)$ if and only if
$x\oplus y \in \{0^{\otimes n}, s\}$. That is, the output will be same
for two different inputs if and only if $x\oplus y$ is either
$0^{\otimes n}$ or $s$. Here, we define the operation $x \oplus y$ to be
the bitwise XOR. That is,
$x\oplus y \equiv (x_1 \text{ XOR } y_1, x_2 \text{ XOR } y_2, ..., x_n \text{ XOR } y_n)$.

::: wraptable
l7cm

::: tblr
c \@C=0.75em \@R=1em & & & & & & &\
& & & & & & &
:::
:::

[]{#cirq:simons label="cirq:simons"}

The goal of the algorithm is to determine the bitstring $s$. To
schematically show that these two formulations (in terms of one-to-one &
two-to-one) and the last one are equivalent, we first note that
$a \oplus b = 0^{\otimes n} \iff a=b$. Another fact that we notice is
the following: for some $x$ and $s$, we have that $x\oplus y = s$ is
unique for $x$ if and only if $s \neq 0^{\otimes n}$. In other words,
the output of the operation $s$ is uniquely determined by the inputs
only if $s=0^{\otimes n}$. Therefore, we say that if
$s\neq 0^{\otimes n}$, the function is two-to-one and if
$s=0^{\otimes n}$, the function is one-to-one.

Let's now consider the circuit of the algorithm. The circuit is given in
[\[cirq:simons\]](#cirq:simons){reference-type="autoref"
reference="cirq:simons"}. As usual, we're considering the initial state,
which will go through the first $\mathcal{H}$ and we'll obtain the usual
result

$$\begin{aligned}
  \mathcal{H}^{\otimes n} \ket{0}^{\otimes n}=\frac{1}{\sqrt{2^n}}\sum_{x=0}^{2^n-1} \ket{x}
\end{aligned}$$

Then we will apply our quantum function evaluation to the state on both
registers:

$$\begin{aligned}
  \sum_{x=0}^{2^n-1} \ket{x} \ket{0}^{\otimes n} \xrightarrow{f(x)} \sum_{x=0}^{2^n-1} \ket{x}\ket{f(x)\oplus x} =\sum_{x=0}^{2^n-1} \ket{x}\ket{f(x)} 
\end{aligned}$$

Which is nothing but the state after the function evaluation and before
the second $\mathcal{H}^{\otimes n}$ on the first register. We will then
obtain as usual: $$\begin{aligned}
  &\sum_{x=0}^{2^n-1} \ket{x}\ket{f(x)} \xrightarrow{(\mathcal{H}^{\otimes n})\otimes (\mathbbm{1}^{\otimes n}) } \\ 
  &\sum_{x=0}^{2^n-1} \biggl[ \sum_{y=0}^{2^n-1} (-1)^{x\cdot y}\ket{y} \biggr] \ket{f(x)}=\sum_{y=0}^{2^n-1}\ket{y} \biggl[ \sum_{x=0}^{2^n-1}(-1)^{x\cdot y}\ket{f(x)} \biggr]
\end{aligned}$$

which is our state that will be measured. In fact, as usual, we've
simplified the multiplicative factor. Therefore, the \"correct\" state
that we'll be measuring, will be as the one described above times the
factor $\nicefrac{1}{(2^n)}$. Therefore for a certain $\ket{y}$, the
probability of this happening will be given by $$\begin{aligned}
  \Bigg| \Bigg| \frac{1}{2^n} \sum_{x=0}^{2^n-1} (-1)^{x\cdot y} \ket{f(x)} \Bigg| \Bigg|^2
  \label{eq:simons_last_meas}
\end{aligned}$$ Now we consider the 2 possible cases (whether $f$ will
be one-to-one or two-to-one).

If the function $f(x)$ is one-to-one, the
[\[eq:simons_last_meas\]](#eq:simons_last_meas){reference-type="autoref"
reference="eq:simons_last_meas"} will give us the probability of
measuring some ket $\ket{y}$. An another way to write this probability
in
[\[eq:simons_last_meas\]](#eq:simons_last_meas){reference-type="autoref"
reference="eq:simons_last_meas"}, we can write the probability for a
state $\ket{y}$ to be measured will be given by $|\bra{y}\ket{x}|$.
Therefore, we have that the probability is given by nothing but
$$\begin{gathered}
  \Bigg< \frac{1}{2^n} \sum_{x=0}^{2^n-1} (-1)^{x\cdot y}\ket{f(x)} \Bigg| \frac{1}{2^n} \sum_{x'=0}^{2^n-1}(-1)^{x' \cdot y} \ket{f(x')} \Biggr> \\
  (\frac{1}{2^n})^2 \sum_{\substack{x=0,x'=0\\ x,x'}} (-1)^{x\cdot y} (-1)^{x' \cdot y} \bra{f(x)}\ket{f(x')}, \text{ using that } \bra{a}\ket{a'}=\delta_{a,a'} \\
   \frac{1}{2^{2n}} \sum_{x=0}^{2^n-1}(-1)^{2x\cdot y}= \frac{1}{2^{2n}} (2^n)\cdot(1)=\frac{1}{2^n}
   \label{eq:simons_inner_product}
\end{gathered}$$ Which is not surprising, as since $f$ is one-to-one,
we're going through all the basis vectors.

Now we consider the second case. That is, the case, where the function
is not one-to-one. We can follow the nice trick shown in Wikipedia
[@noauthor_simons_2023]. When the function is not one-to-one, this means
therefore that for some inputs $x_1$ & $x_2$, we have the same outputs
$f(x_1)=f(x_2)=z$, where $z$ is some kind of value in the range/domain
of the function $f$. For the specific case, one may write for the
probability for some chosen $\ket{y}$ as for
[\[eq:simons_last_meas\]](#eq:simons_last_meas){reference-type="autoref"
reference="eq:simons_last_meas"}. [@noauthor_simons_2023].
$$\begin{gathered}
  \Bigg|\Bigg| \frac{1}{2^n}\sum_{x=0}^{2^n-1} (-1)^{x\cdot y} \ket{f(x)} \Bigg|\Bigg|^2 = 
  \Bigg|\Bigg| \frac{1}{2^n} \sum_{z\in \text{Range}(f)}((-1)^{y\cdot x_1} +(-1)^{y\cdot x_2})\ket{z} \Bigg| \Bigg|^2
  \label{eq:simons_z_range}
\end{gathered}$$

::: wraptable
l3cm

   $x_1$   $x_2$   $s$
  ------- ------- -----
     0       0      0
     1       0      1
     0       1      1
     1       1      0

[]{#table:xor_truth_table label="table:xor_truth_table"}
:::

Note that here we've changed the sum over $x$ i.e. over sum of the
domain, to the sum over the range of its values $z$. We now note another
important property for the XOR operation. The truth table of XOR is
given by the
[\[table:xor_truth_table\]](#table:xor_truth_table){reference-type="autoref"
reference="table:xor_truth_table"}. From which we clearly see that
$x_1 \otimes x_2 = s \iff x_1 \otimes s = x_2$. Therefore, if this is
valid for one bit string, it will also be valid for any bit strings of
any length, as the bitwise XOR only operates on pairs of bits. Thus, by
observing the property of
$x_1 \otimes x_2 = s \iff x_1 \otimes s = x_2$, we can write the
[\[eq:simons_z_range\]](#eq:simons_z_range){reference-type="autoref"
reference="eq:simons_z_range"} as $$\begin{gathered}
  \Bigg|\Bigg| \frac{1}{2^n} \sum_{z\in \text{Range}(f)}((-1)^{y\cdot x_1} +(-1)^{y\cdot x_2})\ket{z} \Bigg| \Bigg|^2 =\\
  =\Bigg| \Bigg| \frac{1}{2^n} \sum_{z\in \text{Range}(f)}((-1)^{y\cdot x_1} +(-1)^{y\cdot (x_1 \otimes s)})\ket{z} \Bigg| \Bigg|^2 \\
  =\Bigg| \Bigg| \frac{1}{2^n} \sum_{z\in \text{Range}(f)}((-1)^{y\cdot x_1} +(-1)^{y\cdot x_1 \otimes y\cdot s)})\ket{z} \Bigg| \Bigg|^2 \\
  =\Bigg| \Bigg| \frac{1}{2^n} \sum_{z\in \text{Range}(f)} (-1)^{y\cdot x_1}(1+(-1)^{y\cdot s})\ket{z} \Bigg| \Bigg|^2 
\end{gathered}$$ From where, we can observe some things: if the chosen
$y$ happens to be such that $y\cdot s = 1$, then the probability (the
sum given right above) will be given by 0 (the factor in front of
$\ket{z}$ will be 0). Now, if the value of the product $y\cdot s = 0$,
it will not be zero. instead, the sum becomes of the form

$$\begin{gathered}
  \Bigg| \Bigg| \frac{1}{2^n} \sum_{z\in \text{Range}(f)} (-1)^{y\cdot x_1}(2)\ket{z} \Bigg| \Bigg|^2 \\
  \Bigg| \Bigg| \frac{1}{2^{n-1}} \sum_{z\in \text{Range}(f)} (-1)^{y\cdot x_1}\ket{z} \Bigg| \Bigg|^2 
\end{gathered}$$ Using the same trick as in
[\[eq:simons_inner_product\]](#eq:simons_inner_product){reference-type="autoref"
reference="eq:simons_inner_product"}, we can deduce that the probability
will be given by $\frac{1}{2^{n-1}}$.

From these two cases, we can therefore deduce the following: the
probability of measuring a certain $y$ if $s=0^{\otimes n}$ (the first
case) will be given by $\frac{1}{2^n}$. And the probability for a
certain $y$ if $s\neq 0^{\otimes n}$, we have 2 (sub)cases. That is,
depending on whether this $y$ will either obey $y\cdot s=0$ or
$y\cdot s\neq 0$. If it is the case of $y\cdot s=0$, we will have 0
probability of measuring this $\ket{y}$. If, on the other hand,
$y\cdot \neq 0$, it will be given by $\frac{1}{2^{n-1}}$.

Therefore, we deduce that in both cases, for some measured y, we will
have that [$y\cdot s =0$]{.underline} (as in the first case, $s=0$ by
definition and in the second, if it is not the case, the probability of
measuring the $y$ state will be zero).

During the mathematical process, starting from
[\[eq:simons_last_meas\]](#eq:simons_last_meas){reference-type="autoref"
reference="eq:simons_last_meas"}, we considered some specific $\ket{y}$
that we'll get at the end/output. So at the end we'll get several
$\ket{y}$'s with probability, depending on different cases, as discussed
above. The key point here is that these states, i.e. all $y$'s obey
$y\cdot s = 0$. As provided in [@noauthor_simons_2023], we use the
classical post processing in order to obtain the necessary $s$ as
required in the problem statement. It is important to note that, it may
happen that there are \"missing states\", as there are sometimes 0
probability of observing some variables.

## Fourier transform {#fourier-transform .unnumbered}

The quantum Fourier algorithm is, in my opinion, the \"first useful
algorithm\" considered here\... Lets recall the (not very formal)
definition of the classical Fourier transform. It is an operation
$\mathcal{F}$ transforming some function $f(x)$ to an another function
$f(y)$. $$\begin{gathered}
  f(x) \xrightarrow{\mathcal{F}} f(y) \; : \; f(y) = \int^{+\infty}_{-\infty}dx f(x) e^{-i2\pi y x}
\end{gathered}$$ From that, one can define the concept of the discrete
fourier transform. We use the analogy/mapping of the interval to a
vector. That is, we can discretize some interval into a vector of $N$
elements $\vec{v}=(v_0, v_1, ..., v_{N-1})$. We call the discretized
version of the Fourier transform, without surprise, the Discrete Fourier
Transform or DFT and defined by the mapping between two vectors
$\vec{x}=(x_0, x_1,..., x_{N-1})$ to $\vec{y}=(y_0, y_1,...,y_{N-1})$.
$$\begin{gathered}
  y_k = \sum_{n=0}^{N-1} x_n e^{-\frac{i2\pi}{N}kn}
\end{gathered}$$

To a very similar manner, one can define the quantum fourier transform,
which, instead of function-to-function and vector-to-vector mappings,
there's quantum state to quantum state mapping. Namely, the Fourier
transform maps some quantum state $\ket{x}\equiv \sum x_i \ket{i}$ to
$\ket{y}=\sum y_i\ket{i}$ for some basis vectors
$\{\ket{i}\}_{i\in \mathbb{N}}$. Thus we obtain the quantum Fourier
transform's definition $$\begin{gathered}
  \ket{y}\xrightarrow{\mathcal{F}} \ket{x}\\
  y_k=\frac{1}{\sqrt{N}} \sum_{n=0}^{N-1} x_n \omega_N^{kn} \text{ , with } \omega_N \equiv e^{i\frac{2\pi}{N}} \text{ and } k\in [0, N-1]
  \label{eq:qft_definition_components}
\end{gathered}$$ Note that here the sign of $\omega$'s power is
unimportant and is nothing but a convention. We also note the inverse
Fourier transform, given by $$\begin{gathered}
  \ket{x}\xrightarrow{\mathcal{F}} \ket{y}\\
  x_k=\frac{1}{\sqrt{N}} \sum_{n=0}^{N-1} y_n \omega_N^{-kn} \text{ , with } \omega_N \equiv e^{i\frac{2\pi}{N}} \text{ and } k\in [0, N-1]
\end{gathered}$$ as shown in beautiful Wikipedia
[@noauthor_quantum_2022], we can represent the quantum Fourier transform
with $$\begin{gathered}
  \ket{x} \xmapsto{\mathcal{F}_{\text{quant}}} \frac{1}{\sqrt{N}} \sum_{k=0}^{N-1}\omega_N^{xk}\ket{k}
  \label{eq:qft_mapsto}
\end{gathered}$$

Or, similarly, we can use the nice ket-bra representation of the
(unitary) QFT operator [@noauthor_quantum_nodate]: $$\begin{gathered}
  \mathcal{F}=\frac{1}{\sqrt{N}} \sum_{x=0}^{N-1} \sum_{k=0}^{N-1} \omega_{N}^{xk}\ket{k}\bra{x}
\end{gathered}$$

In addition to all that, we can also represent the quantum Fourier
transform as a $(N-1)\times (N-1)$ matrix operation, acting on a vector.
$$\begin{gathered}
  F_N=\frac{1}{\sqrt{N}} 
  \begin{bmatrix}
    1     & 1     & 1     & 1     & \cdots & 1    \\
    1     &\omega &\omega^2 & \omega^3 & \cdots & \omega^{N-1}\\
    1     &\omega^2 &\omega^4 & \omega^6 & \cdots & \omega^{2(N-1)}\\
    1     &\omega^3 &\omega^6 & \omega^9 & \cdots & \omega^{3(N-1)}\\
    \vdots &\vdots  & \vdots  & \vdots   & \ddots & \vdots        \\
    1      & \omega^{N-1}&\omega^{2(N-1)}&\omega^{3(N-1)} & \cdots & \omega^{(N-1)(N-1)}
  \end{bmatrix}
\end{gathered}$$

Now, before considering some general cases of the Quantum Fourier
transform and circuits, let's consider first some basic examples with
small number of qubits and other considerations.

First of all [@noauthor_quantum_nodate], we can consider the Fourier
Transform as not changing the initial state, but rather changing it to a
different representation in the so-called fourier basis. That is,
$\mathcal{F}\ket{x}=\ket{\tilde{x}}$.

#### 

Now let's consider one qubit system given by the most general expression
$\ket{\psi}=\alpha \ket{0} + \beta \ket{1}$. The one qubit, as usual
consists of 2 states (in the Z-basis). We can now look at all the
previous expressions written above, to have that $N=2$. Using that, we
can use, for example, the
[\[eq:qft_mapsto\]](#eq:qft_mapsto){reference-type="autoref"
reference="eq:qft_mapsto"}, or the component-by-component expression
[\[eq:qft_definition_components\]](#eq:qft_definition_components){reference-type="autoref"
reference="eq:qft_definition_components"}. Thus, for the 1 qubit system,
we have 2 components that we'll obtain. We will denote the components of
the vector/state $\ket{y}$ by $y_0$ and $y_1$. The components of the
\"input vector\" $\ket{\psi}$ with basis $\ket{0}$ and $\ket{1}$, are
given by respectively $\alpha$ and $\beta$. Thus, using the
[\[eq:qft_definition_components\]](#eq:qft_definition_components){reference-type="autoref"
reference="eq:qft_definition_components"} and the definition of $\omega$
, we have by components: $$\begin{gathered}
  y_0= \frac{1}{\sqrt{N}}\sum_{n=0}^{N-1}\omega_{N}^{kn} x_n \stackrel{N=2, k=0}{=} 
  \frac{1}{\sqrt{2}}\biggl( \alpha e^{\frac{i2\pi}{2}\cdot0\cdot0} + \beta e^{\frac{i2\pi}{2}\cdot 0\cdot 1} \biggr)=
  \frac{1}{\sqrt{2}}(\alpha + \beta )\\
  y_1= \frac{1}{\sqrt{N}}\sum_{n=0}^{N-1}\omega_{N}^{kn} x_n \stackrel{N=2,k=1}{=} 
  \frac{1}{\sqrt{2}}\biggl( \alpha e^{\frac{i2\pi}{2}\cdot1 \cdot0} + \beta e^{\frac{i2\pi}{2}\cdot 1\cdot 1} \biggr)=
  \frac{1}{\sqrt{2}}(\alpha + \beta e^{i\pi})=\frac{1}{\sqrt{2}}(\alpha - \beta) 
\end{gathered}$$

With that, we see that the state $\alpha\ket{0} + \beta\ket{1}$ gets
transformed to
$\frac{(\alpha+\beta)}{\sqrt{2}}\ket{0} + \frac{(\alpha - \beta)}{\sqrt{2}}\ket{1}$.
One may notice that this can be rewritten as
$\frac{\alpha}{\sqrt{2}}(\ket{0}+\ket{1}) + \frac{\beta}{\sqrt{2}}(\ket{0}-\ket{1})$,
which is nothing but $\alpha \ket{+} + \beta \ket{-}$. In other words,
$\alpha \ket{0} + \beta \ket{1} \xrightarrow{\mathcal{F}_{N=2}} \alpha \ket{+} + \beta \ket{-}$,
which is nothing but our Hadamard gate $\mathcal{H}$. Thus, the Fourier
transform of 2 state qubit is the $\mathcal{H}$. As it is mentioned in
[@noauthor_quantum_nodate], we can write the obtained
$\alpha \ket{0} + \beta \ket{1} \xrightarrow{\mathcal{F}_{N=2}} \tilde{\alpha} \ket{0} + \tilde{\beta} \ket{1}$
, which we call the *Fourier basis*.

Now, still following the path given in [@noauthor_quantum_nodate], we
can try to describe this transformation for a generic $n$ qubit case. In
this case, $N=2^n$. Then, we can write for the generic case:
$$\begin{gathered}
  \mathcal{F}_N \ket{x} = \frac{1}{\sqrt{N}}\sum_{y=0}^{N-1} \omega_N^{yx}\ket{y} =\\ 
                        = \frac{1}{\sqrt{N}} \sum_{y=0}^{N-1} e^{i\frac{2\pi xy}{2^n}} \ket{y}
\label{eq:qft_generic_1}
\end{gathered}$$ , now, we can use the fact that $\ket{y}$ represents a
tensor product $\bigotimes_i\ket{y_i}$ , with $\ket{y_i}\in \{0,1\}$. We
elaborate then further on the
[\[eq:qft_generic_1\]](#eq:qft_generic_1){reference-type="autoref"
reference="eq:qft_generic_1"}: $$\begin{gathered}
  \mathcal{F}_N \ket{x} = \frac{1}{\sqrt{N}} \sum_{y=0}^{N-1} e^{i2\pi (\sum_k \frac{y_k}{2^k})x} \ket{y_0 y_1 y_2...y_n}
  \label{eq:qft_generic_2}
\end{gathered}$$ We note however that in
[\[eq:qft_generic_2\]](#eq:qft_generic_2){reference-type="autoref"
reference="eq:qft_generic_2"}, we used the fact that
$\nicefrac{y}{2^n}=\sum_k^n \nicefrac{y_k}{2^k}$. This is true due to
the definition of a binary number notation. Indeed, some number $s$ can
be represented in binary in the form of $s=\sum_{k=1}^{n} s_k 2^k$, with
$n$ being the most signicative bit. Thus, by dividing the whole
expression by $2^n$, we will get
$\nicefrac{s}{2^n}=\sum_{k=1}^{n} s_k 2^{k-n}$. The desired expression
expression is obtained using the difference in the position of the
most/least significant bits, here, followed in
[@noauthor_quantum_nodate][^2]. Now, continuing to expand
[\[eq:qft_generic_2\]](#eq:qft_generic_2){reference-type="autoref"
reference="eq:qft_generic_2"}, we have: $$\begin{gathered}
  \mathcal{F}_N \ket{x} = \frac{1}{\sqrt{N}} \sum_{y=0}^{N-1} e^{i2\pi (\sum_k \frac{y_k}{2^k})x}\ket{y_0 y_1 y_2...y_n} \\
  = \frac{1}{\sqrt{N}} \sum_{y=0}^{N-1} \prod_{k}^{n} e^{i2\pi \frac{y_k}{2^k}}\ket{y_0 y_1 y_2...y_n}
\end{gathered}$$ Now, one can write the sum $\sum_{y=0}^{N-1}$ over the
$\ket{y_0y_1y_2...y_k}$ as the sum over the components $y_k$ of the
$\ket{y_0y_1y_2...y_k}$ as
$\sum_{y_0=0}^{1}\sum_{y_1=0}\sum_{y_2=0}...\sum_{y_n=0}$. The last step
[@hosgood_introduction_nodate] is to simply rewrite as a product of
different states. That is, $$\begin{gathered}
  \mathcal{F}_N \ket{x} = \frac{1}{\sqrt{N}} \sum_{y=0}^{N-1} \prod_{k}^{n} e^{i2\pi \frac{y_k}{2^k}}\ket{y_0 y_1 y_2...y_n} = 
  \bigotimes_{k=1}^{n}\biggl( \ket{0}+e^{2i\pi\frac{x}{2^k}}\ket{1} \biggr)
\end{gathered}$$

::: {#table:qft_crot_urot}
          $CROT_k=                       $UROT_k = 
         \begin{bmatrix}                \begin{bmatrix}
         \mathbbm{1}& 0 \\                   1 & 0 \\
           0 & UROT_k\\            0 & e^{\frac{2\pi i}{2^k}}\\
         \end{bmatrix}$                  \end{bmatrix}$
  ------------------------- ------------------------------------

  : The definitions of the $CROT_k$ and $UROT_k$ operators.
:::

Now, we're in position to consider the Quantum circuit of the fourier
transform. Before that, we'll first consider the building blocks of the
QFT, that is, the 2 gates-the $CROT_k$ and the $UROT_k$. Their
representations are given in
[\[table:qft_crot_urot\]](#table:qft_crot_urot){reference-type="autoref"
reference="table:qft_crot_urot"}. The action of the $CROT_k$ operator
can also be described as follows [@noauthor_quantum_nodate]:
$$\begin{gathered}
  CROT_k \ket{0\psi} = \ket{0 \psi}\\
  CROT_k \ket{1\psi} = e^{\frac{2\pi i}{2^k}\psi}\ket{1 \psi}, \text{ with } \ket{\psi} \text{ is a binary string}
\end{gathered}$$ We can now consider the circuit of the QFT. First, for
2 qubits, the 2-qubit QFT:

::: tblr
c \@C=1em \@R=1em & & & & &\
& & & & &
:::

Let's now write our usual description of the circuit, starting at some
states $\ket{x_1}\otimes\ket{x_2}$. The first gate will give the state
at $A$:
$\ket{\psi_A}=\mathcal{H}\otimes \mathbbm{1} (\ket{x_1}\otimes \ket{x_2}) = 
\frac{1}{\sqrt{2}}(\ket{0}+e^{\frac{2\pi i}{2}x_1}\ket{1})\otimes \ket{x_2}$.
Now, we can apply the $CROT_2$ operator, which, in bra-ket notation
gives
$CROT_2=\mathbbm{1}\otimes\ket{0}\bra{0}+UROT_2\otimes \ket{1}\bra{1}$.
Thus, by applying this operator to the state at A, we get
$$\begin{gathered}
CROT_2\biggl(\frac{1}{\sqrt{2}} \bigl(\ket{0}+e^{\frac{2\pi i}{2}x_1}\ket{1}\bigr)\otimes \ket{x_2}\biggr)=\\
=\biggl(\mathbbm{1}\otimes\ket{0}\bra{0}+UROT_2\otimes \ket{1}\bra{1}\biggr) \biggl(\frac{1}{\sqrt{2}}(\ket{0}\otimes\ket{x_2}+e^{\frac{2\pi i}{2}x_1}\ket{1}\otimes\ket{x_2})\biggr)=\\
=\frac{1}{\sqrt{2}}\biggl(\ket{0}\otimes \bra{0}\ket{x_2} + e^{\frac{2\pi i}{2}x_1}\ket{1}\otimes \bra{0}\ket{x_2}) \biggr)+\\
+ \frac{1}{\sqrt{2}}\biggl(\ket{0}\otimes \bra{1}\ket{x_2} + 
  [e^{\frac{2\pi i}{2}x_2}+e^{\frac{2\pi i}{2^2}x_2}]\otimes\bra{1}\ket{x_2}\biggr)
\end{gathered}$$ which will give different outcomees for different
inputs. Equivalently, in a less messy manner,
[@noauthor_quantum_nodate], we can write: $$\begin{gathered}
  CROT_2\biggl(\frac{1}{\sqrt{2}} \bigl(\ket{0}+e^{\frac{2\pi i}{2}x_1}\ket{1}\bigr)\otimes \ket{x_2}\biggr)\stackrel{\text{ctrl.-2, targ.-1}}{=}\\ 
  = \frac{1}{\sqrt{2}}\biggl( \ket{0}+ [e^{\frac{2\pi i}{2}x_1} + e^{\frac{2\pi i}{2^2}x_2}]\ket{1}\biggr) \otimes \ket{x_2}
\end{gathered}$$ With this idea, let's finally try to generalize it for
a more generic input of $n$ qubits. This by *replacing* the
$\otimes\ket{x_2}$ by $\otimes \ket{x_2x_3...x_n}$. Therefore, the state
after the first $UROT_2$ will be given by
$\frac{1}{\sqrt{2}}\biggl( \ket{0}+ [e^{\frac{2\pi i}{2}x_1} + e^{\frac{2\pi i}{2^2}x_2}]\ket{1}\biggr) \otimes \ket{x_2x_3...x_n}$
Then, the next step will undergo the next $n$ controlled $UROT_k$
operators with the $k$ qubit being the controlled qubit and the first
qubit being the target. After all the $n$ gates (using the same logic as
for the 2-qubit systems), we will get the state
[@noauthor_quantum_nodate]: $$\begin{gathered}
\frac{1}{\sqrt{2}}\biggl( \ket{0}+ [e^{\frac{2\pi i}{2}x_1} + 
e^{\frac{2\pi i}{2^2}x_2}\;...+...\; e^{\frac{2\pi i}{2^{n-1}}x_{n-1}} + e^{\frac{2\pi i}{2^{n}}x_{n}}]\ket{1}\biggr) \otimes \ket{x_2x_3...x_n}
\end{gathered}$$ Now, we can notice the already mentioned *trick* in
[\[eq:qft_generic_2\]](#eq:qft_generic_2){reference-type="autoref"
reference="eq:qft_generic_2"}. That is, the fact that in binary
representation, $x=2^{n-1}x_1+2^{n-2}x_2 + ...+ 2^1x_{n-1} + 2^0x_n$.
Thus, the sum expression in the square brackets (factor of
$\nicefrac{x_j}{2^j}$) is nothing but $\nicefrac{x}{2^n}$, giving us the
state $$\begin{gathered}
  \frac{1}{\sqrt{2}}\biggl( \ket{0}+e^{\frac{2\pi i}{2^n}x}\ket{1}\biggr) \otimes \ket{x_2x_3...x_n}
  \label{eq:qft_2nd_generic_step}
\end{gathered}$$ So up to now we performed the following things on the
1-n qubits: Apply the $\mathcal{H}$ followed by $n$ $UROT_k$ operators
with the first qubit as the target and the 1-n being the control ones.
The next steps are exactly the same, but now, the 2nd qubit becoms the
target and the 2-n become the controls. This is performed them for 3-n,
4-n, etc\... It can be easily shown from the
[\[eq:qft_2nd_generic_step\]](#eq:qft_2nd_generic_step){reference-type="autoref"
reference="eq:qft_2nd_generic_step"}, that, by applying subsequent
operations described above, we will subsequently get $$\begin{gathered}
\frac{1}{\sqrt{2}}\biggl( \ket{0}+e^{\frac{2\pi i}{2^n}x}\ket{1}\biggr)\otimes \ket{x_2x_3...x_n} \rightarrow\\
\frac{1}{\sqrt{2}}\biggl( \ket{0}+e^{\frac{2\pi i}{2^n}x}\ket{1}\biggr)\otimes \frac{1}{\sqrt{2}}\biggl( \ket{0}+e^{\frac{2\pi i}{2^{n-1}}x}\ket{1}\biggr)\otimes \ket{x_3...x_n} \rightarrow ... \\
\frac{1}{\sqrt{2}}\biggl( \ket{0}+e^{\frac{2\pi i}{2^n}x}\ket{1}\biggr)\otimes \frac{1}{\sqrt{2}}\biggl( \ket{0}+e^{\frac{2\pi i}{2^{n-1}}x}\ket{1}\biggr) \otimes ...\otimes \frac{1}{\sqrt{2}}\biggl( \ket{0}+e^{\frac{2\pi i}{2^0}x}\ket{1}\biggr)
\end{gathered}$$

::: tblr
c \@C=1em \@R=1em & & & & & &\
& & & & & &\
& & & & & &\
& & & & & &
:::

[^1]: The $\ket{0}-\ket{1}$ state can be created using the Hadamard gate
    applied on the state. TODO

[^2]: It is possible to check that this is true for any representations
    of binary numbers not depending on LSB/MSB's position
