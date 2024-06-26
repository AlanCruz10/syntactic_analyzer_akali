
variables = {}
variables_err = []
functions = {}
function_err = []
loops = {}
loop_err = []
conditionals = {}
conditional_err = []


def validate_condition(p1, p2, p3):
    p0 = None
    if p2 == "<":
        if isinstance(p1, (int, float)) and isinstance(p3, (int, float)):
            p0 = p1 < p3
        elif isinstance(p1, (int, float)) and (('Ent', p3) in variables or ('Dcm', p3) in variables):
            p0 = p1 < (variables[('Ent', p3)] if ('Ent', p3) in variables else variables[('Dcm', p3)])
        elif (('Ent', p1) in variables or ('Dcm', p1) in variables) and isinstance(p3, (int, float)):
            p0 = (variables[('Ent', p1)] if ('Ent', p1) in variables else variables[('Dcm', p1)]) < p3
        elif (('Ent', p1) in variables or ('Dcm', p1) in variables) and (
                ('Ent', p3) in variables or ('Dcm', p3) in variables):
            p0 = (variables[('Ent', p1)] if ('Ent', p1) in variables else variables[('Dcm', p1)]) < (
                variables[('Ent', p3)] if ('Ent', p3) in variables else variables[('Dcm', p3)])
        else:
            print(f"La condicional '{p1} '{p2}' '{p3}' no es valida, Valor '{p1}' o '{p3}' no es valido")
    elif p2 == ">":
        if isinstance(p1, (int, float)) and isinstance(p3, (int, float)):
            p0 = p1 > p3
        elif isinstance(p1, (int, float)) and (('Ent', p3) in variables or ('Dcm', p3) in variables):
            p0 = p1 > (variables[('Ent', p3)] if ('Ent', p3) in variables else variables[('Dcm', p3)])
        elif (('Ent', p1) in variables or ('Dcm', p1) in variables) and isinstance(p3, (int, float)):
            p0 = (variables[('Ent', p1)] if ('Ent', p1) in variables else variables[('Dcm', p1)]) > p3
        elif (('Ent', p1) in variables or ('Dcm', p1) in variables) and (
                ('Ent', p3) in variables or ('Dcm', p3) in variables):
            p0 = (variables[('Ent', p1)] if ('Ent', p1) in variables else variables[('Dcm', p1)]) > (
                variables[('Ent', p3)] if ('Ent', p3) in variables else variables[('Dcm', p3)])
        else:
            print(f"La condicional '{p1} '{p2}' '{p3}' no es valida, Valor '{p1}' o '{p3}' no es valido")
    elif p2 == "<=":
        if isinstance(p1, (int, float)) and isinstance(p3, (int, float)):
            p0 = p1 <= p3
        elif isinstance(p1, (int, float)) and (('Ent', p3) in variables or ('Dcm', p3) in variables):
            p0 = p1 <= (variables[('Ent', p3)] if ('Ent', p3) in variables else variables[('Dcm', p3)])
        elif (('Ent', p1) in variables or ('Dcm', p1) in variables) and isinstance(p3, (int, float)):
            p0 = (variables[('Ent', p1)] if ('Ent', p1) in variables else variables[('Dcm', p1)]) <= p3
        elif (('Ent', p1) in variables or ('Dcm', p1) in variables) and (
                ('Ent', p3) in variables or ('Dcm', p3) in variables):
            p0 = (variables[('Ent', p1)] if ('Ent', p1) in variables else variables[('Dcm', p1)]) <= (
                variables[('Ent', p3)] if ('Ent', p3) in variables else variables[('Dcm', p3)])
        else:
            print(f"La condicional '{p1} '{p2}' '{p3}' no es valida, Valor '{p1}' o '{p3}' no es valido")
    elif p2 == ">=":
        if isinstance(p1, (int, float)) and isinstance(p3, (int, float)):
            p0 = p1 >= p3
        elif isinstance(p1, (int, float)) and (('Ent', p3) in variables or ('Dcm', p3) in variables):
            p0 = p1 >= (variables[('Ent', p3)] if ('Ent', p3) in variables else variables[('Dcm', p3)])
        elif (('Ent', p1) in variables or ('Dcm', p1) in variables) and isinstance(p3, (int, float)):
            p0 = (variables[('Ent', p1)] if ('Ent', p1) in variables else variables[('Dcm', p1)]) >= p3
        elif (('Ent', p1) in variables or ('Dcm', p1) in variables) and (
                ('Ent', p3) in variables or ('Dcm', p3) in variables):
            p0 = (variables[('Ent', p1)] if ('Ent', p1) in variables else variables[('Dcm', p1)]) >= (
                variables[('Ent', p3)] if ('Ent', p3) in variables else variables[('Dcm', p3)])
        else:
            print(f"La condicional '{p1} '{p2}' '{p3}' no es valida, Valor '{p1}' o '{p3}' no es valido")
    elif p2 == "==":
        if (isinstance(p1, (int, float)) and isinstance(p3, (int, float))) or (
                isinstance(p1, str) and isinstance(p3, str)) or (isinstance(p1, bool) and isinstance(p3, bool)):
            p0 = p1 == p3
        elif isinstance(p1, (int, float)) and (('Ent', p3) in variables or ('Dcm', p3) in variables):
            p0 = p1 == (variables[('Ent', p3)] if ('Ent', p3) in variables else variables[('Dcm', p3)])
        elif (('Ent', p1) in variables or ('Dcm', p1) in variables) and isinstance(p3, (int, float)):
            p0 = (variables[('Ent', p1)] if ('Ent', p1) in variables else variables[('Dcm', p1)]) == p3
        elif (('Ent', p1) in variables or ('Dcm', p1) in variables) and (
                ('Ent', p3) in variables or ('Dcm', p3) in variables):
            p0 = (variables[('Ent', p1)] if ('Ent', p1) in variables else variables[('Dcm', p1)]) == (
                variables[('Ent', p3)] if ('Ent', p3) in variables else variables[('Dcm', p3)])
        elif isinstance(p1, str) and (('Cdn', p3) in variables):
            p0 = p1 == variables[('Cdn', p3)]
        elif (('Cdn', p1) in variables) and isinstance(p3, str):
            p0 = variables[('Cdn', p1)] == p3
        elif (('Cdn', p1) in variables) and (('Cdn', p3) in variables):
            p0 = variables[('Cdn', p1)] == variables[('Cdn', p3)]
        elif isinstance(p1, bool) and (('Bool', p3) in variables):
            p0 = p1 == variables[("Bool", p3)]
        elif (('Bool', p1) in variables) and isinstance(p3, bool):
            p0 = variables[('Bool', p1)] == p3
        elif (('Bool', p1) in variables) and (('Bool', p3) in variables):
            p0 = variables[('Bool', p1)] == variables[('Bool', p3)]
        else:
            print(f"La condicional '{p1} '{p2}' '{p3}' no es valida, Valor '{p1}' o '{p3}' no es valido")
    elif p2 == "!=":
        if (isinstance(p1, (int, float)) and isinstance(p3, (int, float))) or (
                isinstance(p1, str) and isinstance(p3, str)) or (isinstance(p1, bool) and isinstance(p3, bool)):
            p0 = p1 != p3
        elif isinstance(p1, (int, float)) and (('Ent', p3) in variables or ('Ent', p3) in variables):
            p0 = p1 != (variables[('Ent', p3)] if ('Ent', p3) in variables else variables[('Dcm', p3)])
        elif (('Ent', p1) in variables or ('Dcm', p1) in variables) and isinstance(p3, (int, float)):
            p0 = (variables[('Ent', p1)] if ('Ent', p1) in variables else variables[('Dcm', p1)]) != p3
        elif (('Ent', p1) in variables or ('Dcm', p1) in variables) and (
                ('Ent', p3) in variables or ('Dcm', p3) in variables):
            p0 = (variables[('Ent', p1)] if ('Ent', p1) in variables else variables[('Dcm', p1)]) != (
                variables[('Ent', p3)] if ('Ent', p3) in variables else variables[('Dcm', p3)])
        elif isinstance(p1, str) and (('Cdn', p3) in variables):
            p0 = p1 != variables[('Cdn', p3)]
        elif (('Cdn', p1) in variables) and isinstance(p3, str):
            p0 = variables[('Cdn', p1)] != p3
        elif (('Cdn', p1) in variables) and (('Cdn', p3) in variables):
            p0 = variables[('Cdn', p1)] != variables[('Cdn', p3)]
        elif isinstance(p1, bool) and (('Bool', p3) in variables):
            p0 = p1 != variables[('Bool', p3)]
        elif (('Bool', p1) in variables) and isinstance(p3, bool):
            p0 = variables[('Bool', p1)] != p3
        elif (('Bool', p1) in variables) and (('Bool', p3) in variables):
            p0 = variables[('Bool', p1)] != variables[('Bool', p3)]
        else:
            print(f"La condicional '{p1} '{p2}' '{p3}' no es valida, Valor '{p1}' o '{p3}' no es valido")
    else:
        print(f"Operador '{p2}' no es un operador valido")
    return p0


