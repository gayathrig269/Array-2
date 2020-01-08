void func_minmax(int arr[],int size)
{
    //Edge case
    if(size==0||size==1||arr==NULL)
    {return 0;}
    else
    {
        int min=arr[0];
        int max=arr[0];
        for(int i=0;i<size;i++)
        {
            if(max<=arr[i])
            max=arr[i];
            else if(min>=arr[i])
            min=arr[i];
        }
    }
}

int main()
{
    int arr[]={9,5,6,10,2,4,9};
    int size =sizeof(arr)/sizeof(arr[0]);
    func_minmax(arr,size);    
}
