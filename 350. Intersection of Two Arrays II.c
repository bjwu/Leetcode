/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* Insert_sort(int *A, int n){
    for(int j=1;j<=n-1;j++)
    {
        int key=A[j];
        int i=j-1;
        while((i>=0)&&(A[i]>key))
        {
            A[i+1]=A[i];
            i--;
        }
        A[i+1]=key;
        
    }
    return A;
};

int* intersect(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    Insert_sort(nums1,nums1Size);
//    for(int i=0;i<nums1Size;i++)
//        printf("%d ",nums1[i]);
    printf("\n");
    Insert_sort(nums2,nums2Size);
//    for(int i=0;i<nums2Size;i++)
//        printf("%d ",nums2[i]);
    int shortSize=(nums1Size>nums2Size)?nums2Size:nums1Size;
    int* returnArr=(int*)malloc(shortSize*sizeof(int));
    int i=0,j=0,cnt=0;
    while((i<nums1Size)&&(j<nums2Size))
    {
        if (nums1[i]==nums2[j])
        {
            *(returnArr+cnt)=nums1[i];
            i++;j++;
            //printf("%d ",*(returnArr+cnt));
            cnt++;
        }
        else if (nums1[i]>nums2[j])
            j++;
        else
            i++;
    }
    *returnSize=cnt;
    return returnArr;
    
}