def grammar_variables(parse, i):
    type_variable = parse[i + 1]
    name = parse[i + 2]
    value = parse[i + 3]
    if type_variable == "Ent":
        if isinstance(str(value) if isinstance(value, bool) else value, int) or value is None:
            variables[(type_variable, name)] = value
        else:
            variables_err.append(f"Error en el valor de la variable {name}, debe de ser entero'")
    elif type_variable == "Bool":
        if isinstance(value, bool) or value is None:
            variables[(type_variable, name)] = value
        else:
            variables_err.append(f"Error en el valor de la variable {name}, debe de ser boleano'")
    elif type_variable == "Dcm":
        if isinstance(value, float) or value is None:
            variables[(type_variable, name)] = value
        else:
            variables_err.append(f"Error en el valor de la variable {name}, debe de ser float'")
    elif type_variable == "Cdn":
        if isinstance(value, str) or value is None:
            variables[(type_variable, name)] = value
        else:
            variables_err.append(f"Error en el valor de la variable {name}, debe de ser cadena'")


def grammar_conditionals(parse, i):
    condition = parse[i + 1]
    validate = validate_condition(condition[0], condition[1], condition[2])
    if validate:
        print("1")
        if parse[i + 2] is not None:
            analyze_semantic(parse[i + 2])
    elif validate is None:
        print("2")
        pass
    else:
        return False


