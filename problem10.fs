open Math

let sumPrimesBelow n =
    primesBelow n
    |> Seq.map (fun elem -> bigint elem)
    |> Seq.sum

sumPrimesBelow 2000000 |> printfn "%A"
