fn sort(arr: &mut [i32]){
    for i in 0..(arr.len()-1){
        if arr[i+1]>=arr[i]{
            let temp = arr[i+1];
            arr[i+1] = arr[i];
            arr[i] = temp;
            println!("{:#?}",arr);
        }
    }
}



fn main(){
    let mut my_array:[i32;8]=[55,5, 2, 17, 11, 45, 1, 23];
    sort(my_array &mut [i32]);
}
