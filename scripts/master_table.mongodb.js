use("bank_analytics_db")
// db.mastertable.findOne()
// total no of transaction based on transaction_type
// db.mastertable.aggregate([
//     {
//         $group:{
//             _id:"$transaction_type",
//             total_transaction:{$sum:1}
//         }
//     }
// ])

// total amount of transaction based on the transaction type

// db.mastertable.aggregate([
//     {
//         $group:{
//             _id:"$transaction_type",
//             total_amount:{$sum:"$amount"}
//         }
//     }
// ])

// total no of transaction based on the payment method
// db.mastertable.aggregate([
//     {
//         $group:{
//             _id:"$payment_method",
//             total_transaction:{$sum:1}
//         }
//     }
// ])

// total amount of transaction based on the payment method
// db.mastertable.aggregate([
//     {
//         $group:{
//             _id:"$payment_method",
//             total_transaction:{$sum:"$amount"}
//         }
//     }
// ])

// total number of transaction based on the branch
// db.mastertable.aggregate([
//     {
//         $group:{
//             _id:"$branch",
//             total_transaction:{$sum:1}
//         }
//     }

// ])

// total amount of transaction based on the basis of branch
db.mastertable.aggregate([
    {
        $group:{
            _id:"$branch",
            total_amount:{$sum:"amount"}
        }
    }
])

// total amount of transaction based on the fraud_flag
db.mastertable.aggregate([
    {
        $group:{
            _id:"$fraud_flag",
            total_amount:{$sum:"$amount"}
        }
    }
])