def grammar_loop(parse, i):
    for_conditional = parse[i + 1]
    start = for_conditional[0]
    end = for_conditional[1]
    operator = for_conditional[2]
    if start < end:
        if operator == '+':
            for _ in range(start, end + 1):
                if parse[i + 2] is not None:
                    analyze_semantic(parse[i + 2])
        else:
            print(f"El inicio no puede ir en decremento")
    else:
        if operator == '-':
            for _ in reversed(range(end, start + 1)):
                analyze_semantic(parse[i + 2])
        else:
            print(f"El inicio no puede ir en aumento")


def valid_function_returned_value(function_type, variable):
    variable_found = validate_variables_existence(variable)

    if variable_found:
        if variable_found[0][0] == function_type:
            return variable_found
        else:
            function_err.append(f'Tipo de dato variable "{variable}" no valido en retorno')

    return None


def validate_variables_existence(variable):
    for key, value in variables.items():
        if key[1] == variable:
            return key, value

    function_err.append(f"Variable '{variable}' no declarada")
    return None


def grammar_function(parse, i):
    if parse[i + 1] is None:
        if parse[i + 3] is None:
            if parse[i + 4] is None:
                name = parse[i + 2]
                functions[name] = (None, name, None, None, None)
            else:
                name = parse[i + 2]
                content = parse[i + 4]
                analyze_semantic(content)
                functions[name] = (None, name, None, content, None)
        else:
            if parse[i + 4] is None:
                name = parse[i + 2]
                parameter = validate_variables_existence(parse[i + 3])
                if parameter:
                    functions[name] = (None, name, parameter, None, None)
                else:
                    print("Variable en parametro no declarada")
            else:
                if parse[i + 5] is None:
                    name = parse[i + 2]
                    content = parse[i + 4]
                    parameter = validate_variables_existence(parse[i + 3])
                    if parameter:
                        analyze_semantic(content)
                        functions[name] = (None, name, parameter, content, None)
                    else:
                        print("Variable en parametro no declarada")
    else:
        if parse[i + 3] is None:
            if parse[i + 4] is None:
                type = parse[i + 1]
                name = parse[i + 2]
                rtn = valid_function_returned_value(type, parse[i + 5])
                if rtn:
                    functions[name] = (type, name, None, None, rtn)
                else:
                    print("Valor de retorno no coincide con tipo de función")
            else:
                type = parse[i + 1]
                name = parse[i + 2]
                content = parse[i + 4]
                analyze_semantic(content)
                rtn = valid_function_returned_value(type, parse[i + 5])
                if rtn:
                    functions[name] = (type, name, None, content, rtn)
                else:
                    print("Valor de retorno no coincide con tipo de función")
        else:
            if parse[i + 4] is None:
                type = parse[i + 1]
                name = parse[i + 2]
                parameter = validate_variables_existence(parse[i + 3])
                if parameter:
                    rtn = valid_function_returned_value(type, parse[i + 5])
                    if rtn:
                        functions[name] = (type, name, parameter, None, rtn)
                    else:
                        print("Valor de retorno no coincide con tipo de función")
                else:
                    print("Variable en parametro no declarada")
            else:
                type = parse[i + 1]
                name = parse[i + 2]
                parameter = validate_variables_existence(parse[i + 3])
                if parameter:
                    content = parse[i + 4]
                    analyze_semantic(content)
                    rtn = valid_function_returned_value(type, parse[i + 5])
                    if rtn:
                        functions[name] = (type, name, parameter, content, rtn)
                    else:
                        print("Valor de retorno no coincide con tipo de función")
                else:
                    print("Variable en parametro no declarada")


def analyze_semantic(parse):
    variables.clear()
    variables_err.clear()
    functions.clear()
    function_err.clear()
    loops.clear()
    loop_err.clear()
    conditionals.clear()
    conditional_err.clear()

    counter = 0
    for i, code in enumerate(parse):
        if counter == 0:
            if code == "gv":
                grammar_variables(parse, i)
            elif code == "gc":
                if not grammar_conditionals(parse, i):
                    counter = 2
            elif code == "gcf":
                grammar_loop(parse, i)
            elif code == "gf":
                grammar_function(parse, i)
            elif isinstance(code, tuple):
                analyze_semantic(code)
        else:
            counter -= 1

    print("Errores: \n")
    [print(t) for t in variables_err]
    [print(t) for t in conditional_err]
    [print(t) for t in conditional_err]

