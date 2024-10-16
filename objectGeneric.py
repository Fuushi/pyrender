#.obj has several components
    #v <- vertex, contains coordinates
    #vt <- vertex texture, contains 2 floats
    #vn <- vertex normal, contains 3 floats describing normal value
    #f <- face, contains 4 int vectors
        #(vertex, vertex texture, normal texture)

class game_object(object):
    def __init__(self): #self?
        print('initializing object')
        return None

    #idk add methods or somthing

class object_math():
    def apply_pos(vertex, object_pos):
        #print('mathing')
        new_vertex = [0, 0, 0]
        for i in range(3):
            new_vertex[i] = (vertex[i] + object_pos[i])
        #print('math done')
        return(new_vertex)

class serialize():
    def serialize(): #<- probly not nessisary, just pickle the object to bytes
        return()

    def de_serialize(data): #<- either make obj specific or add support4more files
        vertexArray = []
        vertexTextureArray = []
        vertexNormalArray = []
        faceArray = []

        for line in data:

            #refactor dipshit

            if line[:2] == 'v ':
                #format line
                ev = line.rstrip()[2:]
                sub = ''
                subArr = []
                for char in range(len(ev)):
                    if ev[char] == ' ':
                        subArr.append(sub)
                        sub = ''
                        #print(subArr)
                    else:
                        sub = sub + ev[char]
                subArr.append(sub)
                sub = ''

                #print(subArr)
                floatArr = []
                for float in subArr:
                    floatArr.append(eval(float))

                #print('FloatArray: ', floatArr) #floatArr is just the 
                vertexArray.append(floatArr)
                #print('VertexArray: ', vertexArray)


            elif line[:2] == 'vt':
                vertexTextureArray.append(line.rstrip())
            elif line[:2] == 'vn':
                vertexNormalArray.append(line.rstrip())
            elif line[:2] == 'f ': #probly parse face data into a more readable format
                #face array starts with containing raw, reformat before return
                faceArray.append(line.rstrip())

        #reformat face array

        searcherArray = []

        for face in faceArray:
            print(face)
            cache = face[2:]
            sub_str = ''
            sub_arr = []
            for i in range(len(cache)):
                if cache[i] == ' ':
                    sub_arr.append(sub_str)
                    sub_str = ''
                else:
                    sub_str = sub_str + cache[i]
            sub_arr.append(sub_str)
            #searcherArray.append(sub_arr)
            print(sub_arr)
            ##now turn 50/45/34 into [50, 45, 34]
            retArray = [] #<- optimise
            for ind in sub_arr:
                temp = eval(('[' + ind.replace('/', ',') + ']'))
                temp[0] -= 1
                retArray.append(
                    temp
                )
            
            searcherArray.append(retArray)
        #print('search: ', searcherArray)
        #print(vertexArray)
        #ait = input()
        faceArray = searcherArray
        
        return([vertexArray, vertexTextureArray, vertexNormalArray, faceArray])