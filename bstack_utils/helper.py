# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
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
from bstack_utils.constants import (bstack1ll111ll1l_opy_, bstack1ll1ll111l_opy_, bstack1l111lll1l_opy_,
                                    bstack11l11ll11ll_opy_, bstack11l1l1l111l_opy_, bstack11l1l1l11l1_opy_, bstack11l1l11l111_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack1l111ll1ll_opy_, bstack11l1ll1ll1_opy_
from bstack_utils.proxy import bstack1l1lll1l1l_opy_, bstack111lll1l1l_opy_
from bstack_utils.constants import *
from bstack_utils import bstack11l1l1l1ll_opy_
from bstack_utils.bstack11llll1l11_opy_ import bstack1lll11l111_opy_
from browserstack_sdk._version import __version__
bstack1111l111_opy_ = Config.bstack11111ll1_opy_()
logger = bstack11l1l1l1ll_opy_.get_logger(__name__, bstack11l1l1l1ll_opy_.bstack1l1l111l1ll_opy_())
def bstack111l1l1l111_opy_(config):
    return config[bstack11ll_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ᯯ")]
def bstack1111l1l111l_opy_(config):
    return config[bstack11ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨᯰ")]
def bstack1l1llll111_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack111l1l1111l_opy_(obj):
    values = []
    bstack111l111111l_opy_ = re.compile(bstack11ll_opy_ (u"ࡸࠢ࡟ࡅࡘࡗ࡙ࡕࡍࡠࡖࡄࡋࡤࡢࡤࠬࠦࠥᯱ"), re.I)
    for key in obj.keys():
        if bstack111l111111l_opy_.match(key):
            values.append(obj[key])
    return values
def bstack111l1l1lll1_opy_(config):
    tags = []
    tags.extend(bstack111l1l1111l_opy_(os.environ))
    tags.extend(bstack111l1l1111l_opy_(config))
    return tags
def bstack111l11lllll_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack111l1lll1l1_opy_(bstack1111l11ll1l_opy_):
    if not bstack1111l11ll1l_opy_:
        return bstack11ll_opy_ (u"ࠧࠨ᯲")
    return bstack11ll_opy_ (u"ࠣࡽࢀࠤ࠭ࢁࡽࠪࠤ᯳").format(bstack1111l11ll1l_opy_.name, bstack1111l11ll1l_opy_.email)
def bstack111l1l1l11l_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack111l1l11ll1_opy_ = repo.common_dir
        info = {
            bstack11ll_opy_ (u"ࠤࡶ࡬ࡦࠨ᯴"): repo.head.commit.hexsha,
            bstack11ll_opy_ (u"ࠥࡷ࡭ࡵࡲࡵࡡࡶ࡬ࡦࠨ᯵"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack11ll_opy_ (u"ࠦࡧࡸࡡ࡯ࡥ࡫ࠦ᯶"): repo.active_branch.name,
            bstack11ll_opy_ (u"ࠧࡺࡡࡨࠤ᯷"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack11ll_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡺࡥࡳࠤ᯸"): bstack111l1lll1l1_opy_(repo.head.commit.committer),
            bstack11ll_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡴࡦࡴࡢࡨࡦࡺࡥࠣ᯹"): repo.head.commit.committed_datetime.isoformat(),
            bstack11ll_opy_ (u"ࠣࡣࡸࡸ࡭ࡵࡲࠣ᯺"): bstack111l1lll1l1_opy_(repo.head.commit.author),
            bstack11ll_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࡡࡧࡥࡹ࡫ࠢ᯻"): repo.head.commit.authored_datetime.isoformat(),
            bstack11ll_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡢࡱࡪࡹࡳࡢࡩࡨࠦ᯼"): repo.head.commit.message,
            bstack11ll_opy_ (u"ࠦࡷࡵ࡯ࡵࠤ᯽"): repo.git.rev_parse(bstack11ll_opy_ (u"ࠧ࠳࠭ࡴࡪࡲࡻ࠲ࡺ࡯ࡱ࡮ࡨࡺࡪࡲࠢ᯾")),
            bstack11ll_opy_ (u"ࠨࡣࡰ࡯ࡰࡳࡳࡥࡧࡪࡶࡢࡨ࡮ࡸࠢ᯿"): bstack111l1l11ll1_opy_,
            bstack11ll_opy_ (u"ࠢࡸࡱࡵ࡯ࡹࡸࡥࡦࡡࡪ࡭ࡹࡥࡤࡪࡴࠥᰀ"): subprocess.check_output([bstack11ll_opy_ (u"ࠣࡩ࡬ࡸࠧᰁ"), bstack11ll_opy_ (u"ࠤࡵࡩࡻ࠳ࡰࡢࡴࡶࡩࠧᰂ"), bstack11ll_opy_ (u"ࠥ࠱࠲࡭ࡩࡵ࠯ࡦࡳࡲࡳ࡯࡯࠯ࡧ࡭ࡷࠨᰃ")]).strip().decode(
                bstack11ll_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᰄ")),
            bstack11ll_opy_ (u"ࠧࡲࡡࡴࡶࡢࡸࡦ࡭ࠢᰅ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack11ll_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡹ࡟ࡴ࡫ࡱࡧࡪࡥ࡬ࡢࡵࡷࡣࡹࡧࡧࠣᰆ"): repo.git.rev_list(
                bstack11ll_opy_ (u"ࠢࡼࡿ࠱࠲ࢀࢃࠢᰇ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack111l11l1111_opy_ = []
        for remote in remotes:
            bstack111l1111l1l_opy_ = {
                bstack11ll_opy_ (u"ࠣࡰࡤࡱࡪࠨᰈ"): remote.name,
                bstack11ll_opy_ (u"ࠤࡸࡶࡱࠨᰉ"): remote.url,
            }
            bstack111l11l1111_opy_.append(bstack111l1111l1l_opy_)
        bstack1111ll1l11l_opy_ = {
            bstack11ll_opy_ (u"ࠥࡲࡦࡳࡥࠣᰊ"): bstack11ll_opy_ (u"ࠦ࡬࡯ࡴࠣᰋ"),
            **info,
            bstack11ll_opy_ (u"ࠧࡸࡥ࡮ࡱࡷࡩࡸࠨᰌ"): bstack111l11l1111_opy_
        }
        bstack1111ll1l11l_opy_ = bstack111l1l111l1_opy_(bstack1111ll1l11l_opy_)
        return bstack1111ll1l11l_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack11ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡯ࡱࡷ࡯ࡥࡹ࡯࡮ࡨࠢࡊ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡹ࡬ࡸ࡭ࠦࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠤᰍ").format(err))
        return {}
def bstack11ll1l1l1ll_opy_(bstack111l11ll11l_opy_=None):
    bstack11ll_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡈࡧࡷࠤ࡬࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡷࡵ࡫ࡣࡪࡨ࡬ࡧࡦࡲ࡬ࡺࠢࡩࡳࡷࡳࡡࡵࡶࡨࡨࠥ࡬࡯ࡳࠢࡄࡍࠥࡹࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠡࡷࡶࡩࠥࡩࡡࡴࡧࡶࠤ࡫ࡵࡲࠡࡧࡤࡧ࡭ࠦࡦࡰ࡮ࡧࡩࡷࠦࡩ࡯ࠢࡷ࡬ࡪࠦ࡬ࡪࡵࡷ࠲ࠏࠦࠠࠡࠢࡄࡶ࡬ࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡩࡳࡱࡪࡥࡳࡵࠣࠬࡱ࡯ࡳࡵ࠮ࠣࡳࡵࡺࡩࡰࡰࡤࡰ࠮ࡀࠠࡍ࡫ࡶࡸࠥࡵࡦࠡࡨࡲࡰࡩ࡫ࡲࠡࡲࡤࡸ࡭ࡹࠠࡵࡱࠣࡩࡽࡺࡲࡢࡥࡷࠤ࡬࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡪࡷࡵ࡭࠯ࠢࡇࡩ࡫ࡧࡵ࡭ࡶࡶࠤࡹࡵࠠ࡜ࡱࡶ࠲࡬࡫ࡴࡤࡹࡧࠬ࠮ࡣ࠮ࠋࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡮࡬ࡷࡹࡀࠠࡍ࡫ࡶࡸࠥࡵࡦࠡࡦ࡬ࡧࡹࡹࠬࠡࡧࡤࡧ࡭ࠦࡣࡰࡰࡷࡥ࡮ࡴࡩ࡯ࡩࠣ࡫࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡩࡳࡷࠦࡡࠡࡨࡲࡰࡩ࡫ࡲ࠯ࠌࠣࠤࠥࠦࠢࠣࠤᰎ")
    if bstack111l11ll11l_opy_ == None: # bstack1111lllll1l_opy_ for bstack11ll1lllll1_opy_-repo
        bstack111l11ll11l_opy_ = [os.getcwd()]
    results = []
    for folder in bstack111l11ll11l_opy_:
        try:
            repo = git.Repo(folder, search_parent_directories=True)
            result = {
                bstack11ll_opy_ (u"ࠣࡲࡵࡍࡩࠨᰏ"): bstack11ll_opy_ (u"ࠤࠥᰐ"),
                bstack11ll_opy_ (u"ࠥࡪ࡮ࡲࡥࡴࡅ࡫ࡥࡳ࡭ࡥࡥࠤᰑ"): [],
                bstack11ll_opy_ (u"ࠦࡦࡻࡴࡩࡱࡵࡷࠧᰒ"): [],
                bstack11ll_opy_ (u"ࠧࡶࡲࡅࡣࡷࡩࠧᰓ"): bstack11ll_opy_ (u"ࠨࠢᰔ"),
                bstack11ll_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡍࡦࡵࡶࡥ࡬࡫ࡳࠣᰕ"): [],
                bstack11ll_opy_ (u"ࠣࡲࡵࡘ࡮ࡺ࡬ࡦࠤᰖ"): bstack11ll_opy_ (u"ࠤࠥᰗ"),
                bstack11ll_opy_ (u"ࠥࡴࡷࡊࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠥᰘ"): bstack11ll_opy_ (u"ࠦࠧᰙ"),
                bstack11ll_opy_ (u"ࠧࡶࡲࡓࡣࡺࡈ࡮࡬ࡦࠣᰚ"): bstack11ll_opy_ (u"ࠨࠢᰛ")
            }
            bstack1111llllll1_opy_ = repo.active_branch.name
            bstack1111l11l1l1_opy_ = repo.head.commit
            result[bstack11ll_opy_ (u"ࠢࡱࡴࡌࡨࠧᰜ")] = bstack1111l11l1l1_opy_.hexsha
            bstack1111l1l1l1l_opy_ = _111l1l1l1l1_opy_(repo)
            logger.debug(bstack11ll_opy_ (u"ࠣࡄࡤࡷࡪࠦࡢࡳࡣࡱࡧ࡭ࠦࡦࡰࡴࠣࡧࡴࡳࡰࡢࡴ࡬ࡷࡴࡴ࠺ࠡࠤᰝ") + str(bstack1111l1l1l1l_opy_) + bstack11ll_opy_ (u"ࠤࠥᰞ"))
            if bstack1111l1l1l1l_opy_:
                try:
                    bstack1111lll1111_opy_ = repo.git.diff(bstack11ll_opy_ (u"ࠥ࠱࠲ࡴࡡ࡮ࡧ࠰ࡳࡳࡲࡹࠣᰟ"), bstack11l1llll_opy_ (u"ࠦࢀࡨࡡࡴࡧࡢࡦࡷࡧ࡮ࡤࡪࢀ࠲࠳࠴ࡻࡤࡷࡵࡶࡪࡴࡴࡠࡤࡵࡥࡳࡩࡨࡾࠤᰠ")).split(bstack11ll_opy_ (u"ࠬࡢ࡮ࠨᰡ"))
                    logger.debug(bstack11ll_opy_ (u"ࠨࡃࡩࡣࡱ࡫ࡪࡪࠠࡧ࡫࡯ࡩࡸࠦࡢࡦࡶࡺࡩࡪࡴࠠࡼࡤࡤࡷࡪࡥࡢࡳࡣࡱࡧ࡭ࢃࠠࡢࡰࡧࠤࢀࡩࡵࡳࡴࡨࡲࡹࡥࡢࡳࡣࡱࡧ࡭ࢃ࠺ࠡࠤᰢ") + str(bstack1111lll1111_opy_) + bstack11ll_opy_ (u"ࠢࠣᰣ"))
                    result[bstack11ll_opy_ (u"ࠣࡨ࡬ࡰࡪࡹࡃࡩࡣࡱ࡫ࡪࡪࠢᰤ")] = [f.strip() for f in bstack1111lll1111_opy_ if f.strip()]
                    commits = list(repo.iter_commits(bstack11l1llll_opy_ (u"ࠤࡾࡦࡦࡹࡥࡠࡤࡵࡥࡳࡩࡨࡾ࠰࠱ࡿࡨࡻࡲࡳࡧࡱࡸࡤࡨࡲࡢࡰࡦ࡬ࢂࠨᰥ")))
                except Exception:
                    logger.debug(bstack11ll_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡧࡦࡶࠣࡧ࡭ࡧ࡮ࡨࡧࡧࠤ࡫࡯࡬ࡦࡵࠣࡪࡷࡵ࡭ࠡࡤࡵࡥࡳࡩࡨࠡࡥࡲࡱࡵࡧࡲࡪࡵࡲࡲ࠳ࠦࡆࡢ࡮࡯࡭ࡳ࡭ࠠࡣࡣࡦ࡯ࠥࡺ࡯ࠡࡴࡨࡧࡪࡴࡴࠡࡥࡲࡱࡲ࡯ࡴࡴ࠰ࠥᰦ"))
                    commits = list(repo.iter_commits(max_count=10))
                    if commits:
                        result[bstack11ll_opy_ (u"ࠦ࡫࡯࡬ࡦࡵࡆ࡬ࡦࡴࡧࡦࡦࠥᰧ")] = _111l11llll1_opy_(commits[:5])
            else:
                commits = list(repo.iter_commits(max_count=10))
                if commits:
                    result[bstack11ll_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡶࡇ࡭ࡧ࡮ࡨࡧࡧࠦᰨ")] = _111l11llll1_opy_(commits[:5])
            bstack1111ll111l1_opy_ = set()
            bstack111l1ll1l1l_opy_ = []
            for commit in commits:
                logger.debug(bstack11ll_opy_ (u"ࠨࡐࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡧࡴࡳ࡭ࡪࡶ࠽ࠤࠧᰩ") + str(commit.message) + bstack11ll_opy_ (u"ࠢࠣᰪ"))
                bstack1111lllll11_opy_ = commit.author.name if commit.author else bstack11ll_opy_ (u"ࠣࡗࡱ࡯ࡳࡵࡷ࡯ࠤᰫ")
                bstack1111ll111l1_opy_.add(bstack1111lllll11_opy_)
                bstack111l1ll1l1l_opy_.append({
                    bstack11ll_opy_ (u"ࠤࡰࡩࡸࡹࡡࡨࡧࠥᰬ"): commit.message.strip(),
                    bstack11ll_opy_ (u"ࠥࡹࡸ࡫ࡲࠣᰭ"): bstack1111lllll11_opy_
                })
            result[bstack11ll_opy_ (u"ࠦࡦࡻࡴࡩࡱࡵࡷࠧᰮ")] = list(bstack1111ll111l1_opy_)
            result[bstack11ll_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡒ࡫ࡳࡴࡣࡪࡩࡸࠨᰯ")] = bstack111l1ll1l1l_opy_
            result[bstack11ll_opy_ (u"ࠨࡰࡳࡆࡤࡸࡪࠨᰰ")] = bstack1111l11l1l1_opy_.committed_datetime.strftime(bstack11ll_opy_ (u"࡛ࠢࠦ࠰ࠩࡲ࠳ࠥࡥࠤᰱ"))
            if (not result[bstack11ll_opy_ (u"ࠣࡲࡵࡘ࡮ࡺ࡬ࡦࠤᰲ")] or result[bstack11ll_opy_ (u"ࠤࡳࡶ࡙࡯ࡴ࡭ࡧࠥᰳ")].strip() == bstack11ll_opy_ (u"ࠥࠦᰴ")) and bstack1111l11l1l1_opy_.message:
                bstack111l1lll11l_opy_ = bstack1111l11l1l1_opy_.message.strip().splitlines()
                result[bstack11ll_opy_ (u"ࠦࡵࡸࡔࡪࡶ࡯ࡩࠧᰵ")] = bstack111l1lll11l_opy_[0] if bstack111l1lll11l_opy_ else bstack11ll_opy_ (u"ࠧࠨᰶ")
                if len(bstack111l1lll11l_opy_) > 2:
                    result[bstack11ll_opy_ (u"ࠨࡰࡳࡆࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳࠨ᰷")] = bstack11ll_opy_ (u"ࠧ࡝ࡰࠪ᰸").join(bstack111l1lll11l_opy_[2:]).strip()
            results.append(result)
        except Exception as err:
            logger.error(bstack11ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡱࡳࡹࡱࡧࡴࡪࡰࡪࠤࡌ࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡪࡴࡸࠠࡂࡋࠣࡷࡪࡲࡥࡤࡶ࡬ࡳࡳࠦࠨࡧࡱ࡯ࡨࡪࡸ࠺ࠡࡽࡩࡳࡱࡪࡥࡳࡿࠬ࠾ࠥࠨ᰹") + str(err) + bstack11ll_opy_ (u"ࠤࠥ᰺"))
    filtered_results = [
        result
        for result in results
        if _1111ll1ll1l_opy_(result)
    ]
    return filtered_results
def _1111ll1ll1l_opy_(result):
    bstack11ll_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡌࡪࡲࡰࡦࡴࠣࡸࡴࠦࡣࡩࡧࡦ࡯ࠥ࡯ࡦࠡࡣࠣ࡫࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡵࡩࡸࡻ࡬ࡵࠢ࡬ࡷࠥࡼࡡ࡭࡫ࡧࠤ࠭ࡴ࡯࡯࠯ࡨࡱࡵࡺࡹࠡࡨ࡬ࡰࡪࡹࡃࡩࡣࡱ࡫ࡪࡪࠠࡢࡰࡧࠤࡦࡻࡴࡩࡱࡵࡷ࠮࠴ࠊࠡࠢࠣࠤࠧࠨࠢ᰻")
    return (
        isinstance(result.get(bstack11ll_opy_ (u"ࠦ࡫࡯࡬ࡦࡵࡆ࡬ࡦࡴࡧࡦࡦࠥ᰼"), None), list)
        and len(result[bstack11ll_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡶࡇ࡭ࡧ࡮ࡨࡧࡧࠦ᰽")]) > 0
        and isinstance(result.get(bstack11ll_opy_ (u"ࠨࡡࡶࡶ࡫ࡳࡷࡹࠢ᰾"), None), list)
        and len(result[bstack11ll_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸࡳࠣ᰿")]) > 0
    )
def _111l1l1l1l1_opy_(repo):
    bstack11ll_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡖࡵࡽࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤࡹ࡮ࡥࠡࡤࡤࡷࡪࠦࡢࡳࡣࡱࡧ࡭ࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡨ࡫ࡹࡩࡳࠦࡲࡦࡲࡲࠤࡼ࡯ࡴࡩࡱࡸࡸࠥ࡮ࡡࡳࡦࡦࡳࡩ࡫ࡤࠡࡰࡤࡱࡪࡹࠠࡢࡰࡧࠤࡼࡵࡲ࡬ࠢࡺ࡭ࡹ࡮ࠠࡢ࡮࡯ࠤ࡛ࡉࡓࠡࡲࡵࡳࡻ࡯ࡤࡦࡴࡶ࠲ࠏࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵࠣࡸ࡭࡫ࠠࡥࡧࡩࡥࡺࡲࡴࠡࡤࡵࡥࡳࡩࡨࠡ࡫ࡩࠤࡵࡵࡳࡴ࡫ࡥࡰࡪ࠲ࠠࡦ࡮ࡶࡩࠥࡔ࡯࡯ࡧ࠱ࠎࠥࠦࠠࠡࠤࠥࠦ᱀")
    try:
        try:
            origin = repo.remotes.origin
            bstack111l1111ll1_opy_ = origin.refs[bstack11ll_opy_ (u"ࠩࡋࡉࡆࡊࠧ᱁")]
            target = bstack111l1111ll1_opy_.reference.name
            if target.startswith(bstack11ll_opy_ (u"ࠪࡳࡷ࡯ࡧࡪࡰ࠲ࠫ᱂")):
                return target
        except Exception:
            pass
        if repo.remotes and repo.remotes.origin.refs:
            for ref in repo.remotes.origin.refs:
                if ref.name.startswith(bstack11ll_opy_ (u"ࠫࡴࡸࡩࡨ࡫ࡱ࠳ࠬ᱃")):
                    return ref.name
        if repo.heads:
            return repo.heads[0].name
    except Exception:
        pass
    return None
def _111l11llll1_opy_(commits):
    bstack11ll_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡍࡥࡵࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡧ࡭ࡧ࡮ࡨࡧࡧࠤ࡫࡯࡬ࡦࡵࠣࡪࡷࡵ࡭ࠡࡣࠣࡰ࡮ࡹࡴࠡࡱࡩࠤࡨࡵ࡭࡮࡫ࡷࡷ࠳ࠐࠠࠡࠢࠣࠦࠧࠨ᱄")
    bstack1111lll1111_opy_ = set()
    try:
        for commit in commits:
            if commit.parents:
                for parent in commit.parents:
                    diff = commit.diff(parent)
                    for bstack111l11l1ll1_opy_ in diff:
                        if bstack111l11l1ll1_opy_.a_path:
                            bstack1111lll1111_opy_.add(bstack111l11l1ll1_opy_.a_path)
                        if bstack111l11l1ll1_opy_.b_path:
                            bstack1111lll1111_opy_.add(bstack111l11l1ll1_opy_.b_path)
    except Exception:
        pass
    return list(bstack1111lll1111_opy_)
def bstack111l1l111l1_opy_(bstack1111ll1l11l_opy_):
    bstack1111ll11l1l_opy_ = bstack111l1111lll_opy_(bstack1111ll1l11l_opy_)
    if bstack1111ll11l1l_opy_ and bstack1111ll11l1l_opy_ > bstack11l11ll11ll_opy_:
        bstack1111lll1l1l_opy_ = bstack1111ll11l1l_opy_ - bstack11l11ll11ll_opy_
        bstack111l1ll11ll_opy_ = bstack1111lll1lll_opy_(bstack1111ll1l11l_opy_[bstack11ll_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡥ࡭ࡦࡵࡶࡥ࡬࡫ࠢ᱅")], bstack1111lll1l1l_opy_)
        bstack1111ll1l11l_opy_[bstack11ll_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠣ᱆")] = bstack111l1ll11ll_opy_
        logger.info(bstack11ll_opy_ (u"ࠣࡖ࡫ࡩࠥࡩ࡯࡮࡯࡬ࡸࠥ࡮ࡡࡴࠢࡥࡩࡪࡴࠠࡵࡴࡸࡲࡨࡧࡴࡦࡦ࠱ࠤࡘ࡯ࡺࡦࠢࡲࡪࠥࡩ࡯࡮࡯࡬ࡸࠥࡧࡦࡵࡧࡵࠤࡹࡸࡵ࡯ࡥࡤࡸ࡮ࡵ࡮ࠡ࡫ࡶࠤࢀࢃࠠࡌࡄࠥ᱇")
                    .format(bstack111l1111lll_opy_(bstack1111ll1l11l_opy_) / 1024))
    return bstack1111ll1l11l_opy_
def bstack111l1111lll_opy_(json_data):
    try:
        if json_data:
            bstack1111ll1llll_opy_ = json.dumps(json_data)
            bstack1111l1l11l1_opy_ = sys.getsizeof(bstack1111ll1llll_opy_)
            return bstack1111l1l11l1_opy_
    except Exception as e:
        logger.debug(bstack11ll_opy_ (u"ࠤࡖࡳࡲ࡫ࡴࡩ࡫ࡱ࡫ࠥࡽࡥ࡯ࡶࠣࡻࡷࡵ࡮ࡨࠢࡺ࡬࡮ࡲࡥࠡࡥࡤࡰࡨࡻ࡬ࡢࡶ࡬ࡲ࡬ࠦࡳࡪࡼࡨࠤࡴ࡬ࠠࡋࡕࡒࡒࠥࡵࡢ࡫ࡧࡦࡸ࠿ࠦࡻࡾࠤ᱈").format(e))
    return -1
def bstack1111lll1lll_opy_(field, bstack1111llll111_opy_):
    try:
        bstack1111lllllll_opy_ = len(bytes(bstack11l1l1l111l_opy_, bstack11ll_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩ᱉")))
        bstack1111ll1l1l1_opy_ = bytes(field, bstack11ll_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪ᱊"))
        bstack1111ll11111_opy_ = len(bstack1111ll1l1l1_opy_)
        bstack111l1ll1111_opy_ = ceil(bstack1111ll11111_opy_ - bstack1111llll111_opy_ - bstack1111lllllll_opy_)
        if bstack111l1ll1111_opy_ > 0:
            bstack1111l1l1lll_opy_ = bstack1111ll1l1l1_opy_[:bstack111l1ll1111_opy_].decode(bstack11ll_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫ᱋"), errors=bstack11ll_opy_ (u"࠭ࡩࡨࡰࡲࡶࡪ࠭᱌")) + bstack11l1l1l111l_opy_
            return bstack1111l1l1lll_opy_
    except Exception as e:
        logger.debug(bstack11ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡺࡲࡶࡰࡦࡥࡹ࡯࡮ࡨࠢࡩ࡭ࡪࡲࡤ࠭ࠢࡱࡳࡹ࡮ࡩ࡯ࡩࠣࡻࡦࡹࠠࡵࡴࡸࡲࡨࡧࡴࡦࡦࠣ࡬ࡪࡸࡥ࠻ࠢࡾࢁࠧᱍ").format(e))
    return field
def bstack111l1l1l11_opy_():
    env = os.environ
    if (bstack11ll_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡘࡖࡑࠨᱎ") in env and len(env[bstack11ll_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢ࡙ࡗࡒࠢᱏ")]) > 0) or (
            bstack11ll_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣࡍࡕࡍࡆࠤ᱐") in env and len(env[bstack11ll_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤࡎࡏࡎࡇࠥ᱑")]) > 0):
        return {
            bstack11ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᱒"): bstack11ll_opy_ (u"ࠨࡊࡦࡰ࡮࡭ࡳࡹࠢ᱓"),
            bstack11ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ᱔"): env.get(bstack11ll_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦ᱕")),
            bstack11ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ᱖"): env.get(bstack11ll_opy_ (u"ࠥࡎࡔࡈ࡟ࡏࡃࡐࡉࠧ᱗")),
            bstack11ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ᱘"): env.get(bstack11ll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦ᱙"))
        }
    if env.get(bstack11ll_opy_ (u"ࠨࡃࡊࠤᱚ")) == bstack11ll_opy_ (u"ࠢࡵࡴࡸࡩࠧᱛ") and bstack1lll1l1lll_opy_(env.get(bstack11ll_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡄࡋࠥᱜ"))):
        return {
            bstack11ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᱝ"): bstack11ll_opy_ (u"ࠥࡇ࡮ࡸࡣ࡭ࡧࡆࡍࠧᱞ"),
            bstack11ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᱟ"): env.get(bstack11ll_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᱠ")),
            bstack11ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᱡ"): env.get(bstack11ll_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋ࡟ࡋࡑࡅࠦᱢ")),
            bstack11ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᱣ"): env.get(bstack11ll_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࠧᱤ"))
        }
    if env.get(bstack11ll_opy_ (u"ࠥࡇࡎࠨᱥ")) == bstack11ll_opy_ (u"ࠦࡹࡸࡵࡦࠤᱦ") and bstack1lll1l1lll_opy_(env.get(bstack11ll_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࠧᱧ"))):
        return {
            bstack11ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᱨ"): bstack11ll_opy_ (u"ࠢࡕࡴࡤࡺ࡮ࡹࠠࡄࡋࠥᱩ"),
            bstack11ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᱪ"): env.get(bstack11ll_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࡡࡅ࡙ࡎࡒࡄࡠ࡙ࡈࡆࡤ࡛ࡒࡍࠤᱫ")),
            bstack11ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᱬ"): env.get(bstack11ll_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᱭ")),
            bstack11ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᱮ"): env.get(bstack11ll_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᱯ"))
        }
    if env.get(bstack11ll_opy_ (u"ࠢࡄࡋࠥᱰ")) == bstack11ll_opy_ (u"ࠣࡶࡵࡹࡪࠨᱱ") and env.get(bstack11ll_opy_ (u"ࠤࡆࡍࡤࡔࡁࡎࡇࠥᱲ")) == bstack11ll_opy_ (u"ࠥࡧࡴࡪࡥࡴࡪ࡬ࡴࠧᱳ"):
        return {
            bstack11ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᱴ"): bstack11ll_opy_ (u"ࠧࡉ࡯ࡥࡧࡶ࡬࡮ࡶࠢᱵ"),
            bstack11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᱶ"): None,
            bstack11ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᱷ"): None,
            bstack11ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᱸ"): None
        }
    if env.get(bstack11ll_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡈࡒࡂࡐࡆࡌࠧᱹ")) and env.get(bstack11ll_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡃࡐࡏࡐࡍ࡙ࠨᱺ")):
        return {
            bstack11ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᱻ"): bstack11ll_opy_ (u"ࠧࡈࡩࡵࡤࡸࡧࡰ࡫ࡴࠣᱼ"),
            bstack11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᱽ"): env.get(bstack11ll_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡋࡎ࡚࡟ࡉࡖࡗࡔࡤࡕࡒࡊࡉࡌࡒࠧ᱾")),
            bstack11ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᱿"): None,
            bstack11ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᲀ"): env.get(bstack11ll_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᲁ"))
        }
    if env.get(bstack11ll_opy_ (u"ࠦࡈࡏࠢᲂ")) == bstack11ll_opy_ (u"ࠧࡺࡲࡶࡧࠥᲃ") and bstack1lll1l1lll_opy_(env.get(bstack11ll_opy_ (u"ࠨࡄࡓࡑࡑࡉࠧᲄ"))):
        return {
            bstack11ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᲅ"): bstack11ll_opy_ (u"ࠣࡆࡵࡳࡳ࡫ࠢᲆ"),
            bstack11ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᲇ"): env.get(bstack11ll_opy_ (u"ࠥࡈࡗࡕࡎࡆࡡࡅ࡙ࡎࡒࡄࡠࡎࡌࡒࡐࠨᲈ")),
            bstack11ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᲉ"): None,
            bstack11ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᲊ"): env.get(bstack11ll_opy_ (u"ࠨࡄࡓࡑࡑࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦ᲋"))
        }
    if env.get(bstack11ll_opy_ (u"ࠢࡄࡋࠥ᲌")) == bstack11ll_opy_ (u"ࠣࡶࡵࡹࡪࠨ᲍") and bstack1lll1l1lll_opy_(env.get(bstack11ll_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࠧ᲎"))):
        return {
            bstack11ll_opy_ (u"ࠥࡲࡦࡳࡥࠣ᲏"): bstack11ll_opy_ (u"ࠦࡘ࡫࡭ࡢࡲ࡫ࡳࡷ࡫ࠢᲐ"),
            bstack11ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᲑ"): env.get(bstack11ll_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࡡࡒࡖࡌࡇࡎࡊ࡜ࡄࡘࡎࡕࡎࡠࡗࡕࡐࠧᲒ")),
            bstack11ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᲓ"): env.get(bstack11ll_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᲔ")),
            bstack11ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᲕ"): env.get(bstack11ll_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࡥࡊࡐࡄࡢࡍࡉࠨᲖ"))
        }
    if env.get(bstack11ll_opy_ (u"ࠦࡈࡏࠢᲗ")) == bstack11ll_opy_ (u"ࠧࡺࡲࡶࡧࠥᲘ") and bstack1lll1l1lll_opy_(env.get(bstack11ll_opy_ (u"ࠨࡇࡊࡖࡏࡅࡇࡥࡃࡊࠤᲙ"))):
        return {
            bstack11ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᲚ"): bstack11ll_opy_ (u"ࠣࡉ࡬ࡸࡑࡧࡢࠣᲛ"),
            bstack11ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᲜ"): env.get(bstack11ll_opy_ (u"ࠥࡇࡎࡥࡊࡐࡄࡢ࡙ࡗࡒࠢᲝ")),
            bstack11ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᲞ"): env.get(bstack11ll_opy_ (u"ࠧࡉࡉࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᲟ")),
            bstack11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᲠ"): env.get(bstack11ll_opy_ (u"ࠢࡄࡋࡢࡎࡔࡈ࡟ࡊࡆࠥᲡ"))
        }
    if env.get(bstack11ll_opy_ (u"ࠣࡅࡌࠦᲢ")) == bstack11ll_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᲣ") and bstack1lll1l1lll_opy_(env.get(bstack11ll_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࠨᲤ"))):
        return {
            bstack11ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᲥ"): bstack11ll_opy_ (u"ࠧࡈࡵࡪ࡮ࡧ࡯࡮ࡺࡥࠣᲦ"),
            bstack11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᲧ"): env.get(bstack11ll_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᲨ")),
            bstack11ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᲩ"): env.get(bstack11ll_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡒࡁࡃࡇࡏࠦᲪ")) or env.get(bstack11ll_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡐࡄࡑࡊࠨᲫ")),
            bstack11ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᲬ"): env.get(bstack11ll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᲭ"))
        }
    if bstack1lll1l1lll_opy_(env.get(bstack11ll_opy_ (u"ࠨࡔࡇࡡࡅ࡙ࡎࡒࡄࠣᲮ"))):
        return {
            bstack11ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᲯ"): bstack11ll_opy_ (u"ࠣࡘ࡬ࡷࡺࡧ࡬ࠡࡕࡷࡹࡩ࡯࡯ࠡࡖࡨࡥࡲࠦࡓࡦࡴࡹ࡭ࡨ࡫ࡳࠣᲰ"),
            bstack11ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᲱ"): bstack11ll_opy_ (u"ࠥࡿࢂࢁࡽࠣᲲ").format(env.get(bstack11ll_opy_ (u"ࠫࡘ࡟ࡓࡕࡇࡐࡣ࡙ࡋࡁࡎࡈࡒ࡙ࡓࡊࡁࡕࡋࡒࡒࡘࡋࡒࡗࡇࡕ࡙ࡗࡏࠧᲳ")), env.get(bstack11ll_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡓࡖࡔࡐࡅࡄࡖࡌࡈࠬᲴ"))),
            bstack11ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᲵ"): env.get(bstack11ll_opy_ (u"ࠢࡔ࡛ࡖࡘࡊࡓ࡟ࡅࡇࡉࡍࡓࡏࡔࡊࡑࡑࡍࡉࠨᲶ")),
            bstack11ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᲷ"): env.get(bstack11ll_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠤᲸ"))
        }
    if bstack1lll1l1lll_opy_(env.get(bstack11ll_opy_ (u"ࠥࡅࡕࡖࡖࡆ࡛ࡒࡖࠧᲹ"))):
        return {
            bstack11ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᲺ"): bstack11ll_opy_ (u"ࠧࡇࡰࡱࡸࡨࡽࡴࡸࠢ᲻"),
            bstack11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᲼"): bstack11ll_opy_ (u"ࠢࡼࡿ࠲ࡴࡷࡵࡪࡦࡥࡷ࠳ࢀࢃ࠯ࡼࡿ࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂࠨᲽ").format(env.get(bstack11ll_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢ࡙ࡗࡒࠧᲾ")), env.get(bstack11ll_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡆࡉࡃࡐࡗࡑࡘࡤࡔࡁࡎࡇࠪᲿ")), env.get(bstack11ll_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡖࡒࡐࡌࡈࡇ࡙ࡥࡓࡍࡗࡊࠫ᳀")), env.get(bstack11ll_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨ᳁"))),
            bstack11ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ᳂"): env.get(bstack11ll_opy_ (u"ࠨࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥ᳃")),
            bstack11ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᳄"): env.get(bstack11ll_opy_ (u"ࠣࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤ᳅"))
        }
    if env.get(bstack11ll_opy_ (u"ࠤࡄ࡞࡚ࡘࡅࡠࡊࡗࡘࡕࡥࡕࡔࡇࡕࡣࡆࡍࡅࡏࡖࠥ᳆")) and env.get(bstack11ll_opy_ (u"ࠥࡘࡋࡥࡂࡖࡋࡏࡈࠧ᳇")):
        return {
            bstack11ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᳈"): bstack11ll_opy_ (u"ࠧࡇࡺࡶࡴࡨࠤࡈࡏࠢ᳉"),
            bstack11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᳊"): bstack11ll_opy_ (u"ࠢࡼࡿࡾࢁ࠴ࡥࡢࡶ࡫࡯ࡨ࠴ࡸࡥࡴࡷ࡯ࡸࡸࡅࡢࡶ࡫࡯ࡨࡎࡪ࠽ࡼࡿࠥ᳋").format(env.get(bstack11ll_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡌࡏࡖࡐࡇࡅ࡙ࡏࡏࡏࡕࡈࡖ࡛ࡋࡒࡖࡔࡌࠫ᳌")), env.get(bstack11ll_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡐࡓࡑࡍࡉࡈ࡚ࠧ᳍")), env.get(bstack11ll_opy_ (u"ࠪࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠪ᳎"))),
            bstack11ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᳏"): env.get(bstack11ll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠧ᳐")),
            bstack11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ᳑"): env.get(bstack11ll_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠢ᳒"))
        }
    if any([env.get(bstack11ll_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨ᳓")), env.get(bstack11ll_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡘࡅࡔࡑࡏ࡚ࡊࡊ࡟ࡔࡑࡘࡖࡈࡋ࡟ࡗࡇࡕࡗࡎࡕࡎ᳔ࠣ")), env.get(bstack11ll_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡓࡐࡗࡕࡇࡊࡥࡖࡆࡔࡖࡍࡔࡔ᳕ࠢ"))]):
        return {
            bstack11ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᳖"): bstack11ll_opy_ (u"ࠧࡇࡗࡔࠢࡆࡳࡩ࡫ࡂࡶ࡫࡯ࡨ᳗ࠧ"),
            bstack11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᳘"): env.get(bstack11ll_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡔ࡚ࡈࡌࡊࡅࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨ᳙")),
            bstack11ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᳚"): env.get(bstack11ll_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢ᳛")),
            bstack11ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᳜"): env.get(bstack11ll_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤ᳝"))
        }
    if env.get(bstack11ll_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡨࡵࡪ࡮ࡧࡒࡺࡳࡢࡦࡴ᳞ࠥ")):
        return {
            bstack11ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨ᳟ࠦ"): bstack11ll_opy_ (u"ࠢࡃࡣࡰࡦࡴࡵࠢ᳠"),
            bstack11ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ᳡"): env.get(bstack11ll_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡥࡹ࡮ࡲࡤࡓࡧࡶࡹࡱࡺࡳࡖࡴ࡯᳢ࠦ")),
            bstack11ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩ᳣ࠧ"): env.get(bstack11ll_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡸ࡮࡯ࡳࡶࡍࡳࡧࡔࡡ࡮ࡧ᳤ࠥ")),
            bstack11ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵ᳥ࠦ"): env.get(bstack11ll_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡢࡶ࡫࡯ࡨࡓࡻ࡭ࡣࡧࡵ᳦ࠦ"))
        }
    if env.get(bstack11ll_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒ᳧ࠣ")) or env.get(bstack11ll_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡐࡅࡎࡔ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡖࡘࡆࡘࡔࡆࡆ᳨ࠥ")):
        return {
            bstack11ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᳩ"): bstack11ll_opy_ (u"࡛ࠥࡪࡸࡣ࡬ࡧࡵࠦᳪ"),
            bstack11ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᳫ"): env.get(bstack11ll_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤᳬ")),
            bstack11ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥ᳭ࠣ"): bstack11ll_opy_ (u"ࠢࡎࡣ࡬ࡲࠥࡖࡩࡱࡧ࡯࡭ࡳ࡫ࠢᳮ") if env.get(bstack11ll_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡐࡅࡎࡔ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡖࡘࡆࡘࡔࡆࡆࠥᳯ")) else None,
            bstack11ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᳰ"): env.get(bstack11ll_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡌࡏࡔࡠࡅࡒࡑࡒࡏࡔࠣᳱ"))
        }
    if any([env.get(bstack11ll_opy_ (u"ࠦࡌࡉࡐࡠࡒࡕࡓࡏࡋࡃࡕࠤᳲ")), env.get(bstack11ll_opy_ (u"ࠧࡍࡃࡍࡑࡘࡈࡤࡖࡒࡐࡌࡈࡇ࡙ࠨᳳ")), env.get(bstack11ll_opy_ (u"ࠨࡇࡐࡑࡊࡐࡊࡥࡃࡍࡑࡘࡈࡤࡖࡒࡐࡌࡈࡇ࡙ࠨ᳴"))]):
        return {
            bstack11ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᳵ"): bstack11ll_opy_ (u"ࠣࡉࡲࡳ࡬ࡲࡥࠡࡅ࡯ࡳࡺࡪࠢᳶ"),
            bstack11ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ᳷"): None,
            bstack11ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ᳸"): env.get(bstack11ll_opy_ (u"ࠦࡕࡘࡏࡋࡇࡆࡘࡤࡏࡄࠣ᳹")),
            bstack11ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᳺ"): env.get(bstack11ll_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡏࡄࠣ᳻"))
        }
    if env.get(bstack11ll_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࠥ᳼")):
        return {
            bstack11ll_opy_ (u"ࠣࡰࡤࡱࡪࠨ᳽"): bstack11ll_opy_ (u"ࠤࡖ࡬࡮ࡶࡰࡢࡤ࡯ࡩࠧ᳾"),
            bstack11ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᳿"): env.get(bstack11ll_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᴀ")),
            bstack11ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᴁ"): bstack11ll_opy_ (u"ࠨࡊࡰࡤࠣࠧࢀࢃࠢᴂ").format(env.get(bstack11ll_opy_ (u"ࠧࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡎࡔࡈ࡟ࡊࡆࠪᴃ"))) if env.get(bstack11ll_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡏࡕࡂࡠࡋࡇࠦᴄ")) else None,
            bstack11ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᴅ"): env.get(bstack11ll_opy_ (u"ࠥࡗࡍࡏࡐࡑࡃࡅࡐࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᴆ"))
        }
    if bstack1lll1l1lll_opy_(env.get(bstack11ll_opy_ (u"ࠦࡓࡋࡔࡍࡋࡉ࡝ࠧᴇ"))):
        return {
            bstack11ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᴈ"): bstack11ll_opy_ (u"ࠨࡎࡦࡶ࡯࡭࡫ࡿࠢᴉ"),
            bstack11ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᴊ"): env.get(bstack11ll_opy_ (u"ࠣࡆࡈࡔࡑࡕ࡙ࡠࡗࡕࡐࠧᴋ")),
            bstack11ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᴌ"): env.get(bstack11ll_opy_ (u"ࠥࡗࡎ࡚ࡅࡠࡐࡄࡑࡊࠨᴍ")),
            bstack11ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᴎ"): env.get(bstack11ll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢᴏ"))
        }
    if bstack1lll1l1lll_opy_(env.get(bstack11ll_opy_ (u"ࠨࡇࡊࡖࡋ࡙ࡇࡥࡁࡄࡖࡌࡓࡓ࡙ࠢᴐ"))):
        return {
            bstack11ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᴑ"): bstack11ll_opy_ (u"ࠣࡉ࡬ࡸࡍࡻࡢࠡࡃࡦࡸ࡮ࡵ࡮ࡴࠤᴒ"),
            bstack11ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᴓ"): bstack11ll_opy_ (u"ࠥࡿࢂ࠵ࡻࡾ࠱ࡤࡧࡹ࡯࡯࡯ࡵ࠲ࡶࡺࡴࡳ࠰ࡽࢀࠦᴔ").format(env.get(bstack11ll_opy_ (u"ࠫࡌࡏࡔࡉࡗࡅࡣࡘࡋࡒࡗࡇࡕࡣ࡚ࡘࡌࠨᴕ")), env.get(bstack11ll_opy_ (u"ࠬࡍࡉࡕࡊࡘࡆࡤࡘࡅࡑࡑࡖࡍ࡙ࡕࡒ࡚ࠩᴖ")), env.get(bstack11ll_opy_ (u"࠭ࡇࡊࡖࡋ࡙ࡇࡥࡒࡖࡐࡢࡍࡉ࠭ᴗ"))),
            bstack11ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᴘ"): env.get(bstack11ll_opy_ (u"ࠣࡉࡌࡘࡍ࡛ࡂࡠ࡙ࡒࡖࡐࡌࡌࡐ࡙ࠥᴙ")),
            bstack11ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᴚ"): env.get(bstack11ll_opy_ (u"ࠥࡋࡎ࡚ࡈࡖࡄࡢࡖ࡚ࡔ࡟ࡊࡆࠥᴛ"))
        }
    if env.get(bstack11ll_opy_ (u"ࠦࡈࡏࠢᴜ")) == bstack11ll_opy_ (u"ࠧࡺࡲࡶࡧࠥᴝ") and env.get(bstack11ll_opy_ (u"ࠨࡖࡆࡔࡆࡉࡑࠨᴞ")) == bstack11ll_opy_ (u"ࠢ࠲ࠤᴟ"):
        return {
            bstack11ll_opy_ (u"ࠣࡰࡤࡱࡪࠨᴠ"): bstack11ll_opy_ (u"ࠤ࡙ࡩࡷࡩࡥ࡭ࠤᴡ"),
            bstack11ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᴢ"): bstack11ll_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࢀࢃࠢᴣ").format(env.get(bstack11ll_opy_ (u"ࠬ࡜ࡅࡓࡅࡈࡐࡤ࡛ࡒࡍࠩᴤ"))),
            bstack11ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᴥ"): None,
            bstack11ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᴦ"): None,
        }
    if env.get(bstack11ll_opy_ (u"ࠣࡖࡈࡅࡒࡉࡉࡕ࡛ࡢ࡚ࡊࡘࡓࡊࡑࡑࠦᴧ")):
        return {
            bstack11ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᴨ"): bstack11ll_opy_ (u"ࠥࡘࡪࡧ࡭ࡤ࡫ࡷࡽࠧᴩ"),
            bstack11ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᴪ"): None,
            bstack11ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᴫ"): env.get(bstack11ll_opy_ (u"ࠨࡔࡆࡃࡐࡇࡎ࡚࡙ࡠࡒࡕࡓࡏࡋࡃࡕࡡࡑࡅࡒࡋࠢᴬ")),
            bstack11ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᴭ"): env.get(bstack11ll_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᴮ"))
        }
    if any([env.get(bstack11ll_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࠧᴯ")), env.get(bstack11ll_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࡥࡕࡓࡎࠥᴰ")), env.get(bstack11ll_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠤᴱ")), env.get(bstack11ll_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࡠࡖࡈࡅࡒࠨᴲ"))]):
        return {
            bstack11ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᴳ"): bstack11ll_opy_ (u"ࠢࡄࡱࡱࡧࡴࡻࡲࡴࡧࠥᴴ"),
            bstack11ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᴵ"): None,
            bstack11ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᴶ"): env.get(bstack11ll_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᴷ")) or None,
            bstack11ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᴸ"): env.get(bstack11ll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢᴹ"), 0)
        }
    if env.get(bstack11ll_opy_ (u"ࠨࡇࡐࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᴺ")):
        return {
            bstack11ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᴻ"): bstack11ll_opy_ (u"ࠣࡉࡲࡇࡉࠨᴼ"),
            bstack11ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᴽ"): None,
            bstack11ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᴾ"): env.get(bstack11ll_opy_ (u"ࠦࡌࡕ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᴿ")),
            bstack11ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᵀ"): env.get(bstack11ll_opy_ (u"ࠨࡇࡐࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡈࡕࡕࡏࡖࡈࡖࠧᵁ"))
        }
    if env.get(bstack11ll_opy_ (u"ࠢࡄࡈࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᵂ")):
        return {
            bstack11ll_opy_ (u"ࠣࡰࡤࡱࡪࠨᵃ"): bstack11ll_opy_ (u"ࠤࡆࡳࡩ࡫ࡆࡳࡧࡶ࡬ࠧᵄ"),
            bstack11ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᵅ"): env.get(bstack11ll_opy_ (u"ࠦࡈࡌ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᵆ")),
            bstack11ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᵇ"): env.get(bstack11ll_opy_ (u"ࠨࡃࡇࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡓࡇࡍࡆࠤᵈ")),
            bstack11ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᵉ"): env.get(bstack11ll_opy_ (u"ࠣࡅࡉࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᵊ"))
        }
    return {bstack11ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᵋ"): None}
def get_host_info():
    return {
        bstack11ll_opy_ (u"ࠥ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠧᵌ"): platform.node(),
        bstack11ll_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࠨᵍ"): platform.system(),
        bstack11ll_opy_ (u"ࠧࡺࡹࡱࡧࠥᵎ"): platform.machine(),
        bstack11ll_opy_ (u"ࠨࡶࡦࡴࡶ࡭ࡴࡴࠢᵏ"): platform.version(),
        bstack11ll_opy_ (u"ࠢࡢࡴࡦ࡬ࠧᵐ"): platform.architecture()[0]
    }
def bstack11llll1l1l_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack1111lll11l1_opy_():
    if bstack1111l111_opy_.get_property(bstack11ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩᵑ")):
        return bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᵒ")
    return bstack11ll_opy_ (u"ࠪࡹࡳࡱ࡮ࡰࡹࡱࡣ࡬ࡸࡩࡥࠩᵓ")
def bstack1111l1lll11_opy_(driver):
    info = {
        bstack11ll_opy_ (u"ࠫࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪᵔ"): driver.capabilities,
        bstack11ll_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠩᵕ"): driver.session_id,
        bstack11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧᵖ"): driver.capabilities.get(bstack11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬᵗ"), None),
        bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪᵘ"): driver.capabilities.get(bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᵙ"), None),
        bstack11ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࠬᵚ"): driver.capabilities.get(bstack11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠪᵛ"), None),
        bstack11ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᵜ"):driver.capabilities.get(bstack11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᵝ"), None),
    }
    if bstack1111lll11l1_opy_() == bstack11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᵞ"):
        if bstack11ll11l11_opy_():
            info[bstack11ll_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࠩᵟ")] = bstack11ll_opy_ (u"ࠩࡤࡴࡵ࠳ࡡࡶࡶࡲࡱࡦࡺࡥࠨᵠ")
        elif driver.capabilities.get(bstack11ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᵡ"), {}).get(bstack11ll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨᵢ"), False):
            info[bstack11ll_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭ᵣ")] = bstack11ll_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪᵤ")
        else:
            info[bstack11ll_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࠨᵥ")] = bstack11ll_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪᵦ")
    return info
