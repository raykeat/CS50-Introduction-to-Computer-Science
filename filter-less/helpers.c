#include "helpers.h"
#include <math.h>
#include <cs50.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i=0 ; i<height ; i++)
    {
        for (int j=0 ; j<width ; j++)
        {
            int avg = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed)/3.0);
            image[i][j].rgbtBlue = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtRed = avg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i=0 ; i<height ; i++)
    {
        for (int j=0 ; j<width ; j++)
        {
            int b = image[i][j].rgbtBlue;
            int g = image[i][j].rgbtGreen;
            int r = image[i][j].rgbtRed;
            image[i][j].rgbtBlue = round(.272 * r + .534 * g + .131 * b);
            image[i][j].rgbtGreen = round(.349 * r + .686 * g + .168 * b);
            image[i][j].rgbtRed = round(.393 * r + .769 * g + .189 * b);
            if (image[i][j].rgbtBlue>255)
            {
                image[i][j].rgbtBlue=255;
            }
            if (image[i][j].rgbtGreen>255)
            {
                image[i][j].rgbtGreen=255;
            }
            if (image[i][j].rgbtRed>255)
            {
                image[i][j].rgbtRed=255;
            }
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i=0 ; i<height ; i++)
    {
        for (int j=0 ; j<width/2; j++)
        {

            RGBTRIPLE original = image[i][j];
            image[i][j] = image[i][width-j-1];
            image[i][width-j-1] = original;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for (int i=0 ; i<height ; i++)
    {
        for (int j=0 ; j<width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    for (int i=0 ; i<height ; i++)
    {
        for (int j=0 ; j<width; j++)
        {
            int sum_red = 0;
            int sum_blue = 0;
            int sum_green = 0;
            float count = 0.0;
            for (int y=-1 ; y<2 ; y++)
            {
                for (int x=-1 ; x<2 ; x++)
                {
                    if ((i+y)==-1 || (i+y)==height|| (j+x)==-1 || (j+x)==width)
                    {
                        continue;
                    }
                    sum_red += temp[i+y][j+x].rgbtRed;
                    sum_green += temp[i+y][j+x].rgbtGreen;
                    sum_blue += temp[i+y][j+x].rgbtBlue;
                    count++;
                }
            }
            image[i][j].rgbtRed = round(sum_red/(count));
            image[i][j].rgbtGreen = round(sum_green/(count));
            image[i][j].rgbtBlue = round(sum_blue/(count));

        }
    }

}
