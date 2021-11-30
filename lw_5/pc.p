    var x, y, z
begin
    readln(y)
    x := 3 + y
    z := 3 + y
    writeln(z)
    y := y - 1
    z := 3 + y
    writeln(z)
    case x of
        3 : x := x + F,
        F : x := x + 3
    end
    writeln(x)
end