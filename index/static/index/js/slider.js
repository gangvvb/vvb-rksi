const step = 320
let counter = 0

const slides = Array(...document.querySelectorAll('#slide'))
const line = document.querySelector('#line')


document.querySelector('#next').addEventListener('click', () => {
    const position = parseInt(line.style.left.replace('px',''))
    const sum = slides.length - Math.floor(document.querySelector('#slider').clientWidth/310)

    console.log(document.querySelector('#slider').clientWidth)

    if (counter < sum) {
        line.style.left = position - step + 'px'
        counter++
    }
})

document.querySelector('#back').addEventListener('click', () => {
    const position = parseInt(line.style.left.replace('px',''))
    const sum = slides.length - Math.floor(document.querySelector('#slider').clientWidth/step)


    if (counter > 0) {
        line.style.left = position + step + 'px'
        counter--
    }
})
