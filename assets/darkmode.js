dark = false
function lightsOut() {
    
    if(!dark) {
        // Start with the body
        document.body.classList.add("bg-dark")

        // Then the jumbotrons
        jumboList = document.getElementsByClassName('jumbotron')
        for(x = 0; x<jumboList.length; x++) {
            jumboList[x].classList.add('bg-dark')
            jumboList[x].classList.add('text-white')
            jumboList[x].classList.add('border')
            jumboList[x].classList.add('border-white')
        }

        // The buttons
        buttons = document.getElementsByClassName('btn')
        for(x = 0; x<buttons.length; x++) {
            buttons[x].classList.remove('btn-outline-dark')
            buttons[x].classList.add('btn-outline-light')
        }

        // Individual Items
        document.getElementById('top').classList.remove('bg-light')
        document.getElementById('top').classList.add('bg-dark')
        document.getElementById('top').classList.add('text-white')
        document.getElementById('top').classList.add('border-bottom')
        document.getElementById('top').classList.add('border-white')

        headers = document.getElementsByClassName('display-4')
        for(x = 0; x<headers.length; x++) {
            headers[x].classList.add('text-white')
        }
        dividers = document.getElementsByClassName('my-4')
        for(x = 0; x<dividers.length; x++) {
            dividers[x].classList.add('border')
            dividers[x].classList.add('border-white')
        }
        tables = document.getElementsByClassName('table')
        for(x = 0; x<tables.length; x++) {
            tables[x].classList.add('text-white')
        }
        dark = true
        document.getElementById('lights').innerHTML = 'Lights On!'
    } else {
        // Start with the body
        document.body.classList.remove("bg-dark")

        // Then the jumbotrons
        jumboList = document.getElementsByClassName('jumbotron')
        for(x = 0; x<jumboList.length; x++) {
            jumboList[x].classList.remove('bg-dark')
            jumboList[x].classList.remove('text-white')
            jumboList[x].classList.remove('border')
            jumboList[x].classList.remove('border-white')
        }

        // The buttons
        buttons = document.getElementsByClassName('btn')
        for(x = 0; x<buttons.length; x++) {
            buttons[x].classList.add('btn-outline-dark')
            buttons[x].classList.remove('btn-outline-light')
        }

        // Individual Items
        document.getElementById('top').classList.add('bg-light')
        document.getElementById('top').classList.remove('bg-dark')
        document.getElementById('top').classList.remove('text-white')
        document.getElementById('top').classList.remove('border-bottom')
        document.getElementById('top').classList.remove('border-white')

        headers = document.getElementsByClassName('display-4')
        for(x = 0; x<headers.length; x++) {
            headers[x].classList.remove('text-white')
        }
        dividers = document.getElementsByClassName('my-4')
        for(x = 0; x<dividers.length; x++) {
            dividers[x].classList.remove('border')
            dividers[x].classList.remove('border-white')
        }
        tables = document.getElementsByClassName('table')
        for(x = 0; x<tables.length; x++) {
            tables[x].classList.remove('text-white')
        }
        dark = false
        document.getElementById('lights').innerHTML = 'Lights Out!'
    }
} 