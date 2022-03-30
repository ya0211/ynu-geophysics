program test4
    implicit none
    integer year

    write(*,*)"Enter the year"
    read(*,*)year
    
    if(mod(year,100)==0)then
        if(mod(year,400)==0)then
            write(*,*)"366 days in the year"
        else
            write(*,*)"365 days in the year"
        endif
    else if(mod(year,4)==0)then
        write(*,*)"366 days in the year"
    else
        write(*,*)"365 days in the year"
    endif

end