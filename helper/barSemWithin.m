% BARSEMWITHIN Plots a bar plot with WITHIN-SUBJECT standard error bars and labels 
% on the current axis. The format of values, names and colors are a cell arrays.
% E.g., if you have a variable with each subjects' score on condition 1 
% (cond1, a vector), and another with each subjects score on condition 2(cond2),
% you'd call it like so:
%
%   barSem({cond1, cond2}, {'condition 1', 'condition 2'})
%
% By default it draws all the bars in gray. You can pass an optional third param.
% that is a cell array of which colors to draw each bar.
%
% TFB
%
function barSemWithin(values, names, colors)
  cla; hold on;
  sems = semWithin(values);
  for i=1:length(values)
    errorbar(i, nanmean(values{i}), sems(i), '.k');
    if nargin > 2
      color = colors{i};
    else
      color = [.5 .5 .5];
    end
    bar(i, nanmean(values{i}), 'FaceColor', color);
  end
  set(gca, 'XTick', 1:length(values), 'XTickLabel', names);
  xlim([.5 length(values)+0.5]);
end