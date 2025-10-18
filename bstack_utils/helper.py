# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import collections
import datetime
import json
import os
import platform
import re
import subprocess
import traceback
import tempfile
import multiprocessing
import threading
import sys
import logging
from math import ceil
from unittest import result
import urllib
from urllib.parse import urlparse
import copy
import zipfile
import git
import requests
from packaging import version
from bstack_utils.config import Config
from bstack_utils.constants import (bstack1l1111111_opy_, bstack1ll1l1l1ll_opy_, bstack11ll11l11_opy_,
                                    bstack11l11ll11l1_opy_, bstack11l1l11llll_opy_, bstack11l11ll11ll_opy_, bstack11l11l1llll_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack11llll1l11_opy_, bstack11ll1l1ll1_opy_
from bstack_utils.proxy import bstack11l11l1l11_opy_, bstack11l1llllll_opy_
from bstack_utils.constants import *
from bstack_utils import bstack11l111l1ll_opy_
from bstack_utils.bstack1l1l1ll1ll_opy_ import bstack11l1l11l1_opy_
from browserstack_sdk._version import __version__
bstack11111l11_opy_ = Config.bstack111l11l1_opy_()
logger = bstack11l111l1ll_opy_.get_logger(__name__, bstack11l111l1ll_opy_.bstack1l1l111ll11_opy_())
def bstack1111l1ll1l1_opy_(config):
    return config[bstack11l111_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫᯭ")]
def bstack1111l11l1ll_opy_(config):
    return config[bstack11l111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ᯮ")]
def bstack1111l1l1ll_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack1111ll111ll_opy_(obj):
    values = []
    bstack111l1l1lll1_opy_ = re.compile(bstack11l111_opy_ (u"ࡶࠧࡤࡃࡖࡕࡗࡓࡒࡥࡔࡂࡉࡢࡠࡩ࠱ࠤࠣᯯ"), re.I)
    for key in obj.keys():
        if bstack111l1l1lll1_opy_.match(key):
            values.append(obj[key])
    return values
def bstack1111l1l1lll_opy_(config):
    tags = []
    tags.extend(bstack1111ll111ll_opy_(os.environ))
    tags.extend(bstack1111ll111ll_opy_(config))
    return tags
def bstack111l1lll111_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack1111l1l1ll1_opy_(bstack111l1l111l1_opy_):
    if not bstack111l1l111l1_opy_:
        return bstack11l111_opy_ (u"ࠬ࠭ᯰ")
    return bstack11l111_opy_ (u"ࠨࡻࡾࠢࠫࡿࢂ࠯ࠢᯱ").format(bstack111l1l111l1_opy_.name, bstack111l1l111l1_opy_.email)
def bstack1111l1llll1_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack1111lll1111_opy_ = repo.common_dir
        info = {
            bstack11l111_opy_ (u"ࠢࡴࡪࡤ᯲ࠦ"): repo.head.commit.hexsha,
            bstack11l111_opy_ (u"ࠣࡵ࡫ࡳࡷࡺ࡟ࡴࡪࡤ᯳ࠦ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack11l111_opy_ (u"ࠤࡥࡶࡦࡴࡣࡩࠤ᯴"): repo.active_branch.name,
            bstack11l111_opy_ (u"ࠥࡸࡦ࡭ࠢ᯵"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack11l111_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡸࡪࡸࠢ᯶"): bstack1111l1l1ll1_opy_(repo.head.commit.committer),
            bstack11l111_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡹ࡫ࡲࡠࡦࡤࡸࡪࠨ᯷"): repo.head.commit.committed_datetime.isoformat(),
            bstack11l111_opy_ (u"ࠨࡡࡶࡶ࡫ࡳࡷࠨ᯸"): bstack1111l1l1ll1_opy_(repo.head.commit.author),
            bstack11l111_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸ࡟ࡥࡣࡷࡩࠧ᯹"): repo.head.commit.authored_datetime.isoformat(),
            bstack11l111_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡠ࡯ࡨࡷࡸࡧࡧࡦࠤ᯺"): repo.head.commit.message,
            bstack11l111_opy_ (u"ࠤࡵࡳࡴࡺࠢ᯻"): repo.git.rev_parse(bstack11l111_opy_ (u"ࠥ࠱࠲ࡹࡨࡰࡹ࠰ࡸࡴࡶ࡬ࡦࡸࡨࡰࠧ᯼")),
            bstack11l111_opy_ (u"ࠦࡨࡵ࡭࡮ࡱࡱࡣ࡬࡯ࡴࡠࡦ࡬ࡶࠧ᯽"): bstack1111lll1111_opy_,
            bstack11l111_opy_ (u"ࠧࡽ࡯ࡳ࡭ࡷࡶࡪ࡫࡟ࡨ࡫ࡷࡣࡩ࡯ࡲࠣ᯾"): subprocess.check_output([bstack11l111_opy_ (u"ࠨࡧࡪࡶࠥ᯿"), bstack11l111_opy_ (u"ࠢࡳࡧࡹ࠱ࡵࡧࡲࡴࡧࠥᰀ"), bstack11l111_opy_ (u"ࠣ࠯࠰࡫࡮ࡺ࠭ࡤࡱࡰࡱࡴࡴ࠭ࡥ࡫ࡵࠦᰁ")]).strip().decode(
                bstack11l111_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᰂ")),
            bstack11l111_opy_ (u"ࠥࡰࡦࡹࡴࡠࡶࡤ࡫ࠧᰃ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack11l111_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡷࡤࡹࡩ࡯ࡥࡨࡣࡱࡧࡳࡵࡡࡷࡥ࡬ࠨᰄ"): repo.git.rev_list(
                bstack11l111_opy_ (u"ࠧࢁࡽ࠯࠰ࡾࢁࠧᰅ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack1111l1l1l1l_opy_ = []
        for remote in remotes:
            bstack1111lllll1l_opy_ = {
                bstack11l111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᰆ"): remote.name,
                bstack11l111_opy_ (u"ࠢࡶࡴ࡯ࠦᰇ"): remote.url,
            }
            bstack1111l1l1l1l_opy_.append(bstack1111lllll1l_opy_)
        bstack1111lll1lll_opy_ = {
            bstack11l111_opy_ (u"ࠣࡰࡤࡱࡪࠨᰈ"): bstack11l111_opy_ (u"ࠤࡪ࡭ࡹࠨᰉ"),
            **info,
            bstack11l111_opy_ (u"ࠥࡶࡪࡳ࡯ࡵࡧࡶࠦᰊ"): bstack1111l1l1l1l_opy_
        }
        bstack1111lll1lll_opy_ = bstack111l1l1llll_opy_(bstack1111lll1lll_opy_)
        return bstack1111lll1lll_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack11l111_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡴࡶࡵ࡭ࡣࡷ࡭ࡳ࡭ࠠࡈ࡫ࡷࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠢᰋ").format(err))
        return {}
def bstack11ll1ll11l1_opy_(bstack111l11lllll_opy_=None):
    bstack11l111_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡍࡥࡵࠢࡪ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡵࡳࡩࡨ࡯ࡦࡪࡥࡤࡰࡱࡿࠠࡧࡱࡵࡱࡦࡺࡴࡦࡦࠣࡪࡴࡸࠠࡂࡋࠣࡷࡪࡲࡥࡤࡶ࡬ࡳࡳࠦࡵࡴࡧࠣࡧࡦࡹࡥࡴࠢࡩࡳࡷࠦࡥࡢࡥ࡫ࠤ࡫ࡵ࡬ࡥࡧࡵࠤ࡮ࡴࠠࡵࡪࡨࠤࡱ࡯ࡳࡵ࠰ࠍࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡧࡱ࡯ࡨࡪࡸࡳࠡࠪ࡯࡭ࡸࡺࠬࠡࡱࡳࡸ࡮ࡵ࡮ࡢ࡮ࠬ࠾ࠥࡒࡩࡴࡶࠣࡳ࡫ࠦࡦࡰ࡮ࡧࡩࡷࠦࡰࡢࡶ࡫ࡷࠥࡺ࡯ࠡࡧࡻࡸࡷࡧࡣࡵࠢࡪ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡨࡵࡳࡲ࠴ࠠࡅࡧࡩࡥࡺࡲࡴࡴࠢࡷࡳࠥࡡ࡯ࡴ࠰ࡪࡩࡹࡩࡷࡥࠪࠬࡡ࠳ࠐࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦ࡬ࡪࡵࡷ࠾ࠥࡒࡩࡴࡶࠣࡳ࡫ࠦࡤࡪࡥࡷࡷ࠱ࠦࡥࡢࡥ࡫ࠤࡨࡵ࡮ࡵࡣ࡬ࡲ࡮ࡴࡧࠡࡩ࡬ࡸࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡧࡱࡵࠤࡦࠦࡦࡰ࡮ࡧࡩࡷ࠴ࠊࠡࠢࠣࠤࠧࠨࠢᰌ")
    if bstack111l11lllll_opy_ == None: # bstack111l11l1l11_opy_ for bstack11lll111111_opy_-repo
        bstack111l11lllll_opy_ = [os.getcwd()]
    results = []
    for folder in bstack111l11lllll_opy_:
        try:
            repo = git.Repo(folder, search_parent_directories=True)
            result = {
                bstack11l111_opy_ (u"ࠨࡰࡳࡋࡧࠦᰍ"): bstack11l111_opy_ (u"ࠢࠣᰎ"),
                bstack11l111_opy_ (u"ࠣࡨ࡬ࡰࡪࡹࡃࡩࡣࡱ࡫ࡪࡪࠢᰏ"): [],
                bstack11l111_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࡵࠥᰐ"): [],
                bstack11l111_opy_ (u"ࠥࡴࡷࡊࡡࡵࡧࠥᰑ"): bstack11l111_opy_ (u"ࠦࠧᰒ"),
                bstack11l111_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡒ࡫ࡳࡴࡣࡪࡩࡸࠨᰓ"): [],
                bstack11l111_opy_ (u"ࠨࡰࡳࡖ࡬ࡸࡱ࡫ࠢᰔ"): bstack11l111_opy_ (u"ࠢࠣᰕ"),
                bstack11l111_opy_ (u"ࠣࡲࡵࡈࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠣᰖ"): bstack11l111_opy_ (u"ࠤࠥᰗ"),
                bstack11l111_opy_ (u"ࠥࡴࡷࡘࡡࡸࡆ࡬ࡪ࡫ࠨᰘ"): bstack11l111_opy_ (u"ࠦࠧᰙ")
            }
            bstack111l11l11l1_opy_ = repo.active_branch.name
            bstack1111ll111l1_opy_ = repo.head.commit
            result[bstack11l111_opy_ (u"ࠧࡶࡲࡊࡦࠥᰚ")] = bstack1111ll111l1_opy_.hexsha
            bstack111l1l1l1ll_opy_ = _111l111l111_opy_(repo)
            logger.debug(bstack11l111_opy_ (u"ࠨࡂࡢࡵࡨࠤࡧࡸࡡ࡯ࡥ࡫ࠤ࡫ࡵࡲࠡࡥࡲࡱࡵࡧࡲࡪࡵࡲࡲ࠿ࠦࠢᰛ") + str(bstack111l1l1l1ll_opy_) + bstack11l111_opy_ (u"ࠢࠣᰜ"))
            if bstack111l1l1l1ll_opy_:
                try:
                    bstack111l1ll11ll_opy_ = repo.git.diff(bstack11l111_opy_ (u"ࠣ࠯࠰ࡲࡦࡳࡥ࠮ࡱࡱࡰࡾࠨᰝ"), bstack11l1ll1l_opy_ (u"ࠤࡾࡦࡦࡹࡥࡠࡤࡵࡥࡳࡩࡨࡾ࠰࠱࠲ࢀࡩࡵࡳࡴࡨࡲࡹࡥࡢࡳࡣࡱࡧ࡭ࢃࠢᰞ")).split(bstack11l111_opy_ (u"ࠪࡠࡳ࠭ᰟ"))
                    logger.debug(bstack11l111_opy_ (u"ࠦࡈ࡮ࡡ࡯ࡩࡨࡨࠥ࡬ࡩ࡭ࡧࡶࠤࡧ࡫ࡴࡸࡧࡨࡲࠥࢁࡢࡢࡵࡨࡣࡧࡸࡡ࡯ࡥ࡫ࢁࠥࡧ࡮ࡥࠢࡾࡧࡺࡸࡲࡦࡰࡷࡣࡧࡸࡡ࡯ࡥ࡫ࢁ࠿ࠦࠢᰠ") + str(bstack111l1ll11ll_opy_) + bstack11l111_opy_ (u"ࠧࠨᰡ"))
                    result[bstack11l111_opy_ (u"ࠨࡦࡪ࡮ࡨࡷࡈ࡮ࡡ࡯ࡩࡨࡨࠧᰢ")] = [f.strip() for f in bstack111l1ll11ll_opy_ if f.strip()]
                    commits = list(repo.iter_commits(bstack11l1ll1l_opy_ (u"ࠢࡼࡤࡤࡷࡪࡥࡢࡳࡣࡱࡧ࡭ࢃ࠮࠯ࡽࡦࡹࡷࡸࡥ࡯ࡶࡢࡦࡷࡧ࡮ࡤࡪࢀࠦᰣ")))
                except Exception:
                    logger.debug(bstack11l111_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡬࡫ࡴࠡࡥ࡫ࡥࡳ࡭ࡥࡥࠢࡩ࡭ࡱ࡫ࡳࠡࡨࡵࡳࡲࠦࡢࡳࡣࡱࡧ࡭ࠦࡣࡰ࡯ࡳࡥࡷ࡯ࡳࡰࡰ࠱ࠤࡋࡧ࡬࡭࡫ࡱ࡫ࠥࡨࡡࡤ࡭ࠣࡸࡴࠦࡲࡦࡥࡨࡲࡹࠦࡣࡰ࡯ࡰ࡭ࡹࡹ࠮ࠣᰤ"))
                    commits = list(repo.iter_commits(max_count=10))
                    if commits:
                        result[bstack11l111_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡳࡄࡪࡤࡲ࡬࡫ࡤࠣᰥ")] = _1111l1ll11l_opy_(commits[:5])
            else:
                commits = list(repo.iter_commits(max_count=10))
                if commits:
                    result[bstack11l111_opy_ (u"ࠥࡪ࡮ࡲࡥࡴࡅ࡫ࡥࡳ࡭ࡥࡥࠤᰦ")] = _1111l1ll11l_opy_(commits[:5])
            bstack1111l11lll1_opy_ = set()
            bstack1111l1lllll_opy_ = []
            for commit in commits:
                logger.debug(bstack11l111_opy_ (u"ࠦࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡥࡲࡱࡲ࡯ࡴ࠻ࠢࠥᰧ") + str(commit.message) + bstack11l111_opy_ (u"ࠧࠨᰨ"))
                bstack111l11ll1l1_opy_ = commit.author.name if commit.author else bstack11l111_opy_ (u"ࠨࡕ࡯࡭ࡱࡳࡼࡴࠢᰩ")
                bstack1111l11lll1_opy_.add(bstack111l11ll1l1_opy_)
                bstack1111l1lllll_opy_.append({
                    bstack11l111_opy_ (u"ࠢ࡮ࡧࡶࡷࡦ࡭ࡥࠣᰪ"): commit.message.strip(),
                    bstack11l111_opy_ (u"ࠣࡷࡶࡩࡷࠨᰫ"): bstack111l11ll1l1_opy_
                })
            result[bstack11l111_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࡵࠥᰬ")] = list(bstack1111l11lll1_opy_)
            result[bstack11l111_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡐࡩࡸࡹࡡࡨࡧࡶࠦᰭ")] = bstack1111l1lllll_opy_
            result[bstack11l111_opy_ (u"ࠦࡵࡸࡄࡢࡶࡨࠦᰮ")] = bstack1111ll111l1_opy_.committed_datetime.strftime(bstack11l111_opy_ (u"࡙ࠧࠫ࠮ࠧࡰ࠱ࠪࡪࠢᰯ"))
            if (not result[bstack11l111_opy_ (u"ࠨࡰࡳࡖ࡬ࡸࡱ࡫ࠢᰰ")] or result[bstack11l111_opy_ (u"ࠢࡱࡴࡗ࡭ࡹࡲࡥࠣᰱ")].strip() == bstack11l111_opy_ (u"ࠣࠤᰲ")) and bstack1111ll111l1_opy_.message:
                bstack1111lll1l11_opy_ = bstack1111ll111l1_opy_.message.strip().splitlines()
                result[bstack11l111_opy_ (u"ࠤࡳࡶ࡙࡯ࡴ࡭ࡧࠥᰳ")] = bstack1111lll1l11_opy_[0] if bstack1111lll1l11_opy_ else bstack11l111_opy_ (u"ࠥࠦᰴ")
                if len(bstack1111lll1l11_opy_) > 2:
                    result[bstack11l111_opy_ (u"ࠦࡵࡸࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠦᰵ")] = bstack11l111_opy_ (u"ࠬࡢ࡮ࠨᰶ").join(bstack1111lll1l11_opy_[2:]).strip()
            results.append(result)
        except Exception as err:
            logger.error(bstack11l111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡯ࡱࡷ࡯ࡥࡹ࡯࡮ࡨࠢࡊ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡨࡲࡶࠥࡇࡉࠡࡵࡨࡰࡪࡩࡴࡪࡱࡱࠤ࠭࡬࡯࡭ࡦࡨࡶ࠿ࠦࡻࡧࡱ࡯ࡨࡪࡸࡽࠪ࠼᰷ࠣࠦ") + str(err) + bstack11l111_opy_ (u"ࠢࠣ᰸"))
    filtered_results = [
        result
        for result in results
        if _111l11ll1ll_opy_(result)
    ]
    return filtered_results
def _111l11ll1ll_opy_(result):
    bstack11l111_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡊࡨࡰࡵ࡫ࡲࠡࡶࡲࠤࡨ࡮ࡥࡤ࡭ࠣ࡭࡫ࠦࡡࠡࡩ࡬ࡸࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡳࡧࡶࡹࡱࡺࠠࡪࡵࠣࡺࡦࡲࡩࡥࠢࠫࡲࡴࡴ࠭ࡦ࡯ࡳࡸࡾࠦࡦࡪ࡮ࡨࡷࡈ࡮ࡡ࡯ࡩࡨࡨࠥࡧ࡮ࡥࠢࡤࡹࡹ࡮࡯ࡳࡵࠬ࠲ࠏࠦࠠࠡࠢࠥࠦࠧ᰹")
    return (
        isinstance(result.get(bstack11l111_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡳࡄࡪࡤࡲ࡬࡫ࡤࠣ᰺"), None), list)
        and len(result[bstack11l111_opy_ (u"ࠥࡪ࡮ࡲࡥࡴࡅ࡫ࡥࡳ࡭ࡥࡥࠤ᰻")]) > 0
        and isinstance(result.get(bstack11l111_opy_ (u"ࠦࡦࡻࡴࡩࡱࡵࡷࠧ᰼"), None), list)
        and len(result[bstack11l111_opy_ (u"ࠧࡧࡵࡵࡪࡲࡶࡸࠨ᰽")]) > 0
    )
def _111l111l111_opy_(repo):
    bstack11l111_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡔࡳࡻࠣࡸࡴࠦࡤࡦࡶࡨࡶࡲ࡯࡮ࡦࠢࡷ࡬ࡪࠦࡢࡢࡵࡨࠤࡧࡸࡡ࡯ࡥ࡫ࠤ࡫ࡵࡲࠡࡶ࡫ࡩࠥ࡭ࡩࡷࡧࡱࠤࡷ࡫ࡰࡰࠢࡺ࡭ࡹ࡮࡯ࡶࡶࠣ࡬ࡦࡸࡤࡤࡱࡧࡩࡩࠦ࡮ࡢ࡯ࡨࡷࠥࡧ࡮ࡥࠢࡺࡳࡷࡱࠠࡸ࡫ࡷ࡬ࠥࡧ࡬࡭࡙ࠢࡇࡘࠦࡰࡳࡱࡹ࡭ࡩ࡫ࡲࡴ࠰ࠍࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳࠡࡶ࡫ࡩࠥࡪࡥࡧࡣࡸࡰࡹࠦࡢࡳࡣࡱࡧ࡭ࠦࡩࡧࠢࡳࡳࡸࡹࡩࡣ࡮ࡨ࠰ࠥ࡫࡬ࡴࡧࠣࡒࡴࡴࡥ࠯ࠌࠣࠤࠥࠦࠢࠣࠤ᰾")
    try:
        try:
            origin = repo.remotes.origin
            bstack111l1l11lll_opy_ = origin.refs[bstack11l111_opy_ (u"ࠧࡉࡇࡄࡈࠬ᰿")]
            target = bstack111l1l11lll_opy_.reference.name
            if target.startswith(bstack11l111_opy_ (u"ࠨࡱࡵ࡭࡬࡯࡮࠰ࠩ᱀")):
                return target
        except Exception:
            pass
        if repo.remotes and repo.remotes.origin.refs:
            for ref in repo.remotes.origin.refs:
                if ref.name.startswith(bstack11l111_opy_ (u"ࠩࡲࡶ࡮࡭ࡩ࡯࠱ࠪ᱁")):
                    return ref.name
        if repo.heads:
            return repo.heads[0].name
    except Exception:
        pass
    return None
def _1111l1ll11l_opy_(commits):
    bstack11l111_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡋࡪࡺࠠ࡭࡫ࡶࡸࠥࡵࡦࠡࡥ࡫ࡥࡳ࡭ࡥࡥࠢࡩ࡭ࡱ࡫ࡳࠡࡨࡵࡳࡲࠦࡡࠡ࡮࡬ࡷࡹࠦ࡯ࡧࠢࡦࡳࡲࡳࡩࡵࡵ࠱ࠎࠥࠦࠠࠡࠤࠥࠦ᱂")
    bstack111l1ll11ll_opy_ = set()
    try:
        for commit in commits:
            if commit.parents:
                for parent in commit.parents:
                    diff = commit.diff(parent)
                    for bstack1111llllll1_opy_ in diff:
                        if bstack1111llllll1_opy_.a_path:
                            bstack111l1ll11ll_opy_.add(bstack1111llllll1_opy_.a_path)
                        if bstack1111llllll1_opy_.b_path:
                            bstack111l1ll11ll_opy_.add(bstack1111llllll1_opy_.b_path)
    except Exception:
        pass
    return list(bstack111l1ll11ll_opy_)
def bstack111l1l1llll_opy_(bstack1111lll1lll_opy_):
    bstack111l11l1ll1_opy_ = bstack111l1111l11_opy_(bstack1111lll1lll_opy_)
    if bstack111l11l1ll1_opy_ and bstack111l11l1ll1_opy_ > bstack11l11ll11l1_opy_:
        bstack1111ll1llll_opy_ = bstack111l11l1ll1_opy_ - bstack11l11ll11l1_opy_
        bstack1111ll1l1ll_opy_ = bstack1111lllll11_opy_(bstack1111lll1lll_opy_[bstack11l111_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡣࡲ࡫ࡳࡴࡣࡪࡩࠧ᱃")], bstack1111ll1llll_opy_)
        bstack1111lll1lll_opy_[bstack11l111_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡤࡳࡥࡴࡵࡤ࡫ࡪࠨ᱄")] = bstack1111ll1l1ll_opy_
        logger.info(bstack11l111_opy_ (u"ࠨࡔࡩࡧࠣࡧࡴࡳ࡭ࡪࡶࠣ࡬ࡦࡹࠠࡣࡧࡨࡲࠥࡺࡲࡶࡰࡦࡥࡹ࡫ࡤ࠯ࠢࡖ࡭ࡿ࡫ࠠࡰࡨࠣࡧࡴࡳ࡭ࡪࡶࠣࡥ࡫ࡺࡥࡳࠢࡷࡶࡺࡴࡣࡢࡶ࡬ࡳࡳࠦࡩࡴࠢࡾࢁࠥࡑࡂࠣ᱅")
                    .format(bstack111l1111l11_opy_(bstack1111lll1lll_opy_) / 1024))
    return bstack1111lll1lll_opy_
def bstack111l1111l11_opy_(json_data):
    try:
        if json_data:
            bstack1111l1l1111_opy_ = json.dumps(json_data)
            bstack1111ll1ll1l_opy_ = sys.getsizeof(bstack1111l1l1111_opy_)
            return bstack1111ll1ll1l_opy_
    except Exception as e:
        logger.debug(bstack11l111_opy_ (u"ࠢࡔࡱࡰࡩࡹ࡮ࡩ࡯ࡩࠣࡻࡪࡴࡴࠡࡹࡵࡳࡳ࡭ࠠࡸࡪ࡬ࡰࡪࠦࡣࡢ࡮ࡦࡹࡱࡧࡴࡪࡰࡪࠤࡸ࡯ࡺࡦࠢࡲࡪࠥࡐࡓࡐࡐࠣࡳࡧࡰࡥࡤࡶ࠽ࠤࢀࢃࠢ᱆").format(e))
    return -1
def bstack1111lllll11_opy_(field, bstack1111l11l111_opy_):
    try:
        bstack111l111l1l1_opy_ = len(bytes(bstack11l1l11llll_opy_, bstack11l111_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧ᱇")))
        bstack111l1l1ll11_opy_ = bytes(field, bstack11l111_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨ᱈"))
        bstack1111ll11lll_opy_ = len(bstack111l1l1ll11_opy_)
        bstack1111lll1l1l_opy_ = ceil(bstack1111ll11lll_opy_ - bstack1111l11l111_opy_ - bstack111l111l1l1_opy_)
        if bstack1111lll1l1l_opy_ > 0:
            bstack1111ll1111l_opy_ = bstack111l1l1ll11_opy_[:bstack1111lll1l1l_opy_].decode(bstack11l111_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩ᱉"), errors=bstack11l111_opy_ (u"ࠫ࡮࡭࡮ࡰࡴࡨࠫ᱊")) + bstack11l1l11llll_opy_
            return bstack1111ll1111l_opy_
    except Exception as e:
        logger.debug(bstack11l111_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡸࡷࡻ࡮ࡤࡣࡷ࡭ࡳ࡭ࠠࡧ࡫ࡨࡰࡩ࠲ࠠ࡯ࡱࡷ࡬࡮ࡴࡧࠡࡹࡤࡷࠥࡺࡲࡶࡰࡦࡥࡹ࡫ࡤࠡࡪࡨࡶࡪࡀࠠࡼࡿࠥ᱋").format(e))
    return field
def bstack1l1111111l_opy_():
    env = os.environ
    if (bstack11l111_opy_ (u"ࠨࡊࡆࡐࡎࡍࡓ࡙࡟ࡖࡔࡏࠦ᱌") in env and len(env[bstack11l111_opy_ (u"ࠢࡋࡇࡑࡏࡎࡔࡓࡠࡗࡕࡐࠧᱍ")]) > 0) or (
            bstack11l111_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡋࡓࡒࡋࠢᱎ") in env and len(env[bstack11l111_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢࡌࡔࡓࡅࠣᱏ")]) > 0):
        return {
            bstack11l111_opy_ (u"ࠥࡲࡦࡳࡥࠣ᱐"): bstack11l111_opy_ (u"ࠦࡏ࡫࡮࡬࡫ࡱࡷࠧ᱑"),
            bstack11l111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣ᱒"): env.get(bstack11l111_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤ᱓")),
            bstack11l111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᱔"): env.get(bstack11l111_opy_ (u"ࠣࡌࡒࡆࡤࡔࡁࡎࡇࠥ᱕")),
            bstack11l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᱖"): env.get(bstack11l111_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤ᱗"))
        }
    if env.get(bstack11l111_opy_ (u"ࠦࡈࡏࠢ᱘")) == bstack11l111_opy_ (u"ࠧࡺࡲࡶࡧࠥ᱙") and bstack1l1lll1ll1_opy_(env.get(bstack11l111_opy_ (u"ࠨࡃࡊࡔࡆࡐࡊࡉࡉࠣᱚ"))):
        return {
            bstack11l111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᱛ"): bstack11l111_opy_ (u"ࠣࡅ࡬ࡶࡨࡲࡥࡄࡋࠥᱜ"),
            bstack11l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᱝ"): env.get(bstack11l111_opy_ (u"ࠥࡇࡎࡘࡃࡍࡇࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᱞ")),
            bstack11l111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᱟ"): env.get(bstack11l111_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡤࡐࡏࡃࠤᱠ")),
            bstack11l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᱡ"): env.get(bstack11l111_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࠥᱢ"))
        }
    if env.get(bstack11l111_opy_ (u"ࠣࡅࡌࠦᱣ")) == bstack11l111_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᱤ") and bstack1l1lll1ll1_opy_(env.get(bstack11l111_opy_ (u"ࠥࡘࡗࡇࡖࡊࡕࠥᱥ"))):
        return {
            bstack11l111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᱦ"): bstack11l111_opy_ (u"࡚ࠧࡲࡢࡸ࡬ࡷࠥࡉࡉࠣᱧ"),
            bstack11l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᱨ"): env.get(bstack11l111_opy_ (u"ࠢࡕࡔࡄ࡚ࡎ࡙࡟ࡃࡗࡌࡐࡉࡥࡗࡆࡄࡢ࡙ࡗࡒࠢᱩ")),
            bstack11l111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᱪ"): env.get(bstack11l111_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᱫ")),
            bstack11l111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᱬ"): env.get(bstack11l111_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᱭ"))
        }
    if env.get(bstack11l111_opy_ (u"ࠧࡉࡉࠣᱮ")) == bstack11l111_opy_ (u"ࠨࡴࡳࡷࡨࠦᱯ") and env.get(bstack11l111_opy_ (u"ࠢࡄࡋࡢࡒࡆࡓࡅࠣᱰ")) == bstack11l111_opy_ (u"ࠣࡥࡲࡨࡪࡹࡨࡪࡲࠥᱱ"):
        return {
            bstack11l111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᱲ"): bstack11l111_opy_ (u"ࠥࡇࡴࡪࡥࡴࡪ࡬ࡴࠧᱳ"),
            bstack11l111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᱴ"): None,
            bstack11l111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᱵ"): None,
            bstack11l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᱶ"): None
        }
    if env.get(bstack11l111_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡆࡗࡇࡎࡄࡊࠥᱷ")) and env.get(bstack11l111_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡈࡕࡍࡎࡋࡗࠦᱸ")):
        return {
            bstack11l111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᱹ"): bstack11l111_opy_ (u"ࠥࡆ࡮ࡺࡢࡶࡥ࡮ࡩࡹࠨᱺ"),
            bstack11l111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᱻ"): env.get(bstack11l111_opy_ (u"ࠧࡈࡉࡕࡄࡘࡇࡐࡋࡔࡠࡉࡌࡘࡤࡎࡔࡕࡒࡢࡓࡗࡏࡇࡊࡐࠥᱼ")),
            bstack11l111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᱽ"): None,
            bstack11l111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᱾"): env.get(bstack11l111_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥ᱿"))
        }
    if env.get(bstack11l111_opy_ (u"ࠤࡆࡍࠧᲀ")) == bstack11l111_opy_ (u"ࠥࡸࡷࡻࡥࠣᲁ") and bstack1l1lll1ll1_opy_(env.get(bstack11l111_opy_ (u"ࠦࡉࡘࡏࡏࡇࠥᲂ"))):
        return {
            bstack11l111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᲃ"): bstack11l111_opy_ (u"ࠨࡄࡳࡱࡱࡩࠧᲄ"),
            bstack11l111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᲅ"): env.get(bstack11l111_opy_ (u"ࠣࡆࡕࡓࡓࡋ࡟ࡃࡗࡌࡐࡉࡥࡌࡊࡐࡎࠦᲆ")),
            bstack11l111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᲇ"): None,
            bstack11l111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᲈ"): env.get(bstack11l111_opy_ (u"ࠦࡉࡘࡏࡏࡇࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᲉ"))
        }
    if env.get(bstack11l111_opy_ (u"ࠧࡉࡉࠣᲊ")) == bstack11l111_opy_ (u"ࠨࡴࡳࡷࡨࠦ᲋") and bstack1l1lll1ll1_opy_(env.get(bstack11l111_opy_ (u"ࠢࡔࡇࡐࡅࡕࡎࡏࡓࡇࠥ᲌"))):
        return {
            bstack11l111_opy_ (u"ࠣࡰࡤࡱࡪࠨ᲍"): bstack11l111_opy_ (u"ࠤࡖࡩࡲࡧࡰࡩࡱࡵࡩࠧ᲎"),
            bstack11l111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᲏"): env.get(bstack11l111_opy_ (u"ࠦࡘࡋࡍࡂࡒࡋࡓࡗࡋ࡟ࡐࡔࡊࡅࡓࡏ࡚ࡂࡖࡌࡓࡓࡥࡕࡓࡎࠥᲐ")),
            bstack11l111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᲑ"): env.get(bstack11l111_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᲒ")),
            bstack11l111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᲓ"): env.get(bstack11l111_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࡣࡏࡕࡂࡠࡋࡇࠦᲔ"))
        }
    if env.get(bstack11l111_opy_ (u"ࠤࡆࡍࠧᲕ")) == bstack11l111_opy_ (u"ࠥࡸࡷࡻࡥࠣᲖ") and bstack1l1lll1ll1_opy_(env.get(bstack11l111_opy_ (u"ࠦࡌࡏࡔࡍࡃࡅࡣࡈࡏࠢᲗ"))):
        return {
            bstack11l111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᲘ"): bstack11l111_opy_ (u"ࠨࡇࡪࡶࡏࡥࡧࠨᲙ"),
            bstack11l111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᲚ"): env.get(bstack11l111_opy_ (u"ࠣࡅࡌࡣࡏࡕࡂࡠࡗࡕࡐࠧᲛ")),
            bstack11l111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᲜ"): env.get(bstack11l111_opy_ (u"ࠥࡇࡎࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣᲝ")),
            bstack11l111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᲞ"): env.get(bstack11l111_opy_ (u"ࠧࡉࡉࡠࡌࡒࡆࡤࡏࡄࠣᲟ"))
        }
    if env.get(bstack11l111_opy_ (u"ࠨࡃࡊࠤᲠ")) == bstack11l111_opy_ (u"ࠢࡵࡴࡸࡩࠧᲡ") and bstack1l1lll1ll1_opy_(env.get(bstack11l111_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࠦᲢ"))):
        return {
            bstack11l111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᲣ"): bstack11l111_opy_ (u"ࠥࡆࡺ࡯࡬ࡥ࡭࡬ࡸࡪࠨᲤ"),
            bstack11l111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᲥ"): env.get(bstack11l111_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦᲦ")),
            bstack11l111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᲧ"): env.get(bstack11l111_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡐࡆࡈࡅࡍࠤᲨ")) or env.get(bstack11l111_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡎࡂࡏࡈࠦᲩ")),
            bstack11l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᲪ"): env.get(bstack11l111_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᲫ"))
        }
    if bstack1l1lll1ll1_opy_(env.get(bstack11l111_opy_ (u"࡙ࠦࡌ࡟ࡃࡗࡌࡐࡉࠨᲬ"))):
        return {
            bstack11l111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᲭ"): bstack11l111_opy_ (u"ࠨࡖࡪࡵࡸࡥࡱࠦࡓࡵࡷࡧ࡭ࡴࠦࡔࡦࡣࡰࠤࡘ࡫ࡲࡷ࡫ࡦࡩࡸࠨᲮ"),
            bstack11l111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᲯ"): bstack11l111_opy_ (u"ࠣࡽࢀࡿࢂࠨᲰ").format(env.get(bstack11l111_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡆࡐࡗࡑࡈࡆ࡚ࡉࡐࡐࡖࡉࡗ࡜ࡅࡓࡗࡕࡍࠬᲱ")), env.get(bstack11l111_opy_ (u"ࠪࡗ࡞࡙ࡔࡆࡏࡢࡘࡊࡇࡍࡑࡔࡒࡎࡊࡉࡔࡊࡆࠪᲲ"))),
            bstack11l111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᲳ"): env.get(bstack11l111_opy_ (u"࡙࡙ࠧࡔࡖࡈࡑࡤࡊࡅࡇࡋࡑࡍ࡙ࡏࡏࡏࡋࡇࠦᲴ")),
            bstack11l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᲵ"): env.get(bstack11l111_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠢᲶ"))
        }
    if bstack1l1lll1ll1_opy_(env.get(bstack11l111_opy_ (u"ࠣࡃࡓࡔ࡛ࡋ࡙ࡐࡔࠥᲷ"))):
        return {
            bstack11l111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᲸ"): bstack11l111_opy_ (u"ࠥࡅࡵࡶࡶࡦࡻࡲࡶࠧᲹ"),
            bstack11l111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᲺ"): bstack11l111_opy_ (u"ࠧࢁࡽ࠰ࡲࡵࡳ࡯࡫ࡣࡵ࠱ࡾࢁ࠴ࢁࡽ࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀࠦ᲻").format(env.get(bstack11l111_opy_ (u"࠭ࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡗࡕࡐࠬ᲼")), env.get(bstack11l111_opy_ (u"ࠧࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡄࡇࡈࡕࡕࡏࡖࡢࡒࡆࡓࡅࠨᲽ")), env.get(bstack11l111_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡔࡗࡕࡊࡆࡅࡗࡣࡘࡒࡕࡈࠩᲾ")), env.get(bstack11l111_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭Ჿ"))),
            bstack11l111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ᳀"): env.get(bstack11l111_opy_ (u"ࠦࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣ᳁")),
            bstack11l111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ᳂"): env.get(bstack11l111_opy_ (u"ࠨࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢ᳃"))
        }
    if env.get(bstack11l111_opy_ (u"ࠢࡂ࡜ࡘࡖࡊࡥࡈࡕࡖࡓࡣ࡚࡙ࡅࡓࡡࡄࡋࡊࡔࡔࠣ᳄")) and env.get(bstack11l111_opy_ (u"ࠣࡖࡉࡣࡇ࡛ࡉࡍࡆࠥ᳅")):
        return {
            bstack11l111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᳆"): bstack11l111_opy_ (u"ࠥࡅࡿࡻࡲࡦࠢࡆࡍࠧ᳇"),
            bstack11l111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ᳈"): bstack11l111_opy_ (u"ࠧࢁࡽࡼࡿ࠲ࡣࡧࡻࡩ࡭ࡦ࠲ࡶࡪࡹࡵ࡭ࡶࡶࡃࡧࡻࡩ࡭ࡦࡌࡨࡂࢁࡽࠣ᳉").format(env.get(bstack11l111_opy_ (u"࠭ࡓ࡚ࡕࡗࡉࡒࡥࡔࡆࡃࡐࡊࡔ࡛ࡎࡅࡃࡗࡍࡔࡔࡓࡆࡔ࡙ࡉࡗ࡛ࡒࡊࠩ᳊")), env.get(bstack11l111_opy_ (u"ࠧࡔ࡛ࡖࡘࡊࡓ࡟ࡕࡇࡄࡑࡕࡘࡏࡋࡇࡆࡘࠬ᳋")), env.get(bstack11l111_opy_ (u"ࠨࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡏࡄࠨ᳌"))),
            bstack11l111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ᳍"): env.get(bstack11l111_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠥ᳎")),
            bstack11l111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ᳏"): env.get(bstack11l111_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠧ᳐"))
        }
    if any([env.get(bstack11l111_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦ᳑")), env.get(bstack11l111_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡖࡊ࡙ࡏࡍࡘࡈࡈࡤ࡙ࡏࡖࡔࡆࡉࡤ࡜ࡅࡓࡕࡌࡓࡓࠨ᳒")), env.get(bstack11l111_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡘࡕࡕࡓࡅࡈࡣ࡛ࡋࡒࡔࡋࡒࡒࠧ᳓"))]):
        return {
            bstack11l111_opy_ (u"ࠤࡱࡥࡲ࡫᳔ࠢ"): bstack11l111_opy_ (u"ࠥࡅ࡜࡙ࠠࡄࡱࡧࡩࡇࡻࡩ࡭ࡦ᳕ࠥ"),
            bstack11l111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲ᳖ࠢ"): env.get(bstack11l111_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡒࡘࡆࡑࡏࡃࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏ᳗ࠦ")),
            bstack11l111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥ᳘ࠣ"): env.get(bstack11l111_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈ᳙ࠧ")),
            bstack11l111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ᳚"): env.get(bstack11l111_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢ᳛"))
        }
    if env.get(bstack11l111_opy_ (u"ࠥࡦࡦࡳࡢࡰࡱࡢࡦࡺ࡯࡬ࡥࡐࡸࡱࡧ࡫ࡲ᳜ࠣ")):
        return {
            bstack11l111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᳝"): bstack11l111_opy_ (u"ࠧࡈࡡ࡮ࡤࡲࡳ᳞ࠧ"),
            bstack11l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᳟"): env.get(bstack11l111_opy_ (u"ࠢࡣࡣࡰࡦࡴࡵ࡟ࡣࡷ࡬ࡰࡩࡘࡥࡴࡷ࡯ࡸࡸ࡛ࡲ࡭ࠤ᳠")),
            bstack11l111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᳡"): env.get(bstack11l111_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡶ࡬ࡴࡸࡴࡋࡱࡥࡒࡦࡳࡥ᳢ࠣ")),
            bstack11l111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᳣"): env.get(bstack11l111_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡧࡻࡩ࡭ࡦࡑࡹࡲࡨࡥࡳࠤ᳤"))
        }
    if env.get(bstack11l111_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࠨ᳥")) or env.get(bstack11l111_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡎࡃࡌࡒࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡔࡖࡄࡖ࡙ࡋࡄ᳦ࠣ")):
        return {
            bstack11l111_opy_ (u"ࠢ࡯ࡣࡰࡩ᳧ࠧ"): bstack11l111_opy_ (u"࡙ࠣࡨࡶࡨࡱࡥࡳࠤ᳨"),
            bstack11l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᳩ"): env.get(bstack11l111_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢᳪ")),
            bstack11l111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᳫ"): bstack11l111_opy_ (u"ࠧࡓࡡࡪࡰࠣࡔ࡮ࡶࡥ࡭࡫ࡱࡩࠧᳬ") if env.get(bstack11l111_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡎࡃࡌࡒࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡔࡖࡄࡖ࡙ࡋࡄ᳭ࠣ")) else None,
            bstack11l111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᳮ"): env.get(bstack11l111_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡊࡍ࡙ࡥࡃࡐࡏࡐࡍ࡙ࠨᳯ"))
        }
    if any([env.get(bstack11l111_opy_ (u"ࠤࡊࡇࡕࡥࡐࡓࡑࡍࡉࡈ࡚ࠢᳰ")), env.get(bstack11l111_opy_ (u"ࠥࡋࡈࡒࡏࡖࡆࡢࡔࡗࡕࡊࡆࡅࡗࠦᳱ")), env.get(bstack11l111_opy_ (u"ࠦࡌࡕࡏࡈࡎࡈࡣࡈࡒࡏࡖࡆࡢࡔࡗࡕࡊࡆࡅࡗࠦᳲ"))]):
        return {
            bstack11l111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᳳ"): bstack11l111_opy_ (u"ࠨࡇࡰࡱࡪࡰࡪࠦࡃ࡭ࡱࡸࡨࠧ᳴"),
            bstack11l111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᳵ"): None,
            bstack11l111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᳶ"): env.get(bstack11l111_opy_ (u"ࠤࡓࡖࡔࡐࡅࡄࡖࡢࡍࡉࠨ᳷")),
            bstack11l111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᳸"): env.get(bstack11l111_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡍࡉࠨ᳹"))
        }
    if env.get(bstack11l111_opy_ (u"࡙ࠧࡈࡊࡒࡓࡅࡇࡒࡅࠣᳺ")):
        return {
            bstack11l111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ᳻"): bstack11l111_opy_ (u"ࠢࡔࡪ࡬ࡴࡵࡧࡢ࡭ࡧࠥ᳼"),
            bstack11l111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ᳽"): env.get(bstack11l111_opy_ (u"ࠤࡖࡌࡎࡖࡐࡂࡄࡏࡉࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣ᳾")),
            bstack11l111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ᳿"): bstack11l111_opy_ (u"ࠦࡏࡵࡢࠡࠥࡾࢁࠧᴀ").format(env.get(bstack11l111_opy_ (u"࡙ࠬࡈࡊࡒࡓࡅࡇࡒࡅࡠࡌࡒࡆࡤࡏࡄࠨᴁ"))) if env.get(bstack11l111_opy_ (u"ࠨࡓࡉࡋࡓࡔࡆࡈࡌࡆࡡࡍࡓࡇࡥࡉࡅࠤᴂ")) else None,
            bstack11l111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᴃ"): env.get(bstack11l111_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᴄ"))
        }
    if bstack1l1lll1ll1_opy_(env.get(bstack11l111_opy_ (u"ࠤࡑࡉ࡙ࡒࡉࡇ࡛ࠥᴅ"))):
        return {
            bstack11l111_opy_ (u"ࠥࡲࡦࡳࡥࠣᴆ"): bstack11l111_opy_ (u"ࠦࡓ࡫ࡴ࡭࡫ࡩࡽࠧᴇ"),
            bstack11l111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᴈ"): env.get(bstack11l111_opy_ (u"ࠨࡄࡆࡒࡏࡓ࡞ࡥࡕࡓࡎࠥᴉ")),
            bstack11l111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᴊ"): env.get(bstack11l111_opy_ (u"ࠣࡕࡌࡘࡊࡥࡎࡂࡏࡈࠦᴋ")),
            bstack11l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᴌ"): env.get(bstack11l111_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᴍ"))
        }
    if bstack1l1lll1ll1_opy_(env.get(bstack11l111_opy_ (u"ࠦࡌࡏࡔࡉࡗࡅࡣࡆࡉࡔࡊࡑࡑࡗࠧᴎ"))):
        return {
            bstack11l111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᴏ"): bstack11l111_opy_ (u"ࠨࡇࡪࡶࡋࡹࡧࠦࡁࡤࡶ࡬ࡳࡳࡹࠢᴐ"),
            bstack11l111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᴑ"): bstack11l111_opy_ (u"ࠣࡽࢀ࠳ࢀࢃ࠯ࡢࡥࡷ࡭ࡴࡴࡳ࠰ࡴࡸࡲࡸ࠵ࡻࡾࠤᴒ").format(env.get(bstack11l111_opy_ (u"ࠩࡊࡍ࡙ࡎࡕࡃࡡࡖࡉࡗ࡜ࡅࡓࡡࡘࡖࡑ࠭ᴓ")), env.get(bstack11l111_opy_ (u"ࠪࡋࡎ࡚ࡈࡖࡄࡢࡖࡊࡖࡏࡔࡋࡗࡓࡗ࡟ࠧᴔ")), env.get(bstack11l111_opy_ (u"ࠫࡌࡏࡔࡉࡗࡅࡣࡗ࡛ࡎࡠࡋࡇࠫᴕ"))),
            bstack11l111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᴖ"): env.get(bstack11l111_opy_ (u"ࠨࡇࡊࡖࡋ࡙ࡇࡥࡗࡐࡔࡎࡊࡑࡕࡗࠣᴗ")),
            bstack11l111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᴘ"): env.get(bstack11l111_opy_ (u"ࠣࡉࡌࡘࡍ࡛ࡂࡠࡔࡘࡒࡤࡏࡄࠣᴙ"))
        }
    if env.get(bstack11l111_opy_ (u"ࠤࡆࡍࠧᴚ")) == bstack11l111_opy_ (u"ࠥࡸࡷࡻࡥࠣᴛ") and env.get(bstack11l111_opy_ (u"࡛ࠦࡋࡒࡄࡇࡏࠦᴜ")) == bstack11l111_opy_ (u"ࠧ࠷ࠢᴝ"):
        return {
            bstack11l111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᴞ"): bstack11l111_opy_ (u"ࠢࡗࡧࡵࡧࡪࡲࠢᴟ"),
            bstack11l111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᴠ"): bstack11l111_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࡾࢁࠧᴡ").format(env.get(bstack11l111_opy_ (u"࡚ࠪࡊࡘࡃࡆࡎࡢ࡙ࡗࡒࠧᴢ"))),
            bstack11l111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᴣ"): None,
            bstack11l111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᴤ"): None,
        }
    if env.get(bstack11l111_opy_ (u"ࠨࡔࡆࡃࡐࡇࡎ࡚࡙ࡠࡘࡈࡖࡘࡏࡏࡏࠤᴥ")):
        return {
            bstack11l111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᴦ"): bstack11l111_opy_ (u"ࠣࡖࡨࡥࡲࡩࡩࡵࡻࠥᴧ"),
            bstack11l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᴨ"): None,
            bstack11l111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᴩ"): env.get(bstack11l111_opy_ (u"࡙ࠦࡋࡁࡎࡅࡌࡘ࡞ࡥࡐࡓࡑࡍࡉࡈ࡚࡟ࡏࡃࡐࡉࠧᴪ")),
            bstack11l111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᴫ"): env.get(bstack11l111_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᴬ"))
        }
    if any([env.get(bstack11l111_opy_ (u"ࠢࡄࡑࡑࡇࡔ࡛ࡒࡔࡇࠥᴭ")), env.get(bstack11l111_opy_ (u"ࠣࡅࡒࡒࡈࡕࡕࡓࡕࡈࡣ࡚ࡘࡌࠣᴮ")), env.get(bstack11l111_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠢᴯ")), env.get(bstack11l111_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࡥࡔࡆࡃࡐࠦᴰ"))]):
        return {
            bstack11l111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᴱ"): bstack11l111_opy_ (u"ࠧࡉ࡯࡯ࡥࡲࡹࡷࡹࡥࠣᴲ"),
            bstack11l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᴳ"): None,
            bstack11l111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᴴ"): env.get(bstack11l111_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᴵ")) or None,
            bstack11l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᴶ"): env.get(bstack11l111_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᴷ"), 0)
        }
    if env.get(bstack11l111_opy_ (u"ࠦࡌࡕ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᴸ")):
        return {
            bstack11l111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᴹ"): bstack11l111_opy_ (u"ࠨࡇࡰࡅࡇࠦᴺ"),
            bstack11l111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᴻ"): None,
            bstack11l111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᴼ"): env.get(bstack11l111_opy_ (u"ࠤࡊࡓࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢᴽ")),
            bstack11l111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᴾ"): env.get(bstack11l111_opy_ (u"ࠦࡌࡕ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡆࡓ࡚ࡔࡔࡆࡔࠥᴿ"))
        }
    if env.get(bstack11l111_opy_ (u"ࠧࡉࡆࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᵀ")):
        return {
            bstack11l111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᵁ"): bstack11l111_opy_ (u"ࠢࡄࡱࡧࡩࡋࡸࡥࡴࡪࠥᵂ"),
            bstack11l111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᵃ"): env.get(bstack11l111_opy_ (u"ࠤࡆࡊࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᵄ")),
            bstack11l111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᵅ"): env.get(bstack11l111_opy_ (u"ࠦࡈࡌ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡑࡅࡒࡋࠢᵆ")),
            bstack11l111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᵇ"): env.get(bstack11l111_opy_ (u"ࠨࡃࡇࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦᵈ"))
        }
    return {bstack11l111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᵉ"): None}
def get_host_info():
    return {
        bstack11l111_opy_ (u"ࠣࡪࡲࡷࡹࡴࡡ࡮ࡧࠥᵊ"): platform.node(),
        bstack11l111_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࠦᵋ"): platform.system(),
        bstack11l111_opy_ (u"ࠥࡸࡾࡶࡥࠣᵌ"): platform.machine(),
        bstack11l111_opy_ (u"ࠦࡻ࡫ࡲࡴ࡫ࡲࡲࠧᵍ"): platform.version(),
        bstack11l111_opy_ (u"ࠧࡧࡲࡤࡪࠥᵎ"): platform.architecture()[0]
    }
def bstack11l1ll1111_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack111l1ll111l_opy_():
    if bstack11111l11_opy_.get_property(bstack11l111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧᵏ")):
        return bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᵐ")
    return bstack11l111_opy_ (u"ࠨࡷࡱ࡯ࡳࡵࡷ࡯ࡡࡪࡶ࡮ࡪࠧᵑ")
def bstack1111l11ll11_opy_(driver):
    info = {
        bstack11l111_opy_ (u"ࠩࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨᵒ"): driver.capabilities,
        bstack11l111_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠧᵓ"): driver.session_id,
        bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬᵔ"): driver.capabilities.get(bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪᵕ"), None),
        bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᵖ"): driver.capabilities.get(bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᵗ"), None),
        bstack11l111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪᵘ"): driver.capabilities.get(bstack11l111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠨᵙ"), None),
        bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᵚ"):driver.capabilities.get(bstack11l111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᵛ"), None),
    }
    if bstack111l1ll111l_opy_() == bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᵜ"):
        if bstack1l11l1111l_opy_():
            info[bstack11l111_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺࠧᵝ")] = bstack11l111_opy_ (u"ࠧࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᵞ")
        elif driver.capabilities.get(bstack11l111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᵟ"), {}).get(bstack11l111_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭ᵠ"), False):
            info[bstack11l111_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࠫᵡ")] = bstack11l111_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨᵢ")
        else:
            info[bstack11l111_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭ᵣ")] = bstack11l111_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨᵤ")
    return info
