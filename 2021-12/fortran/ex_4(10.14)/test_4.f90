program test4
    implicit none
    integer s

    call arithmetic(100,s)

    write(*,*) s
end program test4

recursive subroutine arithmetic(n,arith)
    implicit none
    integer, intent(in)::n
    integer, intent(out)::arith
    integer tmp

    if(n == 1)then
        arith = 1
    else
        call arithmetic(n-1,tmp)
        arith = tmp + n
    end if
    return

end subroutine arithmetic