// Advanced Programming, A. Wąsowski, IT University of Copenhagen
// Based on Functional Programming in Scala, 2nd Edition

package adpro.adt

import java.util.NoSuchElementException
import scala.annotation.tailrec

enum List[+A]:
  case Nil
  case Cons(head: A, tail: List[A])


object List: 

  def head[A] (l: List[A]): A = l match
    case Nil => throw NoSuchElementException() 
    case Cons(h, _) => h                                                                                                                                                                                                                                       
  
  def apply[A] (as: A*): List[A] =
    if as.isEmpty then Nil
    else Cons(as.head, apply(as.tail*))

  def append[A] (l1: List[A], l2: List[A]): List[A] =
    l1 match
      case Nil => l2
      case Cons(h, t) => Cons(h, append(t, l2)) 

  def foldRight[A, B] (l: List[A], z: B, f: (A, B) => B): B = l match
    case Nil => z
    case Cons(a, as) => f(a, foldRight(as, z, f))
    
  def map[A, B] (l: List[A], f: A => B): List[B] =
    foldRight[A, List[B]] (l, Nil, (a, z) => Cons(f(a), z))

  // Exercise 1 (is to be solved without programming)

  // Exercise 2

  def tail[A] (l: List[A]): List[A] = l match
    case Nil => throw NoSuchElementException()
    case Cons(x, xs) => xs

  // Exercise 3
  
  @tailrec
  def drop[A](l: List[A], n: Int): List[A] = l match
    case l if n <= 0 => l
    case Nil => throw NoSuchElementException()
    case Cons(x, xs) => drop(xs, n - 1)

  // Exercise 4

  @tailrec
  def dropWhile[A](l: List[A], p: A => Boolean): List[A] = l match
    case Nil => l
    case Cons(x, xs) if p(x) => dropWhile(xs, p)
    case Cons(x, xs) => l


  // Exercise 5
  def init[A] (l  : List[A]): List[A] = l match
    case Nil => throw NoSuchElementException()
    case Cons(x, Nil) => Nil
    case Cons(x, xs) => Cons(x, init(xs))

  // Exercise 6

  def length[A] (l: List[A]): Int =
    foldRight(l, 0, (_, acc) => acc + 1)


  // Exercise 7

  @tailrec
  def foldLeft[A, B](l: List[A], z: B, f: (B, A) => B): B = l match
    case Nil => z
    case Cons(x, xs) => foldLeft(xs, f(z, x), f)


  // Exercise 8

  def product (as: List[Int]): Int =
    foldLeft(as, 1, (x, y) => x * y)

  def length1[A] (as: List[A]): Int =
    foldLeft(as, 0, (acc, x) => acc + 1)

  // Exercise 9

  def reverse[A] (l: List[A]): List[A] =
    foldLeft(l, List(), (acc, x) => Cons(x, acc))
 
  // Exercise 10

  def foldRight1[A, B] (l: List[A], z: B, f: (A, B) => B): B =
    foldLeft(reverse(l), z, (x, acc) => f(acc, x))

  // Exercise 11

  def foldLeft1[A, B] (l: List[A], z: B, f: (B, A) => B): B = ???
 
  // Exercise 12

  def concat[A] (l: List[List[A]]): List[A] =
    foldLeft(l, List(), (acc, xs) => List.append(acc, xs))
  
  // Exercise 13

  def filter[A] (l: List[A], p: A => Boolean): List[A] =
    foldRight(l, List(), (x, acc) => if p(x) then Cons(x, acc) else acc)
 
  // Exercise 14

  def flatMap[A,B] (l: List[A], f: A => List[B]): List[B] =
    foldRight(l, List(), (xs, acc) => List.append(f(xs), acc))

  // Exercise 15

  def filter1[A] (l: List[A], p: A => Boolean): List[A] =
    flatMap(l, x => if p(x) then List(x) else Nil)

  // Exercise 16

  def addPairwise (l: List[Int], r: List[Int]): List[Int] = ???

  // Exercise 17

  def zipWith[A, B, C] (l: List[A], r: List[B], f: (A,B) => C): List[C] = ???

  // Exercise 18

  def hasSubsequence[A] (sup: List[A], sub: List[A]): Boolean = ???
