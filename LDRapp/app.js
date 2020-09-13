(function(){
	const firebaseConfig = {
	  apiKey: "AIzaSyBB9EcXYuQRk2lnqgQol1GGSGf9S46t1rU",
	  authDomain: "ldr-cube.firebaseapp.com",
	  databaseURL: "https://ldr-cube.firebaseio.com",
	  projectId: "ldr-cube",
	  storageBucket: "ldr-cube.appspot.com",
	  messagingSenderId: "956968125944",
	  appId: "1:956968125944:web:1cf9a3e9d5d5d77e87020d",
	  measurementId: "G-931Z2320ZC"
	};
	firebse.initializeApp(firebaseConfig);
	const preObject = document.getElementbyId('object');
	const dbRefObject = firebase.database().ref().child('object');

	dbRefObject.on('value',snap => console.log(snap.val()));

});