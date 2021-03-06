time set day

# Define Variables
#	 Syntax
# 		var <variable_name> <integer>
var a 1
var b 1

# Variable Operations
#	 Syntax
#		op <variable_name> <operation> <number/variable_name>
# 		<operation> <variable_name> <number/variable_name>
#
# Operations: += | -= | *= | /= | %=
#		Addition: 			+=
# 		Substraction: 		-=
# 		Multiplication: 	*=
# 		Division: 			/=
# 		Mod: 				%=
op a /= 5
op a += b

# If
#	Syntax
#		if <variable_name> <bool_operator> <variable_name/number>
#		...
#		endif
#		if <variable_name> matches <number/range(1, 1.., ..1, 1..2)>
#		...
#		endif
#		ifnot <variable_name> <bool_operator> <variable_name/number>
#		...
#		endifnot
#		ifnot <variable_name> matches <number/range(1, 1.., ..1, 1..2)>
#		...
#		endifnot
# Boolean Operations: < | > | = | <= | >=
#		Less Than: 			<
#		More Than: 			>
#		Equal to: 			=
#		Less or Equal to:	<=
#		More or Equal to:	>=
if a < b
time set day
endif

# While
#	Syntax
#		while <variable_name> <bool_operator> <variable_name/number>
#		...
#		endwhile
#		while <variable_name> matches <number/range(1, 1.., ..1, 1..2)>
#		...
#		endwhile
#		whilenot <variable_name> <bool_operator> <variable_name/number>
#		...
#		endwhilenot
#		whilenot <variable_name> matches <number/range(1, 1.., ..1, 1..2)>
#		...
#		endwhilenot
while a < b
time set day
endwhile