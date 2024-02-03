if (document.title.includes("Account")) {
	const dateJoined = document.getElementById("date-joined").innerText;
	const passLastChanged = localStorage.getItem("passLastChanged");
	if (passLastChanged == null) {
		localStorage.setItem("passLastChanged", dateJoined);
		document.getElementById("pass-last-changed").innerText = "Updated " + dateJoined;
	} else {
		document.getElementById("pass-last-changed").innerText = "Updated " + passLastChanged;
	}	
}

if (document.title.includes("Change Password") || document.title.includes("Reset Password")) {
	changePassForm = document.getElementsByTagName("form")[0];
	changePassForm.addEventListener("submit", function (event) {
		event.preventDefault();
		let todaysDate = new Date();
		let year = todaysDate.getFullYear();
		let month = todaysDate.getMonth() + 1;
		if (month == 1) {
			month = "Jan";
		} else if (month == 2) {
			month = "Feb";
		} else if (month == 3) {
			month = "Mar";
		} else if (month == 4) {
			month = "Apr";
		} else if (month == 5) {
			month = "May";
		} else if (month == 6) {
			month = "Jun";
		} else if (month == 7) {
			month = "Jul";
		} else if (month == 8) {
			month = "Aug";
		} else if (month == 9) {
			month = "Sep";
		} else if (month == 10) {
			month = "Oct";
		} else if (month == 11) {
			month = "Nov";
		} else {
			month = "Dec";
		}			
		let day = todaysDate.getDate();
		let newDate = `${month} ${String(day)}, ${String(year)}`;
		localStorage.removeItem("passLastChanged");
		localStorage.setItem("passLastChanged", newDate);
		changePassForm.submit();
	});
}	

