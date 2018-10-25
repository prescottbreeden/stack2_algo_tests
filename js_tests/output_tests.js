const calc = require('./Calculator')
const f = require('./functions')
const SLL = require('./sll')

arr = [1,2,3,4,5]
obj = { 'balls': 'hurt' }


f.PrintKeysAndValues(obj) 
f.ReverseArray(arr)
list = new SLL()
list.AddToFront(1)
list.AddToFront(2)
list.AddToFront(3)
list.AddToFront(4)
// list.AddToBack(2)
list.PrintValues()


// c = new calc()
// c.add(1)
// c.divide(2)
// console.log(c.total)
