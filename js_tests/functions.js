module.exports = {

  PrintKeysAndValues: function(obj) {
    for(let k in obj) {
      console.log(k, obj[k])
    }
  },

  ReverseArray: function(arr) {
    for(let i = 0; i < arr.length/2; i++) {
      temp = arr[i]
      arr[i] = arr[arr.length-1-i]
      arr[arr.length-1-i] = temp
    }
    console.log(arr)
  }

}

