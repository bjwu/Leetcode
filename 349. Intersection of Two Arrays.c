/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* intersection(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {  
    int shortSize=(nums1Size>nums2Size)?nums2Size:nums1Size;
    int* returnArr=(int*)malloc(shortSize*sizeof(int));
    int cnt=0;
    for (int i=0;i<nums1Size;i++)
      {
        int flag=0;
        for (int ii=0;ii<i;ii++)
        {
            if (nums1[ii]==nums1[i]) 
            {
                flag=1;
                break;
            }
        }
        if (flag==1) continue;
        for (int j=0;j<nums2Size;j++)
            if(*(nums1+i)==*(nums2+j))
            {
                *(returnArr+cnt)=*(nums1+i);
                cnt++;
                break;
            }
      }
    *returnSize=cnt;
    return returnArr;
}