module Math

open System.Numerics 

let All l =
    Seq.fold (fun acc elem -> acc && elem) true l

let Any l = 
    Seq.fold (fun acc elem -> acc || elem) false l

let In l n =
    Seq.exists (fun elem -> elem = n) l

let prnt fmtStr elem =
    printfn fmtStr elem
    elem

let rec powMod ( x : BigInteger ) ( y : BigInteger ) ( m : BigInteger ) =
    match y with
    | _ when y = 1I -> x
    | _ when y % 2I = 1I -> x * (powMod x (y-1I) m) % m
    | _ -> powMod (x*x%m) (y/2I) m

let primesBelow n = 
    let rec filterComposites next_num max_num numbers = 
        let n = numbers |> List.find (fun elem -> elem >= next_num)
        match n with 
        | _ when n > max_num -> numbers
        | _ -> numbers 
            |> List.filter (fun elem -> elem <= n || elem % n <> 0)
            |> filterComposites (n+1) max_num
    filterComposites 2 (n |> float |> sqrt |> int) (2 :: [3..2..(n-1)])

let prime ( p : BigInteger ) =
    let some_primes = [2I;3I;5I;7I]
    match p with
    | x when x <= Seq.max some_primes ->
        p |> In some_primes
    | _ -> 
        some_primes
        |> Seq.map (fun n -> (p % n <> 0I) && powMod n (p-1I) p = 1I)
        |> All