def bstack11ll11l11_opy_():
    if bstack1111l111_opy_.get_property(bstack11ll_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨᵧ")):
        return True
    if bstack1lll1l1lll_opy_(os.environ.get(bstack11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫᵨ"), None)):
        return True
    return False
def bstack1ll1l1lll_opy_(bstack1111l1llll1_opy_, url, data, config):
    headers = config.get(bstack11ll_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬᵩ"), None)
    proxies = bstack1l1lll1l1l_opy_(config, url)
    auth = config.get(bstack11ll_opy_ (u"ࠬࡧࡵࡵࡪࠪᵪ"), None)
    response = requests.request(
            bstack1111l1llll1_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1l11ll1ll1_opy_(bstack1l11l11111_opy_, size):
    bstack1l1l1ll111_opy_ = []
    while len(bstack1l11l11111_opy_) > size:
        bstack1l11lll1ll_opy_ = bstack1l11l11111_opy_[:size]
        bstack1l1l1ll111_opy_.append(bstack1l11lll1ll_opy_)
        bstack1l11l11111_opy_ = bstack1l11l11111_opy_[size:]
    bstack1l1l1ll111_opy_.append(bstack1l11l11111_opy_)
    return bstack1l1l1ll111_opy_
def bstack1111l1l1111_opy_(message, bstack111l1ll1lll_opy_=False):
    os.write(1, bytes(message, bstack11ll_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᵫ")))
    os.write(1, bytes(bstack11ll_opy_ (u"ࠧ࡝ࡰࠪᵬ"), bstack11ll_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧᵭ")))
    if bstack111l1ll1lll_opy_:
        with open(bstack11ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠯ࡲ࠵࠶ࡿ࠭ࠨᵮ") + os.environ[bstack11ll_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩᵯ")] + bstack11ll_opy_ (u"ࠫ࠳ࡲ࡯ࡨࠩᵰ"), bstack11ll_opy_ (u"ࠬࡧࠧᵱ")) as f:
            f.write(message + bstack11ll_opy_ (u"࠭࡜࡯ࠩᵲ"))
def bstack1lll1l1ll1l_opy_():
    return os.environ[bstack11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪᵳ")].lower() == bstack11ll_opy_ (u"ࠨࡶࡵࡹࡪ࠭ᵴ")
def bstack1lll1111_opy_():
    return bstack1l11llll_opy_().replace(tzinfo=None).isoformat() + bstack11ll_opy_ (u"ࠩ࡝ࠫᵵ")
def bstack111l111lll1_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack11ll_opy_ (u"ࠪ࡞ࠬᵶ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack11ll_opy_ (u"ࠫ࡟࠭ᵷ")))).total_seconds() * 1000
def bstack1111llll11l_opy_(timestamp):
    return bstack111l111l1l1_opy_(timestamp).isoformat() + bstack11ll_opy_ (u"ࠬࡠࠧᵸ")
def bstack1111l1ll11l_opy_(bstack111l1l11l1l_opy_):
    date_format = bstack11ll_opy_ (u"࡚࠭ࠥࠧࡰࠩࡩࠦࠥࡉ࠼ࠨࡑ࠿ࠫࡓ࠯ࠧࡩࠫᵹ")
    bstack1111llll1ll_opy_ = datetime.datetime.strptime(bstack111l1l11l1l_opy_, date_format)
    return bstack1111llll1ll_opy_.isoformat() + bstack11ll_opy_ (u"࡛ࠧࠩᵺ")
def bstack1111l1ll111_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack11ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᵻ")
    else:
        return bstack11ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᵼ")
def bstack1lll1l1lll_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack11ll_opy_ (u"ࠪࡸࡷࡻࡥࠨᵽ")
def bstack1111lll1ll1_opy_(val):
    return val.__str__().lower() == bstack11ll_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪᵾ")
def error_handler(bstack1111ll1lll1_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack1111ll1lll1_opy_ as e:
                print(bstack11ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࡻࡾࠢ࠰ࡂࠥࢁࡽ࠻ࠢࡾࢁࠧᵿ").format(func.__name__, bstack1111ll1lll1_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack1111l11lll1_opy_(bstack111l1l1l1ll_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack111l1l1l1ll_opy_(cls, *args, **kwargs)
            except bstack1111ll1lll1_opy_ as e:
                print(bstack11ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡼࡿࠣ࠱ࡃࠦࡻࡾ࠼ࠣࡿࢂࠨᶀ").format(bstack111l1l1l1ll_opy_.__name__, bstack1111ll1lll1_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack1111l11lll1_opy_
    else:
        return decorator
def bstack1ll11llll1_opy_(bstack1lll111l1_opy_):
    if os.getenv(bstack11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪᶁ")) is not None:
        return bstack1lll1l1lll_opy_(os.getenv(bstack11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫᶂ")))
    if bstack11ll_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᶃ") in bstack1lll111l1_opy_ and bstack1111lll1ll1_opy_(bstack1lll111l1_opy_[bstack11ll_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᶄ")]):
        return False
    if bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᶅ") in bstack1lll111l1_opy_ and bstack1111lll1ll1_opy_(bstack1lll111l1_opy_[bstack11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᶆ")]):
        return False
    return True
def bstack11l1llll1l_opy_():
    try:
        from pytest_bdd import reporting
        bstack111l11ll111_opy_ = os.environ.get(bstack11ll_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡛ࡓࡆࡔࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࠨᶇ"), None)
        return bstack111l11ll111_opy_ is None or bstack111l11ll111_opy_ == bstack11ll_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠦᶈ")
    except Exception as e:
        return False
def bstack1lll11lll1_opy_(hub_url, CONFIG):
    if bstack11l11l11l1_opy_() <= version.parse(bstack11ll_opy_ (u"ࠨ࠵࠱࠵࠸࠴࠰ࠨᶉ")):
        if hub_url:
            return bstack11ll_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥᶊ") + hub_url + bstack11ll_opy_ (u"ࠥ࠾࠽࠶࠯ࡸࡦ࠲࡬ࡺࡨࠢᶋ")
        return bstack1ll1ll111l_opy_
    if hub_url:
        return bstack11ll_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨᶌ") + hub_url + bstack11ll_opy_ (u"ࠧ࠵ࡷࡥ࠱࡫ࡹࡧࠨᶍ")
    return bstack1l111lll1l_opy_
def bstack1111ll1l1ll_opy_():
    return isinstance(os.getenv(bstack11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖ࡙ࡕࡇࡖࡘࡤࡖࡌࡖࡉࡌࡒࠬᶎ")), str)
def bstack11lll11l1_opy_(url):
    return urlparse(url).hostname
def bstack11llll11ll_opy_(hostname):
    for bstack1l111ll11l_opy_ in bstack1ll111ll1l_opy_:
        regex = re.compile(bstack1l111ll11l_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11ll11111l1_opy_(bstack111l1lll111_opy_, file_name, logger):
    bstack1l1ll1ll11_opy_ = os.path.join(os.path.expanduser(bstack11ll_opy_ (u"ࠧࡿࠩᶏ")), bstack111l1lll111_opy_)
    try:
        if not os.path.exists(bstack1l1ll1ll11_opy_):
            os.makedirs(bstack1l1ll1ll11_opy_)
        file_path = os.path.join(os.path.expanduser(bstack11ll_opy_ (u"ࠨࢀࠪᶐ")), bstack111l1lll111_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack11ll_opy_ (u"ࠩࡺࠫᶑ")):
                pass
            with open(file_path, bstack11ll_opy_ (u"ࠥࡻ࠰ࠨᶒ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack1l111ll1ll_opy_.format(str(e)))
def bstack11ll1111ll1_opy_(file_name, key, value, logger):
    file_path = bstack11ll11111l1_opy_(bstack11ll_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᶓ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1l111llll1_opy_ = json.load(open(file_path, bstack11ll_opy_ (u"ࠬࡸࡢࠨᶔ")))
        else:
            bstack1l111llll1_opy_ = {}
        bstack1l111llll1_opy_[key] = value
        with open(file_path, bstack11ll_opy_ (u"ࠨࡷࠬࠤᶕ")) as outfile:
            json.dump(bstack1l111llll1_opy_, outfile)
def bstack111111l111_opy_(file_name, logger):
    file_path = bstack11ll11111l1_opy_(bstack11ll_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᶖ"), file_name, logger)
    bstack1l111llll1_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack11ll_opy_ (u"ࠨࡴࠪᶗ")) as bstack11l1111ll1_opy_:
            bstack1l111llll1_opy_ = json.load(bstack11l1111ll1_opy_)
    return bstack1l111llll1_opy_
def bstack1ll111l1l1_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack11ll_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡩ࡫࡬ࡦࡶ࡬ࡲ࡬ࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ᶘ") + file_path + bstack11ll_opy_ (u"ࠪࠤࠬᶙ") + str(e))
def bstack11l11l11l1_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack11ll_opy_ (u"ࠦࡁࡔࡏࡕࡕࡈࡘࡃࠨᶚ")
def bstack1l11l1l1l_opy_(config):
    if bstack11ll_opy_ (u"ࠬ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫᶛ") in config:
        del (config[bstack11ll_opy_ (u"࠭ࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬᶜ")])
        return False
    if bstack11l11l11l1_opy_() < version.parse(bstack11ll_opy_ (u"ࠧ࠴࠰࠷࠲࠵࠭ᶝ")):
        return False
    if bstack11l11l11l1_opy_() >= version.parse(bstack11ll_opy_ (u"ࠨ࠶࠱࠵࠳࠻ࠧᶞ")):
        return True
    if bstack11ll_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩᶟ") in config and config[bstack11ll_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪᶠ")] is False:
        return False
    else:
        return True
def bstack1l11111111_opy_(args_list, bstack1111l1lll1l_opy_):
    index = -1
    for value in bstack1111l1lll1l_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
def bstack111l1ll1ll1_opy_(a, b):
  for k, v in b.items():
    if isinstance(v, dict) and k in a and isinstance(a[k], dict):
        bstack111l1ll1ll1_opy_(a[k], v)
    else:
        a[k] = v
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1l11l11l_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1l11l11l_opy_ = bstack1l11l11l_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack11ll_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᶡ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack11ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᶢ"), exception=exception)
    def bstack1111111ll1_opy_(self):
        if self.result != bstack11ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᶣ"):
            return None
        if isinstance(self.exception_type, str) and bstack11ll_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥᶤ") in self.exception_type:
            return bstack11ll_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠤᶥ")
        return bstack11ll_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥᶦ")
    def bstack111l11l1lll_opy_(self):
        if self.result != bstack11ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᶧ"):
            return None
        if self.bstack1l11l11l_opy_:
            return self.bstack1l11l11l_opy_
        return bstack111l11lll1l_opy_(self.exception)
def bstack111l11lll1l_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack1111l1lllll_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1l1l11l1_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1l1ll111l_opy_(config, logger):
    try:
        import playwright
        bstack111l1l11l11_opy_ = playwright.__file__
        bstack1111l11ll11_opy_ = os.path.split(bstack111l1l11l11_opy_)
        bstack111l11ll1l1_opy_ = bstack1111l11ll11_opy_[0] + bstack11ll_opy_ (u"ࠫ࠴ࡪࡲࡪࡸࡨࡶ࠴ࡶࡡࡤ࡭ࡤ࡫ࡪ࠵࡬ࡪࡤ࠲ࡧࡱ࡯࠯ࡤ࡮࡬࠲࡯ࡹࠧᶨ")
        os.environ[bstack11ll_opy_ (u"ࠬࡍࡌࡐࡄࡄࡐࡤࡇࡇࡆࡐࡗࡣࡍ࡚ࡔࡑࡡࡓࡖࡔ࡞࡙ࠨᶩ")] = bstack111lll1l1l_opy_(config)
        with open(bstack111l11ll1l1_opy_, bstack11ll_opy_ (u"࠭ࡲࠨᶪ")) as f:
            file_content = f.read()
            bstack111l1l1llll_opy_ = bstack11ll_opy_ (u"ࠧࡨ࡮ࡲࡦࡦࡲ࠭ࡢࡩࡨࡲࡹ࠭ᶫ")
            bstack111l1l11lll_opy_ = file_content.find(bstack111l1l1llll_opy_)
            if bstack111l1l11lll_opy_ == -1:
              process = subprocess.Popen(bstack11ll_opy_ (u"ࠣࡰࡳࡱࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡧ࡭ࡱࡥࡥࡱ࠳ࡡࡨࡧࡱࡸࠧᶬ"), shell=True, cwd=bstack1111l11ll11_opy_[0])
              process.wait()
              bstack1111l11l111_opy_ = bstack11ll_opy_ (u"ࠩࠥࡹࡸ࡫ࠠࡴࡶࡵ࡭ࡨࡺࠢ࠼ࠩᶭ")
              bstack1111l1l1l11_opy_ = bstack11ll_opy_ (u"ࠥࠦࠧࠦ࡜ࠣࡷࡶࡩࠥࡹࡴࡳ࡫ࡦࡸࡡࠨ࠻ࠡࡥࡲࡲࡸࡺࠠࡼࠢࡥࡳࡴࡺࡳࡵࡴࡤࡴࠥࢃࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࠫ࡬ࡲ࡯ࡣࡣ࡯࠱ࡦ࡭ࡥ࡯ࡶࠪ࠭ࡀࠦࡩࡧࠢࠫࡴࡷࡵࡣࡦࡵࡶ࠲ࡪࡴࡶ࠯ࡉࡏࡓࡇࡇࡌࡠࡃࡊࡉࡓ࡚࡟ࡉࡖࡗࡔࡤࡖࡒࡐ࡚࡜࠭ࠥࡨ࡯ࡰࡶࡶࡸࡷࡧࡰࠩࠫ࠾ࠤࠧࠨࠢᶮ")
              bstack1111ll11lll_opy_ = file_content.replace(bstack1111l11l111_opy_, bstack1111l1l1l11_opy_)
              with open(bstack111l11ll1l1_opy_, bstack11ll_opy_ (u"ࠫࡼ࠭ᶯ")) as f:
                f.write(bstack1111ll11lll_opy_)
    except Exception as e:
        logger.error(bstack11l1ll1ll1_opy_.format(str(e)))
def bstack1llll111l1_opy_():
  try:
    bstack1111ll1ll11_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll_opy_ (u"ࠬࡵࡰࡵ࡫ࡰࡥࡱࡥࡨࡶࡤࡢࡹࡷࡲ࠮࡫ࡵࡲࡲࠬᶰ"))
    bstack111l1ll11l1_opy_ = []
    if os.path.exists(bstack1111ll1ll11_opy_):
      with open(bstack1111ll1ll11_opy_) as f:
        bstack111l1ll11l1_opy_ = json.load(f)
      os.remove(bstack1111ll1ll11_opy_)
    return bstack111l1ll11l1_opy_
  except:
    pass
  return []
def bstack11111l1l1l_opy_(bstack1l111111l_opy_):
  try:
    bstack111l1ll11l1_opy_ = []
    bstack1111ll1ll11_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll_opy_ (u"࠭࡯ࡱࡶ࡬ࡱࡦࡲ࡟ࡩࡷࡥࡣࡺࡸ࡬࠯࡬ࡶࡳࡳ࠭ᶱ"))
    if os.path.exists(bstack1111ll1ll11_opy_):
      with open(bstack1111ll1ll11_opy_) as f:
        bstack111l1ll11l1_opy_ = json.load(f)
    bstack111l1ll11l1_opy_.append(bstack1l111111l_opy_)
    with open(bstack1111ll1ll11_opy_, bstack11ll_opy_ (u"ࠧࡸࠩᶲ")) as f:
        json.dump(bstack111l1ll11l1_opy_, f)
  except:
    pass
def bstack11111l111l_opy_(logger, bstack111l111ll1l_opy_ = False):
  try:
    test_name = os.environ.get(bstack11ll_opy_ (u"ࠨࡒ࡜ࡘࡊ࡙ࡔࡠࡖࡈࡗ࡙ࡥࡎࡂࡏࡈࠫᶳ"), bstack11ll_opy_ (u"ࠩࠪᶴ"))
    if test_name == bstack11ll_opy_ (u"ࠪࠫᶵ"):
        test_name = threading.current_thread().__dict__.get(bstack11ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡆࡩࡪ࡟ࡵࡧࡶࡸࡤࡴࡡ࡮ࡧࠪᶶ"), bstack11ll_opy_ (u"ࠬ࠭ᶷ"))
    bstack111l1l1ll11_opy_ = bstack11ll_opy_ (u"࠭ࠬࠡࠩᶸ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack111l111ll1l_opy_:
        bstack1lll111ll1_opy_ = os.environ.get(bstack11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧᶹ"), bstack11ll_opy_ (u"ࠨ࠲ࠪᶺ"))
        bstack1111l11ll_opy_ = {bstack11ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᶻ"): test_name, bstack11ll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᶼ"): bstack111l1l1ll11_opy_, bstack11ll_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪᶽ"): bstack1lll111ll1_opy_}
        bstack1111ll11l11_opy_ = []
        bstack1111lll111l_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡶࡰࡱࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫᶾ"))
        if os.path.exists(bstack1111lll111l_opy_):
            with open(bstack1111lll111l_opy_) as f:
                bstack1111ll11l11_opy_ = json.load(f)
        bstack1111ll11l11_opy_.append(bstack1111l11ll_opy_)
        with open(bstack1111lll111l_opy_, bstack11ll_opy_ (u"࠭ࡷࠨᶿ")) as f:
            json.dump(bstack1111ll11l11_opy_, f)
    else:
        bstack1111l11ll_opy_ = {bstack11ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ᷀"): test_name, bstack11ll_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ᷁"): bstack111l1l1ll11_opy_, bstack11ll_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ᷂"): str(multiprocessing.current_process().name)}
        if bstack11ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺࠧ᷃") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack1111l11ll_opy_)
  except Exception as e:
      logger.warn(bstack11ll_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡲࡶࡪࠦࡰࡺࡶࡨࡷࡹࠦࡦࡶࡰࡱࡩࡱࠦࡤࡢࡶࡤ࠾ࠥࢁࡽࠣ᷄").format(e))
def bstack11111llll_opy_(error_message, test_name, index, logger):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧ࡯ࡳࡨࡱࠠ࡯ࡱࡷࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠬࠡࡷࡶ࡭ࡳ࡭ࠠࡣࡣࡶ࡭ࡨࠦࡦࡪ࡮ࡨࠤࡴࡶࡥࡳࡣࡷ࡭ࡴࡴࡳࠨ᷅"))
    try:
      bstack1111l11l11l_opy_ = []
      bstack1111l11ll_opy_ = {bstack11ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ᷆"): test_name, bstack11ll_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭᷇"): error_message, bstack11ll_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧ᷈"): index}
      bstack111l111ll11_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll_opy_ (u"ࠩࡵࡳࡧࡵࡴࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪ᷉"))
      if os.path.exists(bstack111l111ll11_opy_):
          with open(bstack111l111ll11_opy_) as f:
              bstack1111l11l11l_opy_ = json.load(f)
      bstack1111l11l11l_opy_.append(bstack1111l11ll_opy_)
      with open(bstack111l111ll11_opy_, bstack11ll_opy_ (u"ࠪࡻ᷊ࠬ")) as f:
          json.dump(bstack1111l11l11l_opy_, f)
    except Exception as e:
      logger.warn(bstack11ll_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡲࡶࡪࠦࡲࡰࡤࡲࡸࠥ࡬ࡵ࡯ࡰࡨࡰࠥࡪࡡࡵࡣ࠽ࠤࢀࢃࠢ᷋").format(e))
    return
  bstack1111l11l11l_opy_ = []
  bstack1111l11ll_opy_ = {bstack11ll_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ᷌"): test_name, bstack11ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ᷍"): error_message, bstack11ll_opy_ (u"ࠧࡪࡰࡧࡩࡽ᷎࠭"): index}
  bstack111l111ll11_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll_opy_ (u"ࠨࡴࡲࡦࡴࡺ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯᷏ࠩ"))
  lock_file = bstack111l111ll11_opy_ + bstack11ll_opy_ (u"ࠩ࠱ࡰࡴࡩ࡫ࠨ᷐")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack111l111ll11_opy_):
          with open(bstack111l111ll11_opy_, bstack11ll_opy_ (u"ࠪࡶࠬ᷑")) as f:
              content = f.read().strip()
              if content:
                  bstack1111l11l11l_opy_ = json.load(open(bstack111l111ll11_opy_))
      bstack1111l11l11l_opy_.append(bstack1111l11ll_opy_)
      with open(bstack111l111ll11_opy_, bstack11ll_opy_ (u"ࠫࡼ࠭᷒")) as f:
          json.dump(bstack1111l11l11l_opy_, f)
  except Exception as e:
    logger.warn(bstack11ll_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡳࡷ࡫ࠠࡳࡱࡥࡳࡹࠦࡦࡶࡰࡱࡩࡱࠦࡤࡢࡶࡤࠤࡼ࡯ࡴࡩࠢࡩ࡭ࡱ࡫ࠠ࡭ࡱࡦ࡯࡮ࡴࡧ࠻ࠢࡾࢁࠧᷓ").format(e))
def bstack111ll11l11_opy_(bstack11111ll1l_opy_, name, logger):
  try:
    bstack1111l11ll_opy_ = {bstack11ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᷔ"): name, bstack11ll_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᷕ"): bstack11111ll1l_opy_, bstack11ll_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧᷖ"): str(threading.current_thread()._name)}
    return bstack1111l11ll_opy_
  except Exception as e:
    logger.warn(bstack11ll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡧ࡫ࡨࡢࡸࡨࠤ࡫ࡻ࡮࡯ࡧ࡯ࠤࡩࡧࡴࡢ࠼ࠣࡿࢂࠨᷗ").format(e))
  return
def bstack111l1111111_opy_():
    return platform.system() == bstack11ll_opy_ (u"࡛ࠪ࡮ࡴࡤࡰࡹࡶࠫᷘ")
def bstack11llllllll_opy_(bstack111l1ll1l11_opy_, config, logger):
    bstack111l111l1ll_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack111l1ll1l11_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack11ll_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫࡯ࡸࡪࡸࠠࡤࡱࡱࡪ࡮࡭ࠠ࡬ࡧࡼࡷࠥࡨࡹࠡࡴࡨ࡫ࡪࡾࠠ࡮ࡣࡷࡧ࡭ࡀࠠࡼࡿࠥᷙ").format(e))
    return bstack111l111l1ll_opy_
def bstack11l1l1l1lll_opy_(bstack1111ll11ll1_opy_, bstack1111l11llll_opy_):
    bstack111l11111ll_opy_ = version.parse(bstack1111ll11ll1_opy_)
    bstack111l11111l1_opy_ = version.parse(bstack1111l11llll_opy_)
    if bstack111l11111ll_opy_ > bstack111l11111l1_opy_:
        return 1
    elif bstack111l11111ll_opy_ < bstack111l11111l1_opy_:
        return -1
    else:
        return 0
def bstack1l11llll_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack111l111l1l1_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack1111ll111ll_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack1l11llll11_opy_(options, framework, config, bstack11lll1l1ll_opy_={}):
    if options is None:
        return
    if getattr(options, bstack11ll_opy_ (u"ࠬ࡭ࡥࡵࠩᷚ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack111lllll1_opy_ = caps.get(bstack11ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᷛ"))
    bstack1111lll11ll_opy_ = True
    bstack1ll1111lll_opy_ = os.environ[bstack11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬᷜ")]
    bstack1l1111l111l_opy_ = config.get(bstack11ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᷝ"), False)
    if bstack1l1111l111l_opy_:
        bstack1l1l1ll1l11_opy_ = config.get(bstack11ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩᷞ"), {})
        bstack1l1l1ll1l11_opy_[bstack11ll_opy_ (u"ࠪࡥࡺࡺࡨࡕࡱ࡮ࡩࡳ࠭ᷟ")] = os.getenv(bstack11ll_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩᷠ"))
        bstack111l11l1l1l_opy_ = json.loads(os.getenv(bstack11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭ᷡ"), bstack11ll_opy_ (u"࠭ࡻࡾࠩᷢ"))).get(bstack11ll_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᷣ"))
    if bstack1111lll1ll1_opy_(caps.get(bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡶࡵࡨ࡛࠸ࡉࠧᷤ"))) or bstack1111lll1ll1_opy_(caps.get(bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡷࡶࡩࡤࡽ࠳ࡤࠩᷥ"))):
        bstack1111lll11ll_opy_ = False
    if bstack1l11l1l1l_opy_({bstack11ll_opy_ (u"ࠥࡹࡸ࡫ࡗ࠴ࡅࠥᷦ"): bstack1111lll11ll_opy_}):
        bstack111lllll1_opy_ = bstack111lllll1_opy_ or {}
        bstack111lllll1_opy_[bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ᷧ")] = bstack1111ll111ll_opy_(framework)
        bstack111lllll1_opy_[bstack11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᷨ")] = bstack1lll1l1ll1l_opy_()
        bstack111lllll1_opy_[bstack11ll_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩᷩ")] = bstack1ll1111lll_opy_
        bstack111lllll1_opy_[bstack11ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩᷪ")] = bstack11lll1l1ll_opy_
        if bstack1l1111l111l_opy_:
            bstack111lllll1_opy_[bstack11ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᷫ")] = bstack1l1111l111l_opy_
            bstack111lllll1_opy_[bstack11ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩᷬ")] = bstack1l1l1ll1l11_opy_
            bstack111lllll1_opy_[bstack11ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᷭ")][bstack11ll_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᷮ")] = bstack111l11l1l1l_opy_
        if getattr(options, bstack11ll_opy_ (u"ࠬࡹࡥࡵࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸࡾ࠭ᷯ"), None):
            options.set_capability(bstack11ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᷰ"), bstack111lllll1_opy_)
        else:
            options[bstack11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᷱ")] = bstack111lllll1_opy_
    else:
        if getattr(options, bstack11ll_opy_ (u"ࠨࡵࡨࡸࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡺࠩᷲ"), None):
            options.set_capability(bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪᷳ"), bstack1111ll111ll_opy_(framework))
            options.set_capability(bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᷴ"), bstack1lll1l1ll1l_opy_())
            options.set_capability(bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭᷵"), bstack1ll1111lll_opy_)
            options.set_capability(bstack11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭᷶"), bstack11lll1l1ll_opy_)
            if bstack1l1111l111l_opy_:
                options.set_capability(bstack11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ᷷ࠬ"), bstack1l1111l111l_opy_)
                options.set_capability(bstack11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ᷸࠭"), bstack1l1l1ll1l11_opy_)
                options.set_capability(bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹ࠮ࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ᷹"), bstack111l11l1l1l_opy_)
        else:
            options[bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍ᷺ࠪ")] = bstack1111ll111ll_opy_(framework)
            options[bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ᷻")] = bstack1lll1l1ll1l_opy_()
            options[bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭᷼")] = bstack1ll1111lll_opy_
            options[bstack11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ᷽࠭")] = bstack11lll1l1ll_opy_
            if bstack1l1111l111l_opy_:
                options[bstack11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ᷾")] = bstack1l1111l111l_opy_
                options[bstack11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ᷿࠭")] = bstack1l1l1ll1l11_opy_
                options[bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧḀ")][bstack11ll_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪḁ")] = bstack111l11l1l1l_opy_
    return options
def bstack111l111l11l_opy_(ws_endpoint, framework):
    bstack11lll1l1ll_opy_ = bstack1111l111_opy_.get_property(bstack11ll_opy_ (u"ࠥࡔࡑࡇ࡙ࡘࡔࡌࡋࡍ࡚࡟ࡑࡔࡒࡈ࡚ࡉࡔࡠࡏࡄࡔࠧḂ"))
    if ws_endpoint and len(ws_endpoint.split(bstack11ll_opy_ (u"ࠫࡨࡧࡰࡴ࠿ࠪḃ"))) > 1:
        ws_url = ws_endpoint.split(bstack11ll_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫḄ"))[0]
        if bstack11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩḅ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack111l1ll111l_opy_ = json.loads(urllib.parse.unquote(ws_endpoint.split(bstack11ll_opy_ (u"ࠧࡤࡣࡳࡷࡂ࠭Ḇ"))[1]))
            bstack111l1ll111l_opy_ = bstack111l1ll111l_opy_ or {}
            bstack1ll1111lll_opy_ = os.environ[bstack11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ḇ")]
            bstack111l1ll111l_opy_[bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪḈ")] = str(framework) + str(__version__)
            bstack111l1ll111l_opy_[bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫḉ")] = bstack1lll1l1ll1l_opy_()
            bstack111l1ll111l_opy_[bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭Ḋ")] = bstack1ll1111lll_opy_
            bstack111l1ll111l_opy_[bstack11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ḋ")] = bstack11lll1l1ll_opy_
            ws_endpoint = ws_endpoint.split(bstack11ll_opy_ (u"࠭ࡣࡢࡲࡶࡁࠬḌ"))[0] + bstack11ll_opy_ (u"ࠧࡤࡣࡳࡷࡂ࠭ḍ") + urllib.parse.quote(json.dumps(bstack111l1ll111l_opy_))
    return ws_endpoint
def bstack1ll111l11_opy_():
    global bstack11lll1l11_opy_
    from playwright._impl._browser_type import BrowserType
    bstack11lll1l11_opy_ = BrowserType.connect
    return bstack11lll1l11_opy_
def bstack1l1l11ll1_opy_(framework_name):
    global bstack11l11l111l_opy_
    bstack11l11l111l_opy_ = framework_name
    return framework_name
def bstack1111ll1ll1_opy_(self, *args, **kwargs):
    global bstack11lll1l11_opy_
    try:
        global bstack11l11l111l_opy_
        if bstack11ll_opy_ (u"ࠨࡹࡶࡉࡳࡪࡰࡰ࡫ࡱࡸࠬḎ") in kwargs:
            kwargs[bstack11ll_opy_ (u"ࠩࡺࡷࡊࡴࡤࡱࡱ࡬ࡲࡹ࠭ḏ")] = bstack111l111l11l_opy_(
                kwargs.get(bstack11ll_opy_ (u"ࠪࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺࠧḐ"), None),
                bstack11l11l111l_opy_
            )
    except Exception as e:
        logger.error(bstack11ll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡫࡮ࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫࡙ࠥࡄࡌࠢࡦࡥࡵࡹ࠺ࠡࡽࢀࠦḑ").format(str(e)))
    return bstack11lll1l11_opy_(self, *args, **kwargs)
def bstack1111l11l1ll_opy_(bstack1111ll1111l_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack1l1lll1l1l_opy_(bstack1111ll1111l_opy_, bstack11ll_opy_ (u"ࠧࠨḒ"))
        if proxies and proxies.get(bstack11ll_opy_ (u"ࠨࡨࡵࡶࡳࡷࠧḓ")):
            parsed_url = urlparse(proxies.get(bstack11ll_opy_ (u"ࠢࡩࡶࡷࡴࡸࠨḔ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack11ll_opy_ (u"ࠨࡲࡵࡳࡽࡿࡈࡰࡵࡷࠫḕ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack11ll_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡱࡵࡸࠬḖ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack11ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࡗࡶࡩࡷ࠭ḗ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack11ll_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡥࡸࡹࠧḘ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack1l1lllll1_opy_(bstack1111ll1111l_opy_):
    bstack111l1l111ll_opy_ = {
        bstack11l1l11l111_opy_[bstack111l1l11111_opy_]: bstack1111ll1111l_opy_[bstack111l1l11111_opy_]
        for bstack111l1l11111_opy_ in bstack1111ll1111l_opy_
        if bstack111l1l11111_opy_ in bstack11l1l11l111_opy_
    }
    bstack111l1l111ll_opy_[bstack11ll_opy_ (u"ࠧࡶࡲࡰࡺࡼࡗࡪࡺࡴࡪࡰࡪࡷࠧḙ")] = bstack1111l11l1ll_opy_(bstack1111ll1111l_opy_, bstack1111l111_opy_.get_property(bstack11ll_opy_ (u"ࠨࡰࡳࡱࡻࡽࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸࠨḚ")))
    bstack111l11l11ll_opy_ = [element.lower() for element in bstack11l1l1l11l1_opy_]
    bstack111l11lll11_opy_(bstack111l1l111ll_opy_, bstack111l11l11ll_opy_)
    return bstack111l1l111ll_opy_
def bstack111l11lll11_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack11ll_opy_ (u"ࠢࠫࠬ࠭࠮ࠧḛ")
    for value in d.values():
        if isinstance(value, dict):
            bstack111l11lll11_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack111l11lll11_opy_(item, keys)
def bstack1ll11ll1l1l_opy_():
    bstack1111ll1l111_opy_ = [os.environ.get(bstack11ll_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡋࡏࡉࡘࡥࡄࡊࡔࠥḜ")), os.path.join(os.path.expanduser(bstack11ll_opy_ (u"ࠤࢁࠦḝ")), bstack11ll_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪḞ")), os.path.join(bstack11ll_opy_ (u"ࠫ࠴ࡺ࡭ࡱࠩḟ"), bstack11ll_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬḠ"))]
    for path in bstack1111ll1l111_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack11ll_opy_ (u"ࠨࡆࡪ࡮ࡨࠤࠬࠨḡ") + str(path) + bstack11ll_opy_ (u"ࠢࠨࠢࡨࡼ࡮ࡹࡴࡴ࠰ࠥḢ"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack11ll_opy_ (u"ࠣࡉ࡬ࡺ࡮ࡴࡧࠡࡲࡨࡶࡲ࡯ࡳࡴ࡫ࡲࡲࡸࠦࡦࡰࡴࠣࠫࠧḣ") + str(path) + bstack11ll_opy_ (u"ࠤࠪࠦḤ"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack11ll_opy_ (u"ࠥࡊ࡮ࡲࡥࠡࠩࠥḥ") + str(path) + bstack11ll_opy_ (u"ࠦࠬࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡩࡣࡶࠤࡹ࡮ࡥࠡࡴࡨࡵࡺ࡯ࡲࡦࡦࠣࡴࡪࡸ࡭ࡪࡵࡶ࡭ࡴࡴࡳ࠯ࠤḦ"))
            else:
                logger.debug(bstack11ll_opy_ (u"ࠧࡉࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡧ࡫࡯ࡩࠥ࠭ࠢḧ") + str(path) + bstack11ll_opy_ (u"ࠨࠧࠡࡹ࡬ࡸ࡭ࠦࡷࡳ࡫ࡷࡩࠥࡶࡥࡳ࡯࡬ࡷࡸ࡯࡯࡯࠰ࠥḨ"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack11ll_opy_ (u"ࠢࡐࡲࡨࡶࡦࡺࡩࡰࡰࠣࡷࡺࡩࡣࡦࡧࡧࡩࡩࠦࡦࡰࡴࠣࠫࠧḩ") + str(path) + bstack11ll_opy_ (u"ࠣࠩ࠱ࠦḪ"))
            return path
        except Exception as e:
            logger.debug(bstack11ll_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࠢࡸࡴࠥ࡬ࡩ࡭ࡧࠣࠫࢀࡶࡡࡵࡪࢀࠫ࠿ࠦࠢḫ") + str(e) + bstack11ll_opy_ (u"ࠥࠦḬ"))
    logger.debug(bstack11ll_opy_ (u"ࠦࡆࡲ࡬ࠡࡲࡤࡸ࡭ࡹࠠࡧࡣ࡬ࡰࡪࡪ࠮ࠣḭ"))
    return None
@measure(event_name=EVENTS.bstack11l1l11ll11_opy_, stage=STAGE.bstack1ll1111l1_opy_)
def bstack1l1l1l11111_opy_(binary_path, bstack1l1l1l111l1_opy_, bs_config):
    logger.debug(bstack11ll_opy_ (u"ࠧࡉࡵࡳࡴࡨࡲࡹࠦࡃࡍࡋࠣࡔࡦࡺࡨࠡࡨࡲࡹࡳࡪ࠺ࠡࡽࢀࠦḮ").format(binary_path))
    bstack111l11l1l11_opy_ = bstack11ll_opy_ (u"࠭ࠧḯ")
    bstack111l11ll1ll_opy_ = {
        bstack11ll_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬḰ"): __version__,
        bstack11ll_opy_ (u"ࠣࡱࡶࠦḱ"): platform.system(),
        bstack11ll_opy_ (u"ࠤࡲࡷࡤࡧࡲࡤࡪࠥḲ"): platform.machine(),
        bstack11ll_opy_ (u"ࠥࡧࡱ࡯࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣḳ"): bstack11ll_opy_ (u"ࠫ࠵࠭Ḵ"),
        bstack11ll_opy_ (u"ࠧࡹࡤ࡬ࡡ࡯ࡥࡳ࡭ࡵࡢࡩࡨࠦḵ"): bstack11ll_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭Ḷ")
    }
    bstack1111l111lll_opy_(bstack111l11ll1ll_opy_)
    try:
        if binary_path:
            bstack111l11ll1ll_opy_[bstack11ll_opy_ (u"ࠧࡤ࡮࡬ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬḷ")] = subprocess.check_output([binary_path, bstack11ll_opy_ (u"ࠣࡸࡨࡶࡸ࡯࡯࡯ࠤḸ")]).strip().decode(bstack11ll_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨḹ"))
        response = requests.request(
            bstack11ll_opy_ (u"ࠪࡋࡊ࡚ࠧḺ"),
            url=bstack1lll11l111_opy_(bstack11l11ll111l_opy_),
            headers=None,
            auth=(bs_config[bstack11ll_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ḻ")], bs_config[bstack11ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨḼ")]),
            json=None,
            params=bstack111l11ll1ll_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack11ll_opy_ (u"࠭ࡵࡳ࡮ࠪḽ") in data.keys() and bstack11ll_opy_ (u"ࠧࡶࡲࡧࡥࡹ࡫ࡤࡠࡥ࡯࡭ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭Ḿ") in data.keys():
            logger.debug(bstack11ll_opy_ (u"ࠣࡐࡨࡩࡩࠦࡴࡰࠢࡸࡴࡩࡧࡴࡦࠢࡥ࡭ࡳࡧࡲࡺ࠮ࠣࡧࡺࡸࡲࡦࡰࡷࠤࡧ࡯࡮ࡢࡴࡼࠤࡻ࡫ࡲࡴ࡫ࡲࡲ࠿ࠦࡻࡾࠤḿ").format(bstack111l11ll1ll_opy_[bstack11ll_opy_ (u"ࠩࡦࡰ࡮ࡥࡶࡦࡴࡶ࡭ࡴࡴࠧṀ")]))
            if bstack11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡘࡖࡑ࠭ṁ") in os.environ:
                logger.debug(bstack11ll_opy_ (u"ࠦࡘࡱࡩࡱࡲ࡬ࡲ࡬ࠦࡢࡪࡰࡤࡶࡾࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡣࡶࠤࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆࡎࡔࡁࡓ࡛ࡢ࡙ࡗࡒࠠࡪࡵࠣࡷࡪࡺࠢṂ"))
                data[bstack11ll_opy_ (u"ࠬࡻࡲ࡭ࠩṃ")] = os.environ[bstack11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡉࡏࡃࡕ࡝ࡤ࡛ࡒࡍࠩṄ")]
            bstack111l111llll_opy_ = bstack1111lll1l11_opy_(data[bstack11ll_opy_ (u"ࠧࡶࡴ࡯ࠫṅ")], bstack1l1l1l111l1_opy_)
            bstack111l11l1l11_opy_ = os.path.join(bstack1l1l1l111l1_opy_, bstack111l111llll_opy_)
            os.chmod(bstack111l11l1l11_opy_, 0o777) # bstack1111l1ll1ll_opy_ permission
            return bstack111l11l1l11_opy_
    except Exception as e:
        logger.debug(bstack11ll_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡤࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡳ࡫ࡷࠡࡕࡇࡏࠥࢁࡽࠣṆ").format(e))
    return binary_path
def bstack1111l111lll_opy_(bstack111l11ll1ll_opy_):
    try:
        if bstack11ll_opy_ (u"ࠩ࡯࡭ࡳࡻࡸࠨṇ") not in bstack111l11ll1ll_opy_[bstack11ll_opy_ (u"ࠪࡳࡸ࠭Ṉ")].lower():
            return
        if os.path.exists(bstack11ll_opy_ (u"ࠦ࠴࡫ࡴࡤ࠱ࡲࡷ࠲ࡸࡥ࡭ࡧࡤࡷࡪࠨṉ")):
            with open(bstack11ll_opy_ (u"ࠧ࠵ࡥࡵࡥ࠲ࡳࡸ࠳ࡲࡦ࡮ࡨࡥࡸ࡫ࠢṊ"), bstack11ll_opy_ (u"ࠨࡲࠣṋ")) as f:
                bstack111l1111l11_opy_ = {}
                for line in f:
                    if bstack11ll_opy_ (u"ࠢ࠾ࠤṌ") in line:
                        key, value = line.rstrip().split(bstack11ll_opy_ (u"ࠣ࠿ࠥṍ"), 1)
                        bstack111l1111l11_opy_[key] = value.strip(bstack11ll_opy_ (u"ࠩࠥࡠࠬ࠭Ṏ"))
                bstack111l11ll1ll_opy_[bstack11ll_opy_ (u"ࠪࡨ࡮ࡹࡴࡳࡱࠪṏ")] = bstack111l1111l11_opy_.get(bstack11ll_opy_ (u"ࠦࡎࡊࠢṐ"), bstack11ll_opy_ (u"ࠧࠨṑ"))
        elif os.path.exists(bstack11ll_opy_ (u"ࠨ࠯ࡦࡶࡦ࠳ࡦࡲࡰࡪࡰࡨ࠱ࡷ࡫࡬ࡦࡣࡶࡩࠧṒ")):
            bstack111l11ll1ll_opy_[bstack11ll_opy_ (u"ࠧࡥ࡫ࡶࡸࡷࡵࠧṓ")] = bstack11ll_opy_ (u"ࠨࡣ࡯ࡴ࡮ࡴࡥࠨṔ")
    except Exception as e:
        logger.debug(bstack11ll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡭ࡥࡵࠢࡧ࡭ࡸࡺࡲࡰࠢࡲࡪࠥࡲࡩ࡯ࡷࡻࠦṕ") + e)
@measure(event_name=EVENTS.bstack11l11l1l1l1_opy_, stage=STAGE.bstack1ll1111l1_opy_)
def bstack1111lll1l11_opy_(bstack111l1l1ll1l_opy_, bstack111l11l11l1_opy_):
    logger.debug(bstack11ll_opy_ (u"ࠥࡈࡴࡽ࡮࡭ࡱࡤࡨ࡮ࡴࡧࠡࡕࡇࡏࠥࡨࡩ࡯ࡣࡵࡽࠥ࡬ࡲࡰ࡯࠽ࠤࠧṖ") + str(bstack111l1l1ll1l_opy_) + bstack11ll_opy_ (u"ࠦࠧṗ"))
    zip_path = os.path.join(bstack111l11l11l1_opy_, bstack11ll_opy_ (u"ࠧࡪ࡯ࡸࡰ࡯ࡳࡦࡪࡥࡥࡡࡩ࡭ࡱ࡫࠮ࡻ࡫ࡳࠦṘ"))
    bstack111l111llll_opy_ = bstack11ll_opy_ (u"࠭ࠧṙ")
    with requests.get(bstack111l1l1ll1l_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack11ll_opy_ (u"ࠢࡸࡤࠥṚ")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack11ll_opy_ (u"ࠣࡈ࡬ࡰࡪࠦࡤࡰࡹࡱࡰࡴࡧࡤࡦࡦࠣࡷࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺ࠰ࠥṛ"))
    with zipfile.ZipFile(zip_path, bstack11ll_opy_ (u"ࠩࡵࠫṜ")) as zip_ref:
        bstack111l11l111l_opy_ = zip_ref.namelist()
        if len(bstack111l11l111l_opy_) > 0:
            bstack111l111llll_opy_ = bstack111l11l111l_opy_[0] # bstack1111l1l11ll_opy_ bstack11l11lll1l1_opy_ will be bstack1111l1l1ll1_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack111l11l11l1_opy_)
        logger.debug(bstack11ll_opy_ (u"ࠥࡊ࡮ࡲࡥࡴࠢࡶࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹࠡࡧࡻࡸࡷࡧࡣࡵࡧࡧࠤࡹࡵࠠࠨࠤṝ") + str(bstack111l11l11l1_opy_) + bstack11ll_opy_ (u"ࠦࠬࠨṞ"))
    os.remove(zip_path)
    return bstack111l111llll_opy_
def get_cli_dir():
    bstack111l111l111_opy_ = bstack1ll11ll1l1l_opy_()
    if bstack111l111l111_opy_:
        bstack1l1l1l111l1_opy_ = os.path.join(bstack111l111l111_opy_, bstack11ll_opy_ (u"ࠧࡩ࡬ࡪࠤṟ"))
        if not os.path.exists(bstack1l1l1l111l1_opy_):
            os.makedirs(bstack1l1l1l111l1_opy_, mode=0o777, exist_ok=True)
        return bstack1l1l1l111l1_opy_
    else:
        raise FileNotFoundError(bstack11ll_opy_ (u"ࠨࡎࡰࠢࡺࡶ࡮ࡺࡡࡣ࡮ࡨࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧࠣࡪࡴࡸࠠࡵࡪࡨࠤࡘࡊࡋࠡࡤ࡬ࡲࡦࡸࡹ࠯ࠤṠ"))
def bstack1l1l111ll11_opy_(bstack1l1l1l111l1_opy_):
    bstack11ll_opy_ (u"ࠢࠣࠤࡊࡩࡹࠦࡴࡩࡧࠣࡴࡦࡺࡨࠡࡨࡲࡶࠥࡺࡨࡦࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡕࡇࡏࠥࡨࡩ࡯ࡣࡵࡽࠥ࡯࡮ࠡࡣࠣࡻࡷ࡯ࡴࡢࡤ࡯ࡩࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹ࠯ࠤࠥࠦṡ")
    bstack1111l111ll1_opy_ = [
        os.path.join(bstack1l1l1l111l1_opy_, f)
        for f in os.listdir(bstack1l1l1l111l1_opy_)
        if os.path.isfile(os.path.join(bstack1l1l1l111l1_opy_, f)) and f.startswith(bstack11ll_opy_ (u"ࠣࡤ࡬ࡲࡦࡸࡹ࠮ࠤṢ"))
    ]
    if len(bstack1111l111ll1_opy_) > 0:
        return max(bstack1111l111ll1_opy_, key=os.path.getmtime) # get bstack1111llll1l1_opy_ binary
    return bstack11ll_opy_ (u"ࠤࠥṣ")
def bstack1111l1ll1l1_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l111l11111_opy_(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = bstack1l111l11111_opy_(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack111ll111l1_opy_(data, keys, default=None):
    bstack11ll_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡗࡦ࡬ࡥ࡭ࡻࠣ࡫ࡪࡺࠠࡢࠢࡱࡩࡸࡺࡥࡥࠢࡹࡥࡱࡻࡥࠡࡨࡵࡳࡲࠦࡡࠡࡦ࡬ࡧࡹ࡯࡯࡯ࡣࡵࡽࠥࡵࡲࠡ࡮࡬ࡷࡹ࠴ࠊࠡࠢࠣࠤ࠿ࡶࡡࡳࡣࡰࠤࡩࡧࡴࡢ࠼ࠣࡘ࡭࡫ࠠࡥ࡫ࡦࡸ࡮ࡵ࡮ࡢࡴࡼࠤࡴࡸࠠ࡭࡫ࡶࡸࠥࡺ࡯ࠡࡶࡵࡥࡻ࡫ࡲࡴࡧ࠱ࠎࠥࠦࠠࠡ࠼ࡳࡥࡷࡧ࡭ࠡ࡭ࡨࡽࡸࡀࠠࡂࠢ࡯࡭ࡸࡺࠠࡰࡨࠣ࡯ࡪࡿࡳ࠰࡫ࡱࡨ࡮ࡩࡥࡴࠢࡵࡩࡵࡸࡥࡴࡧࡱࡸ࡮ࡴࡧࠡࡶ࡫ࡩࠥࡶࡡࡵࡪ࠱ࠎࠥࠦࠠࠡ࠼ࡳࡥࡷࡧ࡭ࠡࡦࡨࡪࡦࡻ࡬ࡵ࠼࡚ࠣࡦࡲࡵࡦࠢࡷࡳࠥࡸࡥࡵࡷࡵࡲࠥ࡯ࡦࠡࡶ࡫ࡩࠥࡶࡡࡵࡪࠣࡨࡴ࡫ࡳࠡࡰࡲࡸࠥ࡫ࡸࡪࡵࡷ࠲ࠏࠦࠠࠡࠢ࠽ࡶࡪࡺࡵࡳࡰ࠽ࠤ࡙࡮ࡥࠡࡸࡤࡰࡺ࡫ࠠࡢࡶࠣࡸ࡭࡫ࠠ࡯ࡧࡶࡸࡪࡪࠠࡱࡣࡷ࡬࠱ࠦ࡯ࡳࠢࡧࡩ࡫ࡧࡵ࡭ࡶࠣ࡭࡫ࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥ࠰ࠍࠤࠥࠦࠠࠣࠤࠥṤ")
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