function generate(codes) {
            let code = Math.floor(Math.random() * 100000);
            if(!(code in codes))
                document.getElementById("code").value = code;
            else
                generate();
        }