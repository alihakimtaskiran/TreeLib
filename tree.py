def get_tree(f):
    with open(f,"r") as o:
        f=o.read()
        o.close()
    del o
    try:
        classes=[]
        i=0
        x=len(f)
        while i<x-1:
            i+=1
            try:
                j=f[i:].index("class")
                if i+j not in classes:
                    classes.append(i+j)
            except:
                pass
        
        
        del i,j,x
        classes_=[]
        for i in classes:
            try:
                j=f[i:].index(":")
                k=f[i:i+j].replace("class","").replace(" ","")
                classes_.append(k)
            except:
                pass
        classes=tuple(classes_.copy())
        del classes_,i,j,k
        
        sub_clss=[]
        for i in range(len(classes)-1):
            k=f[f.index(classes[i]):f.index(classes[i+1])]
            sub_clss.append(k)
        
        sub_clss.append(f[f.index(classes[-1]):])
        del i,k,f
        
        def_in=[]
        
        for j in range(len(sub_clss)):
            sub=sub_clss[j]
            def_in.append([])
            t=len(sub)
            i=0
            while i<t:
                try:
                    k=sub[i:].index("def ")
                    if k+i not in def_in[j]:
                       def_in[j].append(k+i)
                       i=k-1
                    else:
                        pass
                except:
                    break
                i+=1
        
        del i,j,k,t,sub
        functions={}
        
        for i in range(len(sub_clss)):
            sub=sub_clss[i]
            k=len(def_in[i])
            functions[classes[i]]=[]
            for j in range(k):
                if not j==k-1:    
                    tmp=sub[def_in[i][j]:def_in[i][j+1]]
                else:
                    tmp=sub[def_in[i][-1]:]
                tmp=tmp[:tmp.index(":")].replace("def","").replace(" ","").replace("self","").replace("(,","(")
                functions[classes[i]].append(tmp)
        
        del def_in,i,j,k,sub,sub_clss,tmp
        
        ##Graph
        tree=""
        l=[]
        for i in classes:
            l.append(len(i))
        l=max(l)
        for i in classes:
            if not i==classes[-1]:
                tree+="|----"+i+(l-len(i))*"-"+"----|\n"
                tmp=functions[i]
                for j in range(len(tmp)):    
                    tree+="|"+" "*(l+8)+"|---"+tmp[j]+"\n"
                tree+="|\n|\n"
            else:
                tree+="|----"+i+(l-len(i))*"-"+"----|\n"
                tmp=functions[i]
                for j in range(len(tmp)):    
                    tree+=" "*(l+9)+"|---"+tmp[j]+"\n"
                    
        return tree
    except:
        raise ValueError("Argument doesn't have any class")
