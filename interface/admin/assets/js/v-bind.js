Vue.component('todo-item', {
  props: ['todo'],
  template: '<li>{{ todo.text }} </li>'
})
var app8 = new Vue({
  el: '#app8',
  data: {
    list: [
      { text: 'Vegetables' },
      { text: 'Cheese' },
      { text: 'Whatever else humans are supposed to eat' }
    ]
  }
})