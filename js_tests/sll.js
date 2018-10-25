const Node = require('./node')

module.exports = class SLL {

  constructor() {
    this.head = null
  }

  AddToFront(val) {
    const node = new Node(val)
    if (this.head) {
      // let temp = this.head
      // this.head = node
      // this.head.next = temp
      node.next = this.head
      this.head = node
    } else {
      this.head = node
    }
  }

  AddToBack(val) {
    const node = new Node(val)
    if (this.head) {
      let runner = this.head
      while(runner.next) {
        runner = runner.next
      }
      runner.next = node
    } else {
      this.head = node
    }
  }

  PrintValues() {
    let runner = this.head
    while(runner) {
      console.log(runner.val)
      runner = runner.next
    }
  }

  
}
