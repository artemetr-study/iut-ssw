    var x, y
begin
    readln(y)
    x := 3 + y
    case x of
        3 : x := x + F,
        F : x := x + 3
    end
    writeln(x)
end