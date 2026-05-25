use("bank_analytics_db")

// db.customers.find()

// db.customers.findOne()

// total no of user based on the city

// db.customers.aggregate([
//     {
//         $group:{
//             _id:"$city",
//             totaluser:{$sum:1}

//         }
//     }
// ])

// // total mo of userbased on the state
// db.customers.aggregate([
//     {
//         $group:{
//             _id:"$city",
//             totaluser:{$sum:1}

//         }
//     }
// ])

// total no of customer on the basis of account type
// db.customers.aggregate([
//     {
//         $group:{
//             _id:"$account_type",
//             totaluser:{$sum:1}
//         }
//     }
// ])

// total no of user on the basis of kyc_status
// db.customers.aggregate([
//     {
//         $group:{
//             _id:"$kyc_status",
//             totaluser:{$sum:1}
            
//         }
//     }
// ])

// total no of user on the basis of risk level
db.customers.aggregate([
    {
        $group:{
            _id:"$risk_level",
            totaluser:{$sum:1}
        }
    }
])