def bstack1l11l1111l_opy_():
    if bstack11111l11_opy_.get_property(bstack11l111_opy_ (u"ࠧࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᵥ")):
        return True
    if bstack1l1lll1ll1_opy_(os.environ.get(bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩᵦ"), None)):
        return True
    return False
def bstack111l1llll1_opy_(bstack1111l11l11l_opy_, url, data, config):
    headers = config.get(bstack11l111_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪᵧ"), None)
    proxies = bstack11l11l1l11_opy_(config, url)
    auth = config.get(bstack11l111_opy_ (u"ࠪࡥࡺࡺࡨࠨᵨ"), None)
    response = requests.request(
            bstack1111l11l11l_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack11l11l111l_opy_(bstack111111llll_opy_, size):
    bstack1111l1l1l_opy_ = []
    while len(bstack111111llll_opy_) > size:
        bstack1l11l1l1l_opy_ = bstack111111llll_opy_[:size]
        bstack1111l1l1l_opy_.append(bstack1l11l1l1l_opy_)
        bstack111111llll_opy_ = bstack111111llll_opy_[size:]
    bstack1111l1l1l_opy_.append(bstack111111llll_opy_)
    return bstack1111l1l1l_opy_
def bstack1111ll11l11_opy_(message, bstack111l1111l1l_opy_=False):
    os.write(1, bytes(message, bstack11l111_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᵩ")))
    os.write(1, bytes(bstack11l111_opy_ (u"ࠬࡢ࡮ࠨᵪ"), bstack11l111_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᵫ")))
    if bstack111l1111l1l_opy_:
        with open(bstack11l111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠭ࡰ࠳࠴ࡽ࠲࠭ᵬ") + os.environ[bstack11l111_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧᵭ")] + bstack11l111_opy_ (u"ࠩ࠱ࡰࡴ࡭ࠧᵮ"), bstack11l111_opy_ (u"ࠪࡥࠬᵯ")) as f:
            f.write(message + bstack11l111_opy_ (u"ࠫࡡࡴࠧᵰ"))
def bstack1lll1l11ll1_opy_():
    return os.environ[bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨᵱ")].lower() == bstack11l111_opy_ (u"࠭ࡴࡳࡷࡨࠫᵲ")
def bstack11lllll1_opy_():
    return bstack1l1l111l_opy_().replace(tzinfo=None).isoformat() + bstack11l111_opy_ (u"࡛ࠧࠩᵳ")
def bstack1111l11llll_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack11l111_opy_ (u"ࠨ࡜ࠪᵴ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack11l111_opy_ (u"ࠩ࡝ࠫᵵ")))).total_seconds() * 1000
def bstack111l11ll111_opy_(timestamp):
    return bstack1111lll111l_opy_(timestamp).isoformat() + bstack11l111_opy_ (u"ࠪ࡞ࠬᵶ")
def bstack1111l11l1l1_opy_(bstack1111lll11ll_opy_):
    date_format = bstack11l111_opy_ (u"ࠫࠪ࡟ࠥ࡮ࠧࡧࠤࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠴ࠥࡧࠩᵷ")
    bstack1111ll1ll11_opy_ = datetime.datetime.strptime(bstack1111lll11ll_opy_, date_format)
    return bstack1111ll1ll11_opy_.isoformat() + bstack11l111_opy_ (u"ࠬࡠࠧᵸ")
def bstack1111l1lll1l_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack11l111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᵹ")
    else:
        return bstack11l111_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᵺ")
def bstack1l1lll1ll1_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack11l111_opy_ (u"ࠨࡶࡵࡹࡪ࠭ᵻ")
def bstack111l1ll1l1l_opy_(val):
    return val.__str__().lower() == bstack11l111_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨᵼ")
def error_handler(bstack1111llll111_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack1111llll111_opy_ as e:
                print(bstack11l111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࢀࢃࠠ࠮ࡀࠣࡿࢂࡀࠠࡼࡿࠥᵽ").format(func.__name__, bstack1111llll111_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack1111ll11111_opy_(bstack1111llll11l_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack1111llll11l_opy_(cls, *args, **kwargs)
            except bstack1111llll111_opy_ as e:
                print(bstack11l111_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥࢁࡽࠡ࠯ࡁࠤࢀࢃ࠺ࠡࡽࢀࠦᵾ").format(bstack1111llll11l_opy_.__name__, bstack1111llll111_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack1111ll11111_opy_
    else:
        return decorator
def bstack11l11l1ll_opy_(bstack1llll1l1l_opy_):
    if os.getenv(bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨᵿ")) is not None:
        return bstack1l1lll1ll1_opy_(os.getenv(bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩᶀ")))
    if bstack11l111_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᶁ") in bstack1llll1l1l_opy_ and bstack111l1ll1l1l_opy_(bstack1llll1l1l_opy_[bstack11l111_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᶂ")]):
        return False
    if bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᶃ") in bstack1llll1l1l_opy_ and bstack111l1ll1l1l_opy_(bstack1llll1l1l_opy_[bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᶄ")]):
        return False
    return True
def bstack1ll11111ll_opy_():
    try:
        from pytest_bdd import reporting
        bstack1111l1ll1ll_opy_ = os.environ.get(bstack11l111_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢ࡙ࡘࡋࡒࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠦᶅ"), None)
        return bstack1111l1ll1ll_opy_ is None or bstack1111l1ll1ll_opy_ == bstack11l111_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠤᶆ")
    except Exception as e:
        return False
def bstack1111llll1_opy_(hub_url, CONFIG):
    if bstack1ll1l11ll_opy_() <= version.parse(bstack11l111_opy_ (u"࠭࠳࠯࠳࠶࠲࠵࠭ᶇ")):
        if hub_url:
            return bstack11l111_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣᶈ") + hub_url + bstack11l111_opy_ (u"ࠣ࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠧᶉ")
        return bstack1ll1l1l1ll_opy_
    if hub_url:
        return bstack11l111_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦᶊ") + hub_url + bstack11l111_opy_ (u"ࠥ࠳ࡼࡪ࠯ࡩࡷࡥࠦᶋ")
    return bstack11ll11l11_opy_
def bstack111l111111l_opy_():
    return isinstance(os.getenv(bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔ࡞࡚ࡅࡔࡖࡢࡔࡑ࡛ࡇࡊࡐࠪᶌ")), str)
def bstack1ll1llllll_opy_(url):
    return urlparse(url).hostname
def bstack11ll1ll111_opy_(hostname):
    for bstack1l11l1l111_opy_ in bstack1l1111111_opy_:
        regex = re.compile(bstack1l11l1l111_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11ll1111l1l_opy_(bstack111l11l1111_opy_, file_name, logger):
    bstack11l1l1ll11_opy_ = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠬࢄࠧᶍ")), bstack111l11l1111_opy_)
    try:
        if not os.path.exists(bstack11l1l1ll11_opy_):
            os.makedirs(bstack11l1l1ll11_opy_)
        file_path = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"࠭ࡾࠨᶎ")), bstack111l11l1111_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack11l111_opy_ (u"ࠧࡸࠩᶏ")):
                pass
            with open(file_path, bstack11l111_opy_ (u"ࠣࡹ࠮ࠦᶐ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack11llll1l11_opy_.format(str(e)))
def bstack11ll1111ll1_opy_(file_name, key, value, logger):
    file_path = bstack11ll1111l1l_opy_(bstack11l111_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩᶑ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1lllll1l1l_opy_ = json.load(open(file_path, bstack11l111_opy_ (u"ࠪࡶࡧ࠭ᶒ")))
        else:
            bstack1lllll1l1l_opy_ = {}
        bstack1lllll1l1l_opy_[key] = value
        with open(file_path, bstack11l111_opy_ (u"ࠦࡼ࠱ࠢᶓ")) as outfile:
            json.dump(bstack1lllll1l1l_opy_, outfile)
def bstack11l1lll1l1_opy_(file_name, logger):
    file_path = bstack11ll1111l1l_opy_(bstack11l111_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᶔ"), file_name, logger)
    bstack1lllll1l1l_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack11l111_opy_ (u"࠭ࡲࠨᶕ")) as bstack1lllll1111_opy_:
            bstack1lllll1l1l_opy_ = json.load(bstack1lllll1111_opy_)
    return bstack1lllll1l1l_opy_
def bstack1ll11111l1_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack11l111_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡧࡩࡱ࡫ࡴࡪࡰࡪࠤ࡫࡯࡬ࡦ࠼ࠣࠫᶖ") + file_path + bstack11l111_opy_ (u"ࠨࠢࠪᶗ") + str(e))
def bstack1ll1l11ll_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack11l111_opy_ (u"ࠤ࠿ࡒࡔ࡚ࡓࡆࡖࡁࠦᶘ")
def bstack11ll1111ll_opy_(config):
    if bstack11l111_opy_ (u"ࠪ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᶙ") in config:
        del (config[bstack11l111_opy_ (u"ࠫ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᶚ")])
        return False
    if bstack1ll1l11ll_opy_() < version.parse(bstack11l111_opy_ (u"ࠬ࠹࠮࠵࠰࠳ࠫᶛ")):
        return False
    if bstack1ll1l11ll_opy_() >= version.parse(bstack11l111_opy_ (u"࠭࠴࠯࠳࠱࠹ࠬᶜ")):
        return True
    if bstack11l111_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧᶝ") in config and config[bstack11l111_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨᶞ")] is False:
        return False
    else:
        return True
def bstack1lll111ll1_opy_(args_list, bstack111l1lll1l1_opy_):
    index = -1
    for value in bstack111l1lll1l1_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
def bstack1111ll1lll1_opy_(a, b):
  for k, v in b.items():
    if isinstance(v, dict) and k in a and isinstance(a[k], dict):
        bstack1111ll1lll1_opy_(a[k], v)
    else:
        a[k] = v
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1l1ll11l_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1l1ll11l_opy_ = bstack1l1ll11l_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack11l111_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᶟ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack11l111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᶠ"), exception=exception)
    def bstack1111111lll_opy_(self):
        if self.result != bstack11l111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᶡ"):
            return None
        if isinstance(self.exception_type, str) and bstack11l111_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࠣᶢ") in self.exception_type:
            return bstack11l111_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࡇࡵࡶࡴࡸࠢᶣ")
        return bstack11l111_opy_ (u"ࠢࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠣᶤ")
    def bstack111l1ll1lll_opy_(self):
        if self.result != bstack11l111_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᶥ"):
            return None
        if self.bstack1l1ll11l_opy_:
            return self.bstack1l1ll11l_opy_
        return bstack1111ll1l111_opy_(self.exception)
def bstack1111ll1l111_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack111l1ll1l11_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1l1lll11_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack111l1l111_opy_(config, logger):
    try:
        import playwright
        bstack1111l1ll111_opy_ = playwright.__file__
        bstack111l11111l1_opy_ = os.path.split(bstack1111l1ll111_opy_)
        bstack1111llll1ll_opy_ = bstack111l11111l1_opy_[0] + bstack11l111_opy_ (u"ࠩ࠲ࡨࡷ࡯ࡶࡦࡴ࠲ࡴࡦࡩ࡫ࡢࡩࡨ࠳ࡱ࡯ࡢ࠰ࡥ࡯࡭࠴ࡩ࡬ࡪ࠰࡭ࡷࠬᶦ")
        os.environ[bstack11l111_opy_ (u"ࠪࡋࡑࡕࡂࡂࡎࡢࡅࡌࡋࡎࡕࡡࡋࡘ࡙ࡖ࡟ࡑࡔࡒ࡜࡞࠭ᶧ")] = bstack11l1llllll_opy_(config)
        with open(bstack1111llll1ll_opy_, bstack11l111_opy_ (u"ࠫࡷ࠭ᶨ")) as f:
            file_content = f.read()
            bstack1111l1l11ll_opy_ = bstack11l111_opy_ (u"ࠬ࡭࡬ࡰࡤࡤࡰ࠲ࡧࡧࡦࡰࡷࠫᶩ")
            bstack111l1l1l1l1_opy_ = file_content.find(bstack1111l1l11ll_opy_)
            if bstack111l1l1l1l1_opy_ == -1:
              process = subprocess.Popen(bstack11l111_opy_ (u"ࠨ࡮ࡱ࡯ࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤ࡬ࡲ࡯ࡣࡣ࡯࠱ࡦ࡭ࡥ࡯ࡶࠥᶪ"), shell=True, cwd=bstack111l11111l1_opy_[0])
              process.wait()
              bstack111l1l11111_opy_ = bstack11l111_opy_ (u"ࠧࠣࡷࡶࡩࠥࡹࡴࡳ࡫ࡦࡸࠧࡁࠧᶫ")
              bstack111l111l11l_opy_ = bstack11l111_opy_ (u"ࠣࠤࠥࠤࡡࠨࡵࡴࡧࠣࡷࡹࡸࡩࡤࡶ࡟ࠦࡀࠦࡣࡰࡰࡶࡸࠥࢁࠠࡣࡱࡲࡸࡸࡺࡲࡢࡲࠣࢁࠥࡃࠠࡳࡧࡴࡹ࡮ࡸࡥࠩࠩࡪࡰࡴࡨࡡ࡭࠯ࡤ࡫ࡪࡴࡴࠨࠫ࠾ࠤ࡮࡬ࠠࠩࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡨࡲࡻ࠴ࡇࡍࡑࡅࡅࡑࡥࡁࡈࡇࡑࡘࡤࡎࡔࡕࡒࡢࡔࡗࡕࡘ࡚ࠫࠣࡦࡴࡵࡴࡴࡶࡵࡥࡵ࠮ࠩ࠼ࠢࠥࠦࠧᶬ")
              bstack111l111llll_opy_ = file_content.replace(bstack111l1l11111_opy_, bstack111l111l11l_opy_)
              with open(bstack1111llll1ll_opy_, bstack11l111_opy_ (u"ࠩࡺࠫᶭ")) as f:
                f.write(bstack111l111llll_opy_)
    except Exception as e:
        logger.error(bstack11ll1l1ll1_opy_.format(str(e)))
def bstack1l111l11l1_opy_():
  try:
    bstack111l11l1l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l111_opy_ (u"ࠪࡳࡵࡺࡩ࡮ࡣ࡯ࡣ࡭ࡻࡢࡠࡷࡵࡰ࠳ࡰࡳࡰࡰࠪᶮ"))
    bstack1111llll1l1_opy_ = []
    if os.path.exists(bstack111l11l1l1l_opy_):
      with open(bstack111l11l1l1l_opy_) as f:
        bstack1111llll1l1_opy_ = json.load(f)
      os.remove(bstack111l11l1l1l_opy_)
    return bstack1111llll1l1_opy_
  except:
    pass
  return []
def bstack111ll111ll_opy_(bstack1l111ll111_opy_):
  try:
    bstack1111llll1l1_opy_ = []
    bstack111l11l1l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l111_opy_ (u"ࠫࡴࡶࡴࡪ࡯ࡤࡰࡤ࡮ࡵࡣࡡࡸࡶࡱ࠴ࡪࡴࡱࡱࠫᶯ"))
    if os.path.exists(bstack111l11l1l1l_opy_):
      with open(bstack111l11l1l1l_opy_) as f:
        bstack1111llll1l1_opy_ = json.load(f)
    bstack1111llll1l1_opy_.append(bstack1l111ll111_opy_)
    with open(bstack111l11l1l1l_opy_, bstack11l111_opy_ (u"ࠬࡽࠧᶰ")) as f:
        json.dump(bstack1111llll1l1_opy_, f)
  except:
    pass
def bstack111l11l11l_opy_(logger, bstack111l1ll1ll1_opy_ = False):
  try:
    test_name = os.environ.get(bstack11l111_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙ࡥࡔࡆࡕࡗࡣࡓࡇࡍࡆࠩᶱ"), bstack11l111_opy_ (u"ࠧࠨᶲ"))
    if test_name == bstack11l111_opy_ (u"ࠨࠩᶳ"):
        test_name = threading.current_thread().__dict__.get(bstack11l111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡄࡧࡨࡤࡺࡥࡴࡶࡢࡲࡦࡳࡥࠨᶴ"), bstack11l111_opy_ (u"ࠪࠫᶵ"))
    bstack1111ll1l1l1_opy_ = bstack11l111_opy_ (u"ࠫ࠱ࠦࠧᶶ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack111l1ll1ll1_opy_:
        bstack1l1lll111l_opy_ = os.environ.get(bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬᶷ"), bstack11l111_opy_ (u"࠭࠰ࠨᶸ"))
        bstack1l1lll1111_opy_ = {bstack11l111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᶹ"): test_name, bstack11l111_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᶺ"): bstack1111ll1l1l1_opy_, bstack11l111_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨᶻ"): bstack1l1lll111l_opy_}
        bstack1111l111lll_opy_ = []
        bstack111l1l11l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡴࡵࡶ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩᶼ"))
        if os.path.exists(bstack111l1l11l1l_opy_):
            with open(bstack111l1l11l1l_opy_) as f:
                bstack1111l111lll_opy_ = json.load(f)
        bstack1111l111lll_opy_.append(bstack1l1lll1111_opy_)
        with open(bstack111l1l11l1l_opy_, bstack11l111_opy_ (u"ࠫࡼ࠭ᶽ")) as f:
            json.dump(bstack1111l111lll_opy_, f)
    else:
        bstack1l1lll1111_opy_ = {bstack11l111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᶾ"): test_name, bstack11l111_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬᶿ"): bstack1111ll1l1l1_opy_, bstack11l111_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭᷀"): str(multiprocessing.current_process().name)}
        if bstack11l111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸࠬ᷁") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack1l1lll1111_opy_)
  except Exception as e:
      logger.warn(bstack11l111_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡵࡿࡴࡦࡵࡷࠤ࡫ࡻ࡮࡯ࡧ࡯ࠤࡩࡧࡴࡢ࠼ࠣࡿࢂࠨ᷂").format(e))
def bstack11l1llll11_opy_(error_message, test_name, index, logger):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l111_opy_ (u"ࠪࡪ࡮ࡲࡥ࡭ࡱࡦ࡯ࠥࡴ࡯ࡵࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩ࠱ࠦࡵࡴ࡫ࡱ࡫ࠥࡨࡡࡴ࡫ࡦࠤ࡫࡯࡬ࡦࠢࡲࡴࡪࡸࡡࡵ࡫ࡲࡲࡸ࠭᷃"))
    try:
      bstack111l111l1ll_opy_ = []
      bstack1l1lll1111_opy_ = {bstack11l111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ᷄"): test_name, bstack11l111_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ᷅"): error_message, bstack11l111_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬ᷆"): index}
      bstack1111l1l11l1_opy_ = os.path.join(tempfile.gettempdir(), bstack11l111_opy_ (u"ࠧࡳࡱࡥࡳࡹࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨ᷇"))
      if os.path.exists(bstack1111l1l11l1_opy_):
          with open(bstack1111l1l11l1_opy_) as f:
              bstack111l111l1ll_opy_ = json.load(f)
      bstack111l111l1ll_opy_.append(bstack1l1lll1111_opy_)
      with open(bstack1111l1l11l1_opy_, bstack11l111_opy_ (u"ࠨࡹࠪ᷈")) as f:
          json.dump(bstack111l111l1ll_opy_, f)
    except Exception as e:
      logger.warn(bstack11l111_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡷࡵࡢࡰࡶࠣࡪࡺࡴ࡮ࡦ࡮ࠣࡨࡦࡺࡡ࠻ࠢࡾࢁࠧ᷉").format(e))
    return
  bstack111l111l1ll_opy_ = []
  bstack1l1lll1111_opy_ = {bstack11l111_opy_ (u"ࠪࡲࡦࡳࡥࠨ᷊"): test_name, bstack11l111_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪ᷋"): error_message, bstack11l111_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫ᷌"): index}
  bstack1111l1l11l1_opy_ = os.path.join(tempfile.gettempdir(), bstack11l111_opy_ (u"࠭ࡲࡰࡤࡲࡸࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧ᷍"))
  lock_file = bstack1111l1l11l1_opy_ + bstack11l111_opy_ (u"ࠧ࠯࡮ࡲࡧࡰ᷎࠭")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack1111l1l11l1_opy_):
          with open(bstack1111l1l11l1_opy_, bstack11l111_opy_ (u"ࠨࡴ᷏ࠪ")) as f:
              content = f.read().strip()
              if content:
                  bstack111l111l1ll_opy_ = json.load(open(bstack1111l1l11l1_opy_))
      bstack111l111l1ll_opy_.append(bstack1l1lll1111_opy_)
      with open(bstack1111l1l11l1_opy_, bstack11l111_opy_ (u"ࠩࡺ᷐ࠫ")) as f:
          json.dump(bstack111l111l1ll_opy_, f)
  except Exception as e:
    logger.warn(bstack11l111_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡱࡵࡩࠥࡸ࡯ࡣࡱࡷࠤ࡫ࡻ࡮࡯ࡧ࡯ࠤࡩࡧࡴࡢࠢࡺ࡭ࡹ࡮ࠠࡧ࡫࡯ࡩࠥࡲ࡯ࡤ࡭࡬ࡲ࡬ࡀࠠࡼࡿࠥ᷑").format(e))
def bstack11l11ll1ll_opy_(bstack1l11lll11l_opy_, name, logger):
  try:
    bstack1l1lll1111_opy_ = {bstack11l111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ᷒"): name, bstack11l111_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᷓ"): bstack1l11lll11l_opy_, bstack11l111_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬᷔ"): str(threading.current_thread()._name)}
    return bstack1l1lll1111_opy_
  except Exception as e:
    logger.warn(bstack11l111_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡵࡲࡦࠢࡥࡩ࡭ࡧࡶࡦࠢࡩࡹࡳࡴࡥ࡭ࠢࡧࡥࡹࡧ࠺ࠡࡽࢀࠦᷕ").format(e))
  return
def bstack111l1l11ll1_opy_():
    return platform.system() == bstack11l111_opy_ (u"ࠨ࡙࡬ࡲࡩࡵࡷࡴࠩᷖ")
def bstack11lll11l1l_opy_(bstack1111l1lll11_opy_, config, logger):
    bstack111l11l1lll_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack1111l1lll11_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack11l111_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡩ࡭ࡶࡨࡶࠥࡩ࡯࡯ࡨ࡬࡫ࠥࡱࡥࡺࡵࠣࡦࡾࠦࡲࡦࡩࡨࡼࠥࡳࡡࡵࡥ࡫࠾ࠥࢁࡽࠣᷗ").format(e))
    return bstack111l11l1lll_opy_
def bstack11l1ll11l1l_opy_(bstack111l1l1l11l_opy_, bstack111l111lll1_opy_):
    bstack111l111ll11_opy_ = version.parse(bstack111l1l1l11l_opy_)
    bstack111l1ll11l1_opy_ = version.parse(bstack111l111lll1_opy_)
    if bstack111l111ll11_opy_ > bstack111l1ll11l1_opy_:
        return 1
    elif bstack111l111ll11_opy_ < bstack111l1ll11l1_opy_:
        return -1
    else:
        return 0
def bstack1l1l111l_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack1111lll111l_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack111l1l1111l_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack11l1l1l1l_opy_(options, framework, config, bstack111ll111l1_opy_={}):
    if options is None:
        return
    if getattr(options, bstack11l111_opy_ (u"ࠪ࡫ࡪࡺࠧᷘ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack11l1111lll_opy_ = caps.get(bstack11l111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᷙ"))
    bstack111l11lll11_opy_ = True
    bstack11l11l1l1l_opy_ = os.environ[bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪᷚ")]
    bstack1l1111l1lll_opy_ = config.get(bstack11l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᷛ"), False)
    if bstack1l1111l1lll_opy_:
        bstack1l1l11l1lll_opy_ = config.get(bstack11l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᷜ"), {})
        bstack1l1l11l1lll_opy_[bstack11l111_opy_ (u"ࠨࡣࡸࡸ࡭࡚࡯࡬ࡧࡱࠫᷝ")] = os.getenv(bstack11l111_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧᷞ"))
        bstack111l11l111l_opy_ = json.loads(os.getenv(bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫᷟ"), bstack11l111_opy_ (u"ࠫࢀࢃࠧᷠ"))).get(bstack11l111_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᷡ"))
    if bstack111l1ll1l1l_opy_(caps.get(bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡻࡳࡦ࡙࠶ࡇࠬᷢ"))) or bstack111l1ll1l1l_opy_(caps.get(bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡵࡴࡧࡢࡻ࠸ࡩࠧᷣ"))):
        bstack111l11lll11_opy_ = False
    if bstack11ll1111ll_opy_({bstack11l111_opy_ (u"ࠣࡷࡶࡩ࡜࠹ࡃࠣᷤ"): bstack111l11lll11_opy_}):
        bstack11l1111lll_opy_ = bstack11l1111lll_opy_ or {}
        bstack11l1111lll_opy_[bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫᷥ")] = bstack111l1l1111l_opy_(framework)
        bstack11l1111lll_opy_[bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᷦ")] = bstack1lll1l11ll1_opy_()
        bstack11l1111lll_opy_[bstack11l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧᷧ")] = bstack11l11l1l1l_opy_
        bstack11l1111lll_opy_[bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧᷨ")] = bstack111ll111l1_opy_
        if bstack1l1111l1lll_opy_:
            bstack11l1111lll_opy_[bstack11l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᷩ")] = bstack1l1111l1lll_opy_
            bstack11l1111lll_opy_[bstack11l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᷪ")] = bstack1l1l11l1lll_opy_
            bstack11l1111lll_opy_[bstack11l111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨᷫ")][bstack11l111_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᷬ")] = bstack111l11l111l_opy_
        if getattr(options, bstack11l111_opy_ (u"ࠪࡷࡪࡺ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶࡼࠫᷭ"), None):
            options.set_capability(bstack11l111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᷮ"), bstack11l1111lll_opy_)
        else:
            options[bstack11l111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᷯ")] = bstack11l1111lll_opy_
    else:
        if getattr(options, bstack11l111_opy_ (u"࠭ࡳࡦࡶࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹࡿࠧᷰ"), None):
            options.set_capability(bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨᷱ"), bstack111l1l1111l_opy_(framework))
            options.set_capability(bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᷲ"), bstack1lll1l11ll1_opy_())
            options.set_capability(bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫᷳ"), bstack11l11l1l1l_opy_)
            options.set_capability(bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫᷴ"), bstack111ll111l1_opy_)
            if bstack1l1111l1lll_opy_:
                options.set_capability(bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ᷵"), bstack1l1111l1lll_opy_)
                options.set_capability(bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ᷶"), bstack1l1l11l1lll_opy_)
                options.set_capability(bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷ࠳ࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ᷷࠭"), bstack111l11l111l_opy_)
        else:
            options[bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨ᷸")] = bstack111l1l1111l_opy_(framework)
            options[bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯᷹ࠩ")] = bstack1lll1l11ll1_opy_()
            options[bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧ᷺ࠫ")] = bstack11l11l1l1l_opy_
            options[bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫ᷻")] = bstack111ll111l1_opy_
            if bstack1l1111l1lll_opy_:
                options[bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ᷼")] = bstack1l1111l1lll_opy_
                options[bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶ᷽ࠫ")] = bstack1l1l11l1lll_opy_
                options[bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ᷾")][bstack11l111_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ᷿")] = bstack111l11l111l_opy_
    return options
def bstack111l1111111_opy_(ws_endpoint, framework):
    bstack111ll111l1_opy_ = bstack11111l11_opy_.get_property(bstack11l111_opy_ (u"ࠣࡒࡏࡅ࡞࡝ࡒࡊࡉࡋࡘࡤࡖࡒࡐࡆࡘࡇ࡙ࡥࡍࡂࡒࠥḀ"))
    if ws_endpoint and len(ws_endpoint.split(bstack11l111_opy_ (u"ࠩࡦࡥࡵࡹ࠽ࠨḁ"))) > 1:
        ws_url = ws_endpoint.split(bstack11l111_opy_ (u"ࠪࡧࡦࡶࡳ࠾ࠩḂ"))[0]
        if bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧḃ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack111l1l111ll_opy_ = json.loads(urllib.parse.unquote(ws_endpoint.split(bstack11l111_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫḄ"))[1]))
            bstack111l1l111ll_opy_ = bstack111l1l111ll_opy_ or {}
            bstack11l11l1l1l_opy_ = os.environ[bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫḅ")]
            bstack111l1l111ll_opy_[bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨḆ")] = str(framework) + str(__version__)
            bstack111l1l111ll_opy_[bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩḇ")] = bstack1lll1l11ll1_opy_()
            bstack111l1l111ll_opy_[bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫḈ")] = bstack11l11l1l1l_opy_
            bstack111l1l111ll_opy_[bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫḉ")] = bstack111ll111l1_opy_
            ws_endpoint = ws_endpoint.split(bstack11l111_opy_ (u"ࠫࡨࡧࡰࡴ࠿ࠪḊ"))[0] + bstack11l111_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫḋ") + urllib.parse.quote(json.dumps(bstack111l1l111ll_opy_))
    return ws_endpoint
def bstack1111ll1l1l_opy_():
    global bstack11l1l111l_opy_
    from playwright._impl._browser_type import BrowserType
    bstack11l1l111l_opy_ = BrowserType.connect
    return bstack11l1l111l_opy_
def bstack1l11ll1lll_opy_(framework_name):
    global bstack1111l1l1l1_opy_
    bstack1111l1l1l1_opy_ = framework_name
    return framework_name
def bstack1l11l1lll1_opy_(self, *args, **kwargs):
    global bstack11l1l111l_opy_
    try:
        global bstack1111l1l1l1_opy_
        if bstack11l111_opy_ (u"࠭ࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶࠪḌ") in kwargs:
            kwargs[bstack11l111_opy_ (u"ࠧࡸࡵࡈࡲࡩࡶ࡯ࡪࡰࡷࠫḍ")] = bstack111l1111111_opy_(
                kwargs.get(bstack11l111_opy_ (u"ࠨࡹࡶࡉࡳࡪࡰࡰ࡫ࡱࡸࠬḎ"), None),
                bstack1111l1l1l1_opy_
            )
    except Exception as e:
        logger.error(bstack11l111_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫ࡩࡳࠦࡰࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡗࡉࡑࠠࡤࡣࡳࡷ࠿ࠦࡻࡾࠤḏ").format(str(e)))
    return bstack11l1l111l_opy_(self, *args, **kwargs)
def bstack111l11lll1l_opy_(bstack1111l1l111l_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack11l11l1l11_opy_(bstack1111l1l111l_opy_, bstack11l111_opy_ (u"ࠥࠦḐ"))
        if proxies and proxies.get(bstack11l111_opy_ (u"ࠦ࡭ࡺࡴࡱࡵࠥḑ")):
            parsed_url = urlparse(proxies.get(bstack11l111_opy_ (u"ࠧ࡮ࡴࡵࡲࡶࠦḒ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack11l111_opy_ (u"࠭ࡰࡳࡱࡻࡽࡍࡵࡳࡵࠩḓ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack11l111_opy_ (u"ࠧࡱࡴࡲࡼࡾࡖ࡯ࡳࡶࠪḔ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack11l111_opy_ (u"ࠨࡲࡵࡳࡽࡿࡕࡴࡧࡵࠫḕ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack11l111_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡣࡶࡷࠬḖ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack1111l11ll1_opy_(bstack1111l1l111l_opy_):
    bstack111l1l1l111_opy_ = {
        bstack11l11l1llll_opy_[bstack111l1111lll_opy_]: bstack1111l1l111l_opy_[bstack111l1111lll_opy_]
        for bstack111l1111lll_opy_ in bstack1111l1l111l_opy_
        if bstack111l1111lll_opy_ in bstack11l11l1llll_opy_
    }
    bstack111l1l1l111_opy_[bstack11l111_opy_ (u"ࠥࡴࡷࡵࡸࡺࡕࡨࡸࡹ࡯࡮ࡨࡵࠥḗ")] = bstack111l11lll1l_opy_(bstack1111l1l111l_opy_, bstack11111l11_opy_.get_property(bstack11l111_opy_ (u"ࠦࡵࡸ࡯ࡹࡻࡖࡩࡹࡺࡩ࡯ࡩࡶࠦḘ")))
    bstack111l11ll11l_opy_ = [element.lower() for element in bstack11l11ll11ll_opy_]
    bstack111l111ll1l_opy_(bstack111l1l1l111_opy_, bstack111l11ll11l_opy_)
    return bstack111l1l1l111_opy_
def bstack111l111ll1l_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack11l111_opy_ (u"ࠧ࠰ࠪࠫࠬࠥḙ")
    for value in d.values():
        if isinstance(value, dict):
            bstack111l111ll1l_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack111l111ll1l_opy_(item, keys)
def bstack1ll1l1ll111_opy_():
    bstack111l11111ll_opy_ = [os.environ.get(bstack11l111_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡉࡍࡇࡖࡣࡉࡏࡒࠣḚ")), os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠢࡿࠤḛ")), bstack11l111_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨḜ")), os.path.join(bstack11l111_opy_ (u"ࠩ࠲ࡸࡲࡶࠧḝ"), bstack11l111_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪḞ"))]
    for path in bstack111l11111ll_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack11l111_opy_ (u"ࠦࡋ࡯࡬ࡦࠢࠪࠦḟ") + str(path) + bstack11l111_opy_ (u"ࠧ࠭ࠠࡦࡺ࡬ࡷࡹࡹ࠮ࠣḠ"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack11l111_opy_ (u"ࠨࡇࡪࡸ࡬ࡲ࡬ࠦࡰࡦࡴࡰ࡭ࡸࡹࡩࡰࡰࡶࠤ࡫ࡵࡲࠡࠩࠥḡ") + str(path) + bstack11l111_opy_ (u"ࠢࠨࠤḢ"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack11l111_opy_ (u"ࠣࡈ࡬ࡰࡪࠦࠧࠣḣ") + str(path) + bstack11l111_opy_ (u"ࠤࠪࠤࡦࡲࡲࡦࡣࡧࡽࠥ࡮ࡡࡴࠢࡷ࡬ࡪࠦࡲࡦࡳࡸ࡭ࡷ࡫ࡤࠡࡲࡨࡶࡲ࡯ࡳࡴ࡫ࡲࡲࡸ࠴ࠢḤ"))
            else:
                logger.debug(bstack11l111_opy_ (u"ࠥࡇࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥ࡬ࡩ࡭ࡧࠣࠫࠧḥ") + str(path) + bstack11l111_opy_ (u"ࠦࠬࠦࡷࡪࡶ࡫ࠤࡼࡸࡩࡵࡧࠣࡴࡪࡸ࡭ࡪࡵࡶ࡭ࡴࡴ࠮ࠣḦ"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack11l111_opy_ (u"ࠧࡕࡰࡦࡴࡤࡸ࡮ࡵ࡮ࠡࡵࡸࡧࡨ࡫ࡥࡥࡧࡧࠤ࡫ࡵࡲࠡࠩࠥḧ") + str(path) + bstack11l111_opy_ (u"ࠨࠧ࠯ࠤḨ"))
            return path
        except Exception as e:
            logger.debug(bstack11l111_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࠠࡶࡲࠣࡪ࡮ࡲࡥࠡࠩࡾࡴࡦࡺࡨࡾࠩ࠽ࠤࠧḩ") + str(e) + bstack11l111_opy_ (u"ࠣࠤḪ"))
    logger.debug(bstack11l111_opy_ (u"ࠤࡄࡰࡱࠦࡰࡢࡶ࡫ࡷࠥ࡬ࡡࡪ࡮ࡨࡨ࠳ࠨḫ"))
    return None
@measure(event_name=EVENTS.bstack11l11llllll_opy_, stage=STAGE.bstack1l11lll11_opy_)
def bstack1l1l1l1l111_opy_(binary_path, bstack1l11ll111ll_opy_, bs_config):
    logger.debug(bstack11l111_opy_ (u"ࠥࡇࡺࡸࡲࡦࡰࡷࠤࡈࡒࡉࠡࡒࡤࡸ࡭ࠦࡦࡰࡷࡱࡨ࠿ࠦࡻࡾࠤḬ").format(binary_path))
    bstack1111ll11l1l_opy_ = bstack11l111_opy_ (u"ࠫࠬḭ")
    bstack1111lll1ll1_opy_ = {
        bstack11l111_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪḮ"): __version__,
        bstack11l111_opy_ (u"ࠨ࡯ࡴࠤḯ"): platform.system(),
        bstack11l111_opy_ (u"ࠢࡰࡵࡢࡥࡷࡩࡨࠣḰ"): platform.machine(),
        bstack11l111_opy_ (u"ࠣࡥ࡯࡭ࡤࡼࡥࡳࡵ࡬ࡳࡳࠨḱ"): bstack11l111_opy_ (u"ࠩ࠳ࠫḲ"),
        bstack11l111_opy_ (u"ࠥࡷࡩࡱ࡟࡭ࡣࡱ࡫ࡺࡧࡧࡦࠤḳ"): bstack11l111_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫḴ")
    }
    bstack1111lllllll_opy_(bstack1111lll1ll1_opy_)
    try:
        if binary_path:
            bstack1111lll1ll1_opy_[bstack11l111_opy_ (u"ࠬࡩ࡬ࡪࡡࡹࡩࡷࡹࡩࡰࡰࠪḵ")] = subprocess.check_output([binary_path, bstack11l111_opy_ (u"ࠨࡶࡦࡴࡶ࡭ࡴࡴࠢḶ")]).strip().decode(bstack11l111_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ḷ"))
        response = requests.request(
            bstack11l111_opy_ (u"ࠨࡉࡈࡘࠬḸ"),
            url=bstack11l1l11l1_opy_(bstack11l11lll1l1_opy_),
            headers=None,
            auth=(bs_config[bstack11l111_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫḹ")], bs_config[bstack11l111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭Ḻ")]),
            json=None,
            params=bstack1111lll1ll1_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack11l111_opy_ (u"ࠫࡺࡸ࡬ࠨḻ") in data.keys() and bstack11l111_opy_ (u"ࠬࡻࡰࡥࡣࡷࡩࡩࡥࡣ࡭࡫ࡢࡺࡪࡸࡳࡪࡱࡱࠫḼ") in data.keys():
            logger.debug(bstack11l111_opy_ (u"ࠨࡎࡦࡧࡧࠤࡹࡵࠠࡶࡲࡧࡥࡹ࡫ࠠࡣ࡫ࡱࡥࡷࡿࠬࠡࡥࡸࡶࡷ࡫࡮ࡵࠢࡥ࡭ࡳࡧࡲࡺࠢࡹࡩࡷࡹࡩࡰࡰ࠽ࠤࢀࢃࠢḽ").format(bstack1111lll1ll1_opy_[bstack11l111_opy_ (u"ࠧࡤ࡮࡬ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬḾ")]))
            if bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡋࡑࡅࡗ࡟࡟ࡖࡔࡏࠫḿ") in os.environ:
                logger.debug(bstack11l111_opy_ (u"ࠤࡖ࡯࡮ࡶࡰࡪࡰࡪࠤࡧ࡯࡮ࡢࡴࡼࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠦࡡࡴࠢࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡌࡒࡆࡘ࡙ࡠࡗࡕࡐࠥ࡯ࡳࠡࡵࡨࡸࠧṀ"))
                data[bstack11l111_opy_ (u"ࠪࡹࡷࡲࠧṁ")] = os.environ[bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆࡎࡔࡁࡓ࡛ࡢ࡙ࡗࡒࠧṂ")]
            bstack1111l1l1l11_opy_ = bstack111l1l1ll1l_opy_(data[bstack11l111_opy_ (u"ࠬࡻࡲ࡭ࠩṃ")], bstack1l11ll111ll_opy_)
            bstack1111ll11l1l_opy_ = os.path.join(bstack1l11ll111ll_opy_, bstack1111l1l1l11_opy_)
            os.chmod(bstack1111ll11l1l_opy_, 0o777) # bstack1111ll1l11l_opy_ permission
            return bstack1111ll11l1l_opy_
    except Exception as e:
        logger.debug(bstack11l111_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡱࡩࡼࠦࡓࡅࡍࠣࡿࢂࠨṄ").format(e))
    return binary_path
def bstack1111lllllll_opy_(bstack1111lll1ll1_opy_):
    try:
        if bstack11l111_opy_ (u"ࠧ࡭࡫ࡱࡹࡽ࠭ṅ") not in bstack1111lll1ll1_opy_[bstack11l111_opy_ (u"ࠨࡱࡶࠫṆ")].lower():
            return
        if os.path.exists(bstack11l111_opy_ (u"ࠤ࠲ࡩࡹࡩ࠯ࡰࡵ࠰ࡶࡪࡲࡥࡢࡵࡨࠦṇ")):
            with open(bstack11l111_opy_ (u"ࠥ࠳ࡪࡺࡣ࠰ࡱࡶ࠱ࡷ࡫࡬ࡦࡣࡶࡩࠧṈ"), bstack11l111_opy_ (u"ࠦࡷࠨṉ")) as f:
                bstack111l1ll1111_opy_ = {}
                for line in f:
                    if bstack11l111_opy_ (u"ࠧࡃࠢṊ") in line:
                        key, value = line.rstrip().split(bstack11l111_opy_ (u"ࠨ࠽ࠣṋ"), 1)
                        bstack111l1ll1111_opy_[key] = value.strip(bstack11l111_opy_ (u"ࠧࠣ࡞ࠪࠫṌ"))
                bstack1111lll1ll1_opy_[bstack11l111_opy_ (u"ࠨࡦ࡬ࡷࡹࡸ࡯ࠨṍ")] = bstack111l1ll1111_opy_.get(bstack11l111_opy_ (u"ࠤࡌࡈࠧṎ"), bstack11l111_opy_ (u"ࠥࠦṏ"))
        elif os.path.exists(bstack11l111_opy_ (u"ࠦ࠴࡫ࡴࡤ࠱ࡤࡰࡵ࡯࡮ࡦ࠯ࡵࡩࡱ࡫ࡡࡴࡧࠥṐ")):
            bstack1111lll1ll1_opy_[bstack11l111_opy_ (u"ࠬࡪࡩࡴࡶࡵࡳࠬṑ")] = bstack11l111_opy_ (u"࠭ࡡ࡭ࡲ࡬ࡲࡪ࠭Ṓ")
    except Exception as e:
        logger.debug(bstack11l111_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣ࡫ࡪࡺࠠࡥ࡫ࡶࡸࡷࡵࠠࡰࡨࠣࡰ࡮ࡴࡵࡹࠤṓ") + e)
@measure(event_name=EVENTS.bstack11l1l11l11l_opy_, stage=STAGE.bstack1l11lll11_opy_)
def bstack111l1l1ll1l_opy_(bstack111l11l11ll_opy_, bstack111l1lll11l_opy_):
    logger.debug(bstack11l111_opy_ (u"ࠣࡆࡲࡻࡳࡲ࡯ࡢࡦ࡬ࡲ࡬ࠦࡓࡅࡍࠣࡦ࡮ࡴࡡࡳࡻࠣࡪࡷࡵ࡭࠻ࠢࠥṔ") + str(bstack111l11l11ll_opy_) + bstack11l111_opy_ (u"ࠤࠥṕ"))
    zip_path = os.path.join(bstack111l1lll11l_opy_, bstack11l111_opy_ (u"ࠥࡨࡴࡽ࡮࡭ࡱࡤࡨࡪࡪ࡟ࡧ࡫࡯ࡩ࠳ࢀࡩࡱࠤṖ"))
    bstack1111l1l1l11_opy_ = bstack11l111_opy_ (u"ࠫࠬṗ")
    with requests.get(bstack111l11l11ll_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack11l111_opy_ (u"ࠧࡽࡢࠣṘ")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack11l111_opy_ (u"ࠨࡆࡪ࡮ࡨࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࡫ࡤࠡࡵࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࡱࡿ࠮ࠣṙ"))
    with zipfile.ZipFile(zip_path, bstack11l111_opy_ (u"ࠧࡳࠩṚ")) as zip_ref:
        bstack111l1111ll1_opy_ = zip_ref.namelist()
        if len(bstack111l1111ll1_opy_) > 0:
            bstack1111l1l1l11_opy_ = bstack111l1111ll1_opy_[0] # bstack111l1l11l11_opy_ bstack11l1l11lll1_opy_ will be bstack1111l11ll1l_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack111l1lll11l_opy_)
        logger.debug(bstack11l111_opy_ (u"ࠣࡈ࡬ࡰࡪࡹࠠࡴࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࡰࡾࠦࡥࡹࡶࡵࡥࡨࡺࡥࡥࠢࡷࡳࠥ࠭ࠢṛ") + str(bstack111l1lll11l_opy_) + bstack11l111_opy_ (u"ࠤࠪࠦṜ"))
    os.remove(zip_path)
    return bstack1111l1l1l11_opy_
def get_cli_dir():
    bstack1111lll11l1_opy_ = bstack1ll1l1ll111_opy_()
    if bstack1111lll11l1_opy_:
        bstack1l11ll111ll_opy_ = os.path.join(bstack1111lll11l1_opy_, bstack11l111_opy_ (u"ࠥࡧࡱ࡯ࠢṝ"))
        if not os.path.exists(bstack1l11ll111ll_opy_):
            os.makedirs(bstack1l11ll111ll_opy_, mode=0o777, exist_ok=True)
        return bstack1l11ll111ll_opy_
    else:
        raise FileNotFoundError(bstack11l111_opy_ (u"ࠦࡓࡵࠠࡸࡴ࡬ࡸࡦࡨ࡬ࡦࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥࠡࡨࡲࡶࠥࡺࡨࡦࠢࡖࡈࡐࠦࡢࡪࡰࡤࡶࡾ࠴ࠢṞ"))
def bstack1l1l111l11l_opy_(bstack1l11ll111ll_opy_):
    bstack11l111_opy_ (u"ࠧࠨࠢࡈࡧࡷࠤࡹ࡮ࡥࠡࡲࡤࡸ࡭ࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡓࡅࡍࠣࡦ࡮ࡴࡡࡳࡻࠣ࡭ࡳࠦࡡࠡࡹࡵ࡭ࡹࡧࡢ࡭ࡧࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾ࠴ࠢࠣࠤṟ")
    bstack111l11llll1_opy_ = [
        os.path.join(bstack1l11ll111ll_opy_, f)
        for f in os.listdir(bstack1l11ll111ll_opy_)
        if os.path.isfile(os.path.join(bstack1l11ll111ll_opy_, f)) and f.startswith(bstack11l111_opy_ (u"ࠨࡢࡪࡰࡤࡶࡾ࠳ࠢṠ"))
    ]
    if len(bstack111l11llll1_opy_) > 0:
        return max(bstack111l11llll1_opy_, key=os.path.getmtime) # get bstack1111ll11ll1_opy_ binary
    return bstack11l111_opy_ (u"ࠢࠣṡ")
def bstack111l1lll1ll_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l111ll1l1l_opy_(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = bstack1l111ll1l1l_opy_(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack111111ll11_opy_(data, keys, default=None):
    bstack11l111_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡕࡤࡪࡪࡲࡹࠡࡩࡨࡸࠥࡧࠠ࡯ࡧࡶࡸࡪࡪࠠࡷࡣ࡯ࡹࡪࠦࡦࡳࡱࡰࠤࡦࠦࡤࡪࡥࡷ࡭ࡴࡴࡡࡳࡻࠣࡳࡷࠦ࡬ࡪࡵࡷ࠲ࠏࠦࠠࠡࠢ࠽ࡴࡦࡸࡡ࡮ࠢࡧࡥࡹࡧ࠺ࠡࡖ࡫ࡩࠥࡪࡩࡤࡶ࡬ࡳࡳࡧࡲࡺࠢࡲࡶࠥࡲࡩࡴࡶࠣࡸࡴࠦࡴࡳࡣࡹࡩࡷࡹࡥ࠯ࠌࠣࠤࠥࠦ࠺ࡱࡣࡵࡥࡲࠦ࡫ࡦࡻࡶ࠾ࠥࡇࠠ࡭࡫ࡶࡸࠥࡵࡦࠡ࡭ࡨࡽࡸ࠵ࡩ࡯ࡦ࡬ࡧࡪࡹࠠࡳࡧࡳࡶࡪࡹࡥ࡯ࡶ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡴࡦࡺࡨ࠯ࠌࠣࠤࠥࠦ࠺ࡱࡣࡵࡥࡲࠦࡤࡦࡨࡤࡹࡱࡺ࠺ࠡࡘࡤࡰࡺ࡫ࠠࡵࡱࠣࡶࡪࡺࡵࡳࡰࠣ࡭࡫ࠦࡴࡩࡧࠣࡴࡦࡺࡨࠡࡦࡲࡩࡸࠦ࡮ࡰࡶࠣࡩࡽ࡯ࡳࡵ࠰ࠍࠤࠥࠦࠠ࠻ࡴࡨࡸࡺࡸ࡮࠻ࠢࡗ࡬ࡪࠦࡶࡢ࡮ࡸࡩࠥࡧࡴࠡࡶ࡫ࡩࠥࡴࡥࡴࡶࡨࡨࠥࡶࡡࡵࡪ࠯ࠤࡴࡸࠠࡥࡧࡩࡥࡺࡲࡴࠡ࡫ࡩࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪ࠮ࠋࠢࠣࠤࠥࠨࠢࠣṢ")
    if not data:
        return default
    current = data
    try:
        for key in keys:
            if isinstance(current, dict):
                current = current[key]
            elif isinstance(current, list) and isinstance(key, int):
                current = current[key]
            else:
                return default
        return current
    except (KeyError, IndexError, TypeError):
        return default