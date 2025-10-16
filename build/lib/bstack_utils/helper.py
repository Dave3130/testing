# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
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
from bstack_utils.constants import (bstack1ll1lll11_opy_, bstack11ll1ll1l_opy_, bstack1l1l1l1lll_opy_,
                                    bstack11l1l1l111l_opy_, bstack11l1l11llll_opy_, bstack11l1l11lll1_opy_, bstack11l1l1l1111_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack1l1l1111l_opy_, bstack1ll1ll11ll_opy_
from bstack_utils.proxy import bstack1111l1ll1l_opy_, bstack1l1llllll_opy_
from bstack_utils.constants import *
from bstack_utils import bstack111ll1l1l_opy_
from bstack_utils.bstack11llll111l_opy_ import bstack11lllll11_opy_
from browserstack_sdk._version import __version__
bstack1lll1ll1l_opy_ = Config.bstack1llll11ll_opy_()
logger = bstack111ll1l1l_opy_.get_logger(__name__, bstack111ll1l1l_opy_.bstack1l1ll111lll_opy_())
def bstack111l111lll1_opy_(config):
    return config[bstack1l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧᯍ")]
def bstack111l1l1l111_opy_(config):
    return config[bstack1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩᯎ")]
def bstack111l1ll11_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack111l11ll1l1_opy_(obj):
    values = []
    bstack1111l1l1ll1_opy_ = re.compile(bstack1l_opy_ (u"ࡲࠣࡠࡆ࡙ࡘ࡚ࡏࡎࡡࡗࡅࡌࡥ࡜ࡥ࠭ࠧࠦᯏ"), re.I)
    for key in obj.keys():
        if bstack1111l1l1ll1_opy_.match(key):
            values.append(obj[key])
    return values
def bstack1111ll1ll11_opy_(config):
    tags = []
    tags.extend(bstack111l11ll1l1_opy_(os.environ))
    tags.extend(bstack111l11ll1l1_opy_(config))
    return tags
def bstack1111ll1lll1_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack111l11111l1_opy_(bstack1111lllllll_opy_):
    if not bstack1111lllllll_opy_:
        return bstack1l_opy_ (u"ࠨࠩᯐ")
    return bstack1l_opy_ (u"ࠤࡾࢁࠥ࠮ࡻࡾࠫࠥᯑ").format(bstack1111lllllll_opy_.name, bstack1111lllllll_opy_.email)
def bstack111l1l1111l_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack111l11l1111_opy_ = repo.common_dir
        info = {
            bstack1l_opy_ (u"ࠥࡷ࡭ࡧࠢᯒ"): repo.head.commit.hexsha,
            bstack1l_opy_ (u"ࠦࡸ࡮࡯ࡳࡶࡢࡷ࡭ࡧࠢᯓ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack1l_opy_ (u"ࠧࡨࡲࡢࡰࡦ࡬ࠧᯔ"): repo.active_branch.name,
            bstack1l_opy_ (u"ࠨࡴࡢࡩࠥᯕ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack1l_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡴࡦࡴࠥᯖ"): bstack111l11111l1_opy_(repo.head.commit.committer),
            bstack1l_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡵࡧࡵࡣࡩࡧࡴࡦࠤᯗ"): repo.head.commit.committed_datetime.isoformat(),
            bstack1l_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࠤᯘ"): bstack111l11111l1_opy_(repo.head.commit.author),
            bstack1l_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࡢࡨࡦࡺࡥࠣᯙ"): repo.head.commit.authored_datetime.isoformat(),
            bstack1l_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡣࡲ࡫ࡳࡴࡣࡪࡩࠧᯚ"): repo.head.commit.message,
            bstack1l_opy_ (u"ࠧࡸ࡯ࡰࡶࠥᯛ"): repo.git.rev_parse(bstack1l_opy_ (u"ࠨ࠭࠮ࡵ࡫ࡳࡼ࠳ࡴࡰࡲ࡯ࡩࡻ࡫࡬ࠣᯜ")),
            bstack1l_opy_ (u"ࠢࡤࡱࡰࡱࡴࡴ࡟ࡨ࡫ࡷࡣࡩ࡯ࡲࠣᯝ"): bstack111l11l1111_opy_,
            bstack1l_opy_ (u"ࠣࡹࡲࡶࡰࡺࡲࡦࡧࡢ࡫࡮ࡺ࡟ࡥ࡫ࡵࠦᯞ"): subprocess.check_output([bstack1l_opy_ (u"ࠤࡪ࡭ࡹࠨᯟ"), bstack1l_opy_ (u"ࠥࡶࡪࡼ࠭ࡱࡣࡵࡷࡪࠨᯠ"), bstack1l_opy_ (u"ࠦ࠲࠳ࡧࡪࡶ࠰ࡧࡴࡳ࡭ࡰࡰ࠰ࡨ࡮ࡸࠢᯡ")]).strip().decode(
                bstack1l_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫᯢ")),
            bstack1l_opy_ (u"ࠨ࡬ࡢࡵࡷࡣࡹࡧࡧࠣᯣ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack1l_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡳࡠࡵ࡬ࡲࡨ࡫࡟࡭ࡣࡶࡸࡤࡺࡡࡨࠤᯤ"): repo.git.rev_list(
                bstack1l_opy_ (u"ࠣࡽࢀ࠲࠳ࢁࡽࠣᯥ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack1111lllll11_opy_ = []
        for remote in remotes:
            bstack1111l1l11ll_opy_ = {
                bstack1l_opy_ (u"ࠤࡱࡥࡲ࡫᯦ࠢ"): remote.name,
                bstack1l_opy_ (u"ࠥࡹࡷࡲࠢᯧ"): remote.url,
            }
            bstack1111lllll11_opy_.append(bstack1111l1l11ll_opy_)
        bstack111ll111l11_opy_ = {
            bstack1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᯨ"): bstack1l_opy_ (u"ࠧ࡭ࡩࡵࠤᯩ"),
            **info,
            bstack1l_opy_ (u"ࠨࡲࡦ࡯ࡲࡸࡪࡹࠢᯪ"): bstack1111lllll11_opy_
        }
        bstack111ll111l11_opy_ = bstack1111l1ll1ll_opy_(bstack111ll111l11_opy_)
        return bstack111ll111l11_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack1l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡰࡲࡸࡰࡦࡺࡩ࡯ࡩࠣࡋ࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࡀࠠࡼࡿࠥᯫ").format(err))
        return {}
def bstack11lll11111l_opy_(bstack1111llll1l1_opy_=None):
    bstack1l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡉࡨࡸࠥ࡭ࡩࡵࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤࡸࡶࡥࡤ࡫ࡩ࡭ࡨࡧ࡬࡭ࡻࠣࡪࡴࡸ࡭ࡢࡶࡷࡩࡩࠦࡦࡰࡴࠣࡅࡎࠦࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠢࡸࡷࡪࠦࡣࡢࡵࡨࡷࠥ࡬࡯ࡳࠢࡨࡥࡨ࡮ࠠࡧࡱ࡯ࡨࡪࡸࠠࡪࡰࠣࡸ࡭࡫ࠠ࡭࡫ࡶࡸ࠳ࠐࠠࠡࠢࠣࡅࡷ࡭ࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡪࡴࡲࡤࡦࡴࡶࠤ࠭ࡲࡩࡴࡶ࠯ࠤࡴࡶࡴࡪࡱࡱࡥࡱ࠯࠺ࠡࡎ࡬ࡷࡹࠦ࡯ࡧࠢࡩࡳࡱࡪࡥࡳࠢࡳࡥࡹ࡮ࡳࠡࡶࡲࠤࡪࡾࡴࡳࡣࡦࡸࠥ࡭ࡩࡵࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤ࡫ࡸ࡯࡮࠰ࠣࡈࡪ࡬ࡡࡶ࡮ࡷࡷࠥࡺ࡯ࠡ࡝ࡲࡷ࠳࡭ࡥࡵࡥࡺࡨ࠭࠯࡝࠯ࠌࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢ࡯࡭ࡸࡺ࠺ࠡࡎ࡬ࡷࡹࠦ࡯ࡧࠢࡧ࡭ࡨࡺࡳ࠭ࠢࡨࡥࡨ࡮ࠠࡤࡱࡱࡸࡦ࡯࡮ࡪࡰࡪࠤ࡬࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡪࡴࡸࠠࡢࠢࡩࡳࡱࡪࡥࡳ࠰ࠍࠤࠥࠦࠠࠣࠤࠥᯬ")
    if bstack1111llll1l1_opy_ == None: # bstack1111ll11l11_opy_ for bstack11lll11ll11_opy_-repo
        bstack1111llll1l1_opy_ = [os.getcwd()]
    results = []
    for folder in bstack1111llll1l1_opy_:
        try:
            repo = git.Repo(folder, search_parent_directories=True)
            result = {
                bstack1l_opy_ (u"ࠤࡳࡶࡎࡪࠢᯭ"): bstack1l_opy_ (u"ࠥࠦᯮ"),
                bstack1l_opy_ (u"ࠦ࡫࡯࡬ࡦࡵࡆ࡬ࡦࡴࡧࡦࡦࠥᯯ"): [],
                bstack1l_opy_ (u"ࠧࡧࡵࡵࡪࡲࡶࡸࠨᯰ"): [],
                bstack1l_opy_ (u"ࠨࡰࡳࡆࡤࡸࡪࠨᯱ"): bstack1l_opy_ (u"᯲ࠢࠣ"),
                bstack1l_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡎࡧࡶࡷࡦ࡭ࡥࡴࠤ᯳"): [],
                bstack1l_opy_ (u"ࠤࡳࡶ࡙࡯ࡴ࡭ࡧࠥ᯴"): bstack1l_opy_ (u"ࠥࠦ᯵"),
                bstack1l_opy_ (u"ࠦࡵࡸࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠦ᯶"): bstack1l_opy_ (u"ࠧࠨ᯷"),
                bstack1l_opy_ (u"ࠨࡰࡳࡔࡤࡻࡉ࡯ࡦࡧࠤ᯸"): bstack1l_opy_ (u"ࠢࠣ᯹")
            }
            bstack1111ll11111_opy_ = repo.active_branch.name
            bstack111l111ll11_opy_ = repo.head.commit
            result[bstack1l_opy_ (u"ࠣࡲࡵࡍࡩࠨ᯺")] = bstack111l111ll11_opy_.hexsha
            bstack111l1lll1l1_opy_ = _111l11l111l_opy_(repo)
            logger.debug(bstack1l_opy_ (u"ࠤࡅࡥࡸ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠࡧࡱࡵࠤࡨࡵ࡭ࡱࡣࡵ࡭ࡸࡵ࡮࠻ࠢࠥ᯻") + str(bstack111l1lll1l1_opy_) + bstack1l_opy_ (u"ࠥࠦ᯼"))
            if bstack111l1lll1l1_opy_:
                try:
                    bstack1111ll1111l_opy_ = repo.git.diff(bstack1l_opy_ (u"ࠦ࠲࠳࡮ࡢ࡯ࡨ࠱ࡴࡴ࡬ࡺࠤ᯽"), bstack1lll1ll1l1l_opy_ (u"ࠧࢁࡢࡢࡵࡨࡣࡧࡸࡡ࡯ࡥ࡫ࢁ࠳࠴࠮ࡼࡥࡸࡶࡷ࡫࡮ࡵࡡࡥࡶࡦࡴࡣࡩࡿࠥ᯾")).split(bstack1l_opy_ (u"࠭࡜࡯ࠩ᯿"))
                    logger.debug(bstack1l_opy_ (u"ࠢࡄࡪࡤࡲ࡬࡫ࡤࠡࡨ࡬ࡰࡪࡹࠠࡣࡧࡷࡻࡪ࡫࡮ࠡࡽࡥࡥࡸ࡫࡟ࡣࡴࡤࡲࡨ࡮ࡽࠡࡣࡱࡨࠥࢁࡣࡶࡴࡵࡩࡳࡺ࡟ࡣࡴࡤࡲࡨ࡮ࡽ࠻ࠢࠥᰀ") + str(bstack1111ll1111l_opy_) + bstack1l_opy_ (u"ࠣࠤᰁ"))
                    result[bstack1l_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡳࡄࡪࡤࡲ࡬࡫ࡤࠣᰂ")] = [f.strip() for f in bstack1111ll1111l_opy_ if f.strip()]
                    commits = list(repo.iter_commits(bstack1lll1ll1l1l_opy_ (u"ࠥࡿࡧࡧࡳࡦࡡࡥࡶࡦࡴࡣࡩࡿ࠱࠲ࢀࡩࡵࡳࡴࡨࡲࡹࡥࡢࡳࡣࡱࡧ࡭ࢃࠢᰃ")))
                except Exception:
                    logger.debug(bstack1l_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡨࡧࡷࠤࡨ࡮ࡡ࡯ࡩࡨࡨࠥ࡬ࡩ࡭ࡧࡶࠤ࡫ࡸ࡯࡮ࠢࡥࡶࡦࡴࡣࡩࠢࡦࡳࡲࡶࡡࡳ࡫ࡶࡳࡳ࠴ࠠࡇࡣ࡯ࡰ࡮ࡴࡧࠡࡤࡤࡧࡰࠦࡴࡰࠢࡵࡩࡨ࡫࡮ࡵࠢࡦࡳࡲࡳࡩࡵࡵ࠱ࠦᰄ"))
                    commits = list(repo.iter_commits(max_count=10))
                    if commits:
                        result[bstack1l_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡶࡇ࡭ࡧ࡮ࡨࡧࡧࠦᰅ")] = _1111ll11l1l_opy_(commits[:5])
            else:
                commits = list(repo.iter_commits(max_count=10))
                if commits:
                    result[bstack1l_opy_ (u"ࠨࡦࡪ࡮ࡨࡷࡈ࡮ࡡ࡯ࡩࡨࡨࠧᰆ")] = _1111ll11l1l_opy_(commits[:5])
            bstack111l1l1ll11_opy_ = set()
            bstack1111l1ll11l_opy_ = []
            for commit in commits:
                logger.debug(bstack1l_opy_ (u"ࠢࡑࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡨࡵ࡭࡮࡫ࡷ࠾ࠥࠨᰇ") + str(commit.message) + bstack1l_opy_ (u"ࠣࠤᰈ"))
                bstack111ll1111l1_opy_ = commit.author.name if commit.author else bstack1l_opy_ (u"ࠤࡘࡲࡰࡴ࡯ࡸࡰࠥᰉ")
                bstack111l1l1ll11_opy_.add(bstack111ll1111l1_opy_)
                bstack1111l1ll11l_opy_.append({
                    bstack1l_opy_ (u"ࠥࡱࡪࡹࡳࡢࡩࡨࠦᰊ"): commit.message.strip(),
                    bstack1l_opy_ (u"ࠦࡺࡹࡥࡳࠤᰋ"): bstack111ll1111l1_opy_
                })
            result[bstack1l_opy_ (u"ࠧࡧࡵࡵࡪࡲࡶࡸࠨᰌ")] = list(bstack111l1l1ll11_opy_)
            result[bstack1l_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡓࡥࡴࡵࡤ࡫ࡪࡹࠢᰍ")] = bstack1111l1ll11l_opy_
            result[bstack1l_opy_ (u"ࠢࡱࡴࡇࡥࡹ࡫ࠢᰎ")] = bstack111l111ll11_opy_.committed_datetime.strftime(bstack1l_opy_ (u"ࠣࠧ࡜࠱ࠪࡳ࠭ࠦࡦࠥᰏ"))
            if (not result[bstack1l_opy_ (u"ࠤࡳࡶ࡙࡯ࡴ࡭ࡧࠥᰐ")] or result[bstack1l_opy_ (u"ࠥࡴࡷ࡚ࡩࡵ࡮ࡨࠦᰑ")].strip() == bstack1l_opy_ (u"ࠦࠧᰒ")) and bstack111l111ll11_opy_.message:
                bstack111l11ll11l_opy_ = bstack111l111ll11_opy_.message.strip().splitlines()
                result[bstack1l_opy_ (u"ࠧࡶࡲࡕ࡫ࡷࡰࡪࠨᰓ")] = bstack111l11ll11l_opy_[0] if bstack111l11ll11l_opy_ else bstack1l_opy_ (u"ࠨࠢᰔ")
                if len(bstack111l11ll11l_opy_) > 2:
                    result[bstack1l_opy_ (u"ࠢࡱࡴࡇࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠢᰕ")] = bstack1l_opy_ (u"ࠨ࡞ࡱࠫᰖ").join(bstack111l11ll11l_opy_[2:]).strip()
            results.append(result)
        except Exception as err:
            logger.error(bstack1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡲࡴࡺࡲࡡࡵ࡫ࡱ࡫ࠥࡍࡩࡵࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤ࡫ࡵࡲࠡࡃࡌࠤࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠠࠩࡨࡲࡰࡩ࡫ࡲ࠻ࠢࡾࡪࡴࡲࡤࡦࡴࢀ࠭࠿ࠦࠢᰗ") + str(err) + bstack1l_opy_ (u"ࠥࠦᰘ"))
    filtered_results = [
        result
        for result in results
        if _1111lll1lll_opy_(result)
    ]
    return filtered_results
def _1111lll1lll_opy_(result):
    bstack1l_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡍ࡫࡬ࡱࡧࡵࠤࡹࡵࠠࡤࡪࡨࡧࡰࠦࡩࡧࠢࡤࠤ࡬࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡶࡪࡹࡵ࡭ࡶࠣ࡭ࡸࠦࡶࡢ࡮࡬ࡨࠥ࠮࡮ࡰࡰ࠰ࡩࡲࡶࡴࡺࠢࡩ࡭ࡱ࡫ࡳࡄࡪࡤࡲ࡬࡫ࡤࠡࡣࡱࡨࠥࡧࡵࡵࡪࡲࡶࡸ࠯࠮ࠋࠢࠣࠤࠥࠨࠢࠣᰙ")
    return (
        isinstance(result.get(bstack1l_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡶࡇ࡭ࡧ࡮ࡨࡧࡧࠦᰚ"), None), list)
        and len(result[bstack1l_opy_ (u"ࠨࡦࡪ࡮ࡨࡷࡈ࡮ࡡ࡯ࡩࡨࡨࠧᰛ")]) > 0
        and isinstance(result.get(bstack1l_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸࡳࠣᰜ"), None), list)
        and len(result[bstack1l_opy_ (u"ࠣࡣࡸࡸ࡭ࡵࡲࡴࠤᰝ")]) > 0
    )
def _111l11l111l_opy_(repo):
    bstack1l_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡗࡶࡾࠦࡴࡰࠢࡧࡩࡹ࡫ࡲ࡮࡫ࡱࡩࠥࡺࡨࡦࠢࡥࡥࡸ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡩ࡬ࡺࡪࡴࠠࡳࡧࡳࡳࠥࡽࡩࡵࡪࡲࡹࡹࠦࡨࡢࡴࡧࡧࡴࡪࡥࡥࠢࡱࡥࡲ࡫ࡳࠡࡣࡱࡨࠥࡽ࡯ࡳ࡭ࠣࡻ࡮ࡺࡨࠡࡣ࡯ࡰࠥ࡜ࡃࡔࠢࡳࡶࡴࡼࡩࡥࡧࡵࡷ࠳ࠐࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶࠤࡹ࡮ࡥࠡࡦࡨࡪࡦࡻ࡬ࡵࠢࡥࡶࡦࡴࡣࡩࠢ࡬ࡪࠥࡶ࡯ࡴࡵ࡬ࡦࡱ࡫ࠬࠡࡧ࡯ࡷࡪࠦࡎࡰࡰࡨ࠲ࠏࠦࠠࠡࠢࠥࠦࠧᰞ")
    try:
        try:
            origin = repo.remotes.origin
            bstack111l1l1llll_opy_ = origin.refs[bstack1l_opy_ (u"ࠪࡌࡊࡇࡄࠨᰟ")]
            target = bstack111l1l1llll_opy_.reference.name
            if target.startswith(bstack1l_opy_ (u"ࠫࡴࡸࡩࡨ࡫ࡱ࠳ࠬᰠ")):
                return target
        except Exception:
            pass
        if repo.remotes and repo.remotes.origin.refs:
            for ref in repo.remotes.origin.refs:
                if ref.name.startswith(bstack1l_opy_ (u"ࠬࡵࡲࡪࡩ࡬ࡲ࠴࠭ᰡ")):
                    return ref.name
        if repo.heads:
            return repo.heads[0].name
    except Exception:
        pass
    return None
def _1111ll11l1l_opy_(commits):
    bstack1l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡇࡦࡶࠣࡰ࡮ࡹࡴࠡࡱࡩࠤࡨ࡮ࡡ࡯ࡩࡨࡨࠥ࡬ࡩ࡭ࡧࡶࠤ࡫ࡸ࡯࡮ࠢࡤࠤࡱ࡯ࡳࡵࠢࡲࡪࠥࡩ࡯࡮࡯࡬ࡸࡸ࠴ࠊࠡࠢࠣࠤࠧࠨࠢᰢ")
    bstack1111ll1111l_opy_ = set()
    try:
        for commit in commits:
            if commit.parents:
                for parent in commit.parents:
                    diff = commit.diff(parent)
                    for bstack1111l1llll1_opy_ in diff:
                        if bstack1111l1llll1_opy_.a_path:
                            bstack1111ll1111l_opy_.add(bstack1111l1llll1_opy_.a_path)
                        if bstack1111l1llll1_opy_.b_path:
                            bstack1111ll1111l_opy_.add(bstack1111l1llll1_opy_.b_path)
    except Exception:
        pass
    return list(bstack1111ll1111l_opy_)
def bstack1111l1ll1ll_opy_(bstack111ll111l11_opy_):
    bstack111l1lll111_opy_ = bstack111l1ll11l1_opy_(bstack111ll111l11_opy_)
    if bstack111l1lll111_opy_ and bstack111l1lll111_opy_ > bstack11l1l1l111l_opy_:
        bstack111l111l11l_opy_ = bstack111l1lll111_opy_ - bstack11l1l1l111l_opy_
        bstack111l11ll111_opy_ = bstack111l1111lll_opy_(bstack111ll111l11_opy_[bstack1l_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠣᰣ")], bstack111l111l11l_opy_)
        bstack111ll111l11_opy_[bstack1l_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡠ࡯ࡨࡷࡸࡧࡧࡦࠤᰤ")] = bstack111l11ll111_opy_
        logger.info(bstack1l_opy_ (u"ࠤࡗ࡬ࡪࠦࡣࡰ࡯ࡰ࡭ࡹࠦࡨࡢࡵࠣࡦࡪ࡫࡮ࠡࡶࡵࡹࡳࡩࡡࡵࡧࡧ࠲࡙ࠥࡩࡻࡧࠣࡳ࡫ࠦࡣࡰ࡯ࡰ࡭ࡹࠦࡡࡧࡶࡨࡶࠥࡺࡲࡶࡰࡦࡥࡹ࡯࡯࡯ࠢ࡬ࡷࠥࢁࡽࠡࡍࡅࠦᰥ")
                    .format(bstack111l1ll11l1_opy_(bstack111ll111l11_opy_) / 1024))
    return bstack111ll111l11_opy_
def bstack111l1ll11l1_opy_(json_data):
    try:
        if json_data:
            bstack111l11lll11_opy_ = json.dumps(json_data)
            bstack111l1ll1lll_opy_ = sys.getsizeof(bstack111l11lll11_opy_)
            return bstack111l1ll1lll_opy_
    except Exception as e:
        logger.debug(bstack1l_opy_ (u"ࠥࡗࡴࡳࡥࡵࡪ࡬ࡲ࡬ࠦࡷࡦࡰࡷࠤࡼࡸ࡯࡯ࡩࠣࡻ࡭࡯࡬ࡦࠢࡦࡥࡱࡩࡵ࡭ࡣࡷ࡭ࡳ࡭ࠠࡴ࡫ࡽࡩࠥࡵࡦࠡࡌࡖࡓࡓࠦ࡯ࡣ࡬ࡨࡧࡹࡀࠠࡼࡿࠥᰦ").format(e))
    return -1
def bstack111l1111lll_opy_(field, bstack111l1llll1l_opy_):
    try:
        bstack111l1l11111_opy_ = len(bytes(bstack11l1l11llll_opy_, bstack1l_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᰧ")))
        bstack111l11111ll_opy_ = bytes(field, bstack1l_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫᰨ"))
        bstack111l1l1ll1l_opy_ = len(bstack111l11111ll_opy_)
        bstack111l111llll_opy_ = ceil(bstack111l1l1ll1l_opy_ - bstack111l1llll1l_opy_ - bstack111l1l11111_opy_)
        if bstack111l111llll_opy_ > 0:
            bstack1111llll111_opy_ = bstack111l11111ll_opy_[:bstack111l111llll_opy_].decode(bstack1l_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᰩ"), errors=bstack1l_opy_ (u"ࠧࡪࡩࡱࡳࡷ࡫ࠧᰪ")) + bstack11l1l11llll_opy_
            return bstack1111llll111_opy_
    except Exception as e:
        logger.debug(bstack1l_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡴࡳࡷࡱࡧࡦࡺࡩ࡯ࡩࠣࡪ࡮࡫࡬ࡥ࠮ࠣࡲࡴࡺࡨࡪࡰࡪࠤࡼࡧࡳࠡࡶࡵࡹࡳࡩࡡࡵࡧࡧࠤ࡭࡫ࡲࡦ࠼ࠣࡿࢂࠨᰫ").format(e))
    return field
def bstack11ll1111l_opy_():
    env = os.environ
    if (bstack1l_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢ࡙ࡗࡒࠢᰬ") in env and len(env[bstack1l_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣ࡚ࡘࡌࠣᰭ")]) > 0) or (
            bstack1l_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤࡎࡏࡎࡇࠥᰮ") in env and len(env[bstack1l_opy_ (u"ࠧࡐࡅࡏࡍࡌࡒࡘࡥࡈࡐࡏࡈࠦᰯ")]) > 0):
        return {
            bstack1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᰰ"): bstack1l_opy_ (u"ࠢࡋࡧࡱ࡯࡮ࡴࡳࠣᰱ"),
            bstack1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᰲ"): env.get(bstack1l_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧᰳ")),
            bstack1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᰴ"): env.get(bstack1l_opy_ (u"ࠦࡏࡕࡂࡠࡐࡄࡑࡊࠨᰵ")),
            bstack1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᰶ"): env.get(bstack1l_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖ᰷ࠧ"))
        }
    if env.get(bstack1l_opy_ (u"ࠢࡄࡋࠥ᰸")) == bstack1l_opy_ (u"ࠣࡶࡵࡹࡪࠨ᰹") and bstack1l11l1ll1l_opy_(env.get(bstack1l_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡅࡌࠦ᰺"))):
        return {
            bstack1l_opy_ (u"ࠥࡲࡦࡳࡥࠣ᰻"): bstack1l_opy_ (u"ࠦࡈ࡯ࡲࡤ࡮ࡨࡇࡎࠨ᰼"),
            bstack1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣ᰽"): env.get(bstack1l_opy_ (u"ࠨࡃࡊࡔࡆࡐࡊࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤ᰾")),
            bstack1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᰿"): env.get(bstack1l_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡠࡌࡒࡆࠧ᱀")),
            bstack1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᱁"): env.get(bstack1l_opy_ (u"ࠥࡇࡎࡘࡃࡍࡇࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࠨ᱂"))
        }
    if env.get(bstack1l_opy_ (u"ࠦࡈࡏࠢ᱃")) == bstack1l_opy_ (u"ࠧࡺࡲࡶࡧࠥ᱄") and bstack1l11l1ll1l_opy_(env.get(bstack1l_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࠨ᱅"))):
        return {
            bstack1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᱆"): bstack1l_opy_ (u"ࠣࡖࡵࡥࡻ࡯ࡳࠡࡅࡌࠦ᱇"),
            bstack1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ᱈"): env.get(bstack1l_opy_ (u"ࠥࡘࡗࡇࡖࡊࡕࡢࡆ࡚ࡏࡌࡅࡡ࡚ࡉࡇࡥࡕࡓࡎࠥ᱉")),
            bstack1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᱊"): env.get(bstack1l_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢ᱋")),
            bstack1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ᱌"): env.get(bstack1l_opy_ (u"ࠢࡕࡔࡄ࡚ࡎ࡙࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨᱍ"))
        }
    if env.get(bstack1l_opy_ (u"ࠣࡅࡌࠦᱎ")) == bstack1l_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᱏ") and env.get(bstack1l_opy_ (u"ࠥࡇࡎࡥࡎࡂࡏࡈࠦ᱐")) == bstack1l_opy_ (u"ࠦࡨࡵࡤࡦࡵ࡫࡭ࡵࠨ᱑"):
        return {
            bstack1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᱒"): bstack1l_opy_ (u"ࠨࡃࡰࡦࡨࡷ࡭࡯ࡰࠣ᱓"),
            bstack1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ᱔"): None,
            bstack1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᱕"): None,
            bstack1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᱖"): None
        }
    if env.get(bstack1l_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡂࡓࡃࡑࡇࡍࠨ᱗")) and env.get(bstack1l_opy_ (u"ࠦࡇࡏࡔࡃࡗࡆࡏࡊ࡚࡟ࡄࡑࡐࡑࡎ࡚ࠢ᱘")):
        return {
            bstack1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᱙"): bstack1l_opy_ (u"ࠨࡂࡪࡶࡥࡹࡨࡱࡥࡵࠤᱚ"),
            bstack1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᱛ"): env.get(bstack1l_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡌࡏࡔࡠࡊࡗࡘࡕࡥࡏࡓࡋࡊࡍࡓࠨᱜ")),
            bstack1l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᱝ"): None,
            bstack1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᱞ"): env.get(bstack1l_opy_ (u"ࠦࡇࡏࡔࡃࡗࡆࡏࡊ࡚࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨᱟ"))
        }
    if env.get(bstack1l_opy_ (u"ࠧࡉࡉࠣᱠ")) == bstack1l_opy_ (u"ࠨࡴࡳࡷࡨࠦᱡ") and bstack1l11l1ll1l_opy_(env.get(bstack1l_opy_ (u"ࠢࡅࡔࡒࡒࡊࠨᱢ"))):
        return {
            bstack1l_opy_ (u"ࠣࡰࡤࡱࡪࠨᱣ"): bstack1l_opy_ (u"ࠤࡇࡶࡴࡴࡥࠣᱤ"),
            bstack1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᱥ"): env.get(bstack1l_opy_ (u"ࠦࡉࡘࡏࡏࡇࡢࡆ࡚ࡏࡌࡅࡡࡏࡍࡓࡑࠢᱦ")),
            bstack1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᱧ"): None,
            bstack1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᱨ"): env.get(bstack1l_opy_ (u"ࠢࡅࡔࡒࡒࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᱩ"))
        }
    if env.get(bstack1l_opy_ (u"ࠣࡅࡌࠦᱪ")) == bstack1l_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᱫ") and bstack1l11l1ll1l_opy_(env.get(bstack1l_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࠨᱬ"))):
        return {
            bstack1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᱭ"): bstack1l_opy_ (u"࡙ࠧࡥ࡮ࡣࡳ࡬ࡴࡸࡥࠣᱮ"),
            bstack1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᱯ"): env.get(bstack1l_opy_ (u"ࠢࡔࡇࡐࡅࡕࡎࡏࡓࡇࡢࡓࡗࡍࡁࡏࡋ࡝ࡅ࡙ࡏࡏࡏࡡࡘࡖࡑࠨᱰ")),
            bstack1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᱱ"): env.get(bstack1l_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢᱲ")),
            bstack1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᱳ"): env.get(bstack1l_opy_ (u"ࠦࡘࡋࡍࡂࡒࡋࡓࡗࡋ࡟ࡋࡑࡅࡣࡎࡊࠢᱴ"))
        }
    if env.get(bstack1l_opy_ (u"ࠧࡉࡉࠣᱵ")) == bstack1l_opy_ (u"ࠨࡴࡳࡷࡨࠦᱶ") and bstack1l11l1ll1l_opy_(env.get(bstack1l_opy_ (u"ࠢࡈࡋࡗࡐࡆࡈ࡟ࡄࡋࠥᱷ"))):
        return {
            bstack1l_opy_ (u"ࠣࡰࡤࡱࡪࠨᱸ"): bstack1l_opy_ (u"ࠤࡊ࡭ࡹࡒࡡࡣࠤᱹ"),
            bstack1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᱺ"): env.get(bstack1l_opy_ (u"ࠦࡈࡏ࡟ࡋࡑࡅࡣ࡚ࡘࡌࠣᱻ")),
            bstack1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᱼ"): env.get(bstack1l_opy_ (u"ࠨࡃࡊࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᱽ")),
            bstack1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᱾"): env.get(bstack1l_opy_ (u"ࠣࡅࡌࡣࡏࡕࡂࡠࡋࡇࠦ᱿"))
        }
    if env.get(bstack1l_opy_ (u"ࠤࡆࡍࠧᲀ")) == bstack1l_opy_ (u"ࠥࡸࡷࡻࡥࠣᲁ") and bstack1l11l1ll1l_opy_(env.get(bstack1l_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋࠢᲂ"))):
        return {
            bstack1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᲃ"): bstack1l_opy_ (u"ࠨࡂࡶ࡫࡯ࡨࡰ࡯ࡴࡦࠤᲄ"),
            bstack1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᲅ"): env.get(bstack1l_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢᲆ")),
            bstack1l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᲇ"): env.get(bstack1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡌࡂࡄࡈࡐࠧᲈ")) or env.get(bstack1l_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡑࡅࡒࡋࠢᲉ")),
            bstack1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᲊ"): env.get(bstack1l_opy_ (u"ࠨࡂࡖࡋࡏࡈࡐࡏࡔࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣ᲋"))
        }
    if bstack1l11l1ll1l_opy_(env.get(bstack1l_opy_ (u"ࠢࡕࡈࡢࡆ࡚ࡏࡌࡅࠤ᲌"))):
        return {
            bstack1l_opy_ (u"ࠣࡰࡤࡱࡪࠨ᲍"): bstack1l_opy_ (u"ࠤ࡙࡭ࡸࡻࡡ࡭ࠢࡖࡸࡺࡪࡩࡰࠢࡗࡩࡦࡳࠠࡔࡧࡵࡺ࡮ࡩࡥࡴࠤ᲎"),
            bstack1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᲏"): bstack1l_opy_ (u"ࠦࢀࢃࡻࡾࠤᲐ").format(env.get(bstack1l_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡉࡓ࡚ࡔࡄࡂࡖࡌࡓࡓ࡙ࡅࡓࡘࡈࡖ࡚ࡘࡉࠨᲑ")), env.get(bstack1l_opy_ (u"࠭ࡓ࡚ࡕࡗࡉࡒࡥࡔࡆࡃࡐࡔࡗࡕࡊࡆࡅࡗࡍࡉ࠭Გ"))),
            bstack1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᲓ"): env.get(bstack1l_opy_ (u"ࠣࡕ࡜ࡗ࡙ࡋࡍࡠࡆࡈࡊࡎࡔࡉࡕࡋࡒࡒࡎࡊࠢᲔ")),
            bstack1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᲕ"): env.get(bstack1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠥᲖ"))
        }
    if bstack1l11l1ll1l_opy_(env.get(bstack1l_opy_ (u"ࠦࡆࡖࡐࡗࡇ࡜ࡓࡗࠨᲗ"))):
        return {
            bstack1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᲘ"): bstack1l_opy_ (u"ࠨࡁࡱࡲࡹࡩࡾࡵࡲࠣᲙ"),
            bstack1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᲚ"): bstack1l_opy_ (u"ࠣࡽࢀ࠳ࡵࡸ࡯࡫ࡧࡦࡸ࠴ࢁࡽ࠰ࡽࢀ࠳ࡧࡻࡩ࡭ࡦࡶ࠳ࢀࢃࠢᲛ").format(env.get(bstack1l_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣ࡚ࡘࡌࠨᲜ")), env.get(bstack1l_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡇࡃࡄࡑࡘࡒ࡙ࡥࡎࡂࡏࡈࠫᲝ")), env.get(bstack1l_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡐࡓࡑࡍࡉࡈ࡚࡟ࡔࡎࡘࡋࠬᲞ")), env.get(bstack1l_opy_ (u"ࠬࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩᲟ"))),
            bstack1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᲠ"): env.get(bstack1l_opy_ (u"ࠢࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᲡ")),
            bstack1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᲢ"): env.get(bstack1l_opy_ (u"ࠤࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᲣ"))
        }
    if env.get(bstack1l_opy_ (u"ࠥࡅ࡟࡛ࡒࡆࡡࡋࡘ࡙ࡖ࡟ࡖࡕࡈࡖࡤࡇࡇࡆࡐࡗࠦᲤ")) and env.get(bstack1l_opy_ (u"࡙ࠦࡌ࡟ࡃࡗࡌࡐࡉࠨᲥ")):
        return {
            bstack1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᲦ"): bstack1l_opy_ (u"ࠨࡁࡻࡷࡵࡩࠥࡉࡉࠣᲧ"),
            bstack1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᲨ"): bstack1l_opy_ (u"ࠣࡽࢀࡿࢂ࠵࡟ࡣࡷ࡬ࡰࡩ࠵ࡲࡦࡵࡸࡰࡹࡹ࠿ࡣࡷ࡬ࡰࡩࡏࡤ࠾ࡽࢀࠦᲩ").format(env.get(bstack1l_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡆࡐࡗࡑࡈࡆ࡚ࡉࡐࡐࡖࡉࡗ࡜ࡅࡓࡗࡕࡍࠬᲪ")), env.get(bstack1l_opy_ (u"ࠪࡗ࡞࡙ࡔࡆࡏࡢࡘࡊࡇࡍࡑࡔࡒࡎࡊࡉࡔࠨᲫ")), env.get(bstack1l_opy_ (u"ࠫࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡋࡇࠫᲬ"))),
            bstack1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᲭ"): env.get(bstack1l_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡍࡉࠨᲮ")),
            bstack1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᲯ"): env.get(bstack1l_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡏࡄࠣᲰ"))
        }
    if any([env.get(bstack1l_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢᲱ")), env.get(bstack1l_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡒࡆࡕࡒࡐ࡛ࡋࡄࡠࡕࡒ࡙ࡗࡉࡅࡠࡘࡈࡖࡘࡏࡏࡏࠤᲲ")), env.get(bstack1l_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡔࡑࡘࡖࡈࡋ࡟ࡗࡇࡕࡗࡎࡕࡎࠣᲳ"))]):
        return {
            bstack1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᲴ"): bstack1l_opy_ (u"ࠨࡁࡘࡕࠣࡇࡴࡪࡥࡃࡷ࡬ࡰࡩࠨᲵ"),
            bstack1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᲶ"): env.get(bstack1l_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡕ࡛ࡂࡍࡋࡆࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢᲷ")),
            bstack1l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᲸ"): env.get(bstack1l_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠣᲹ")),
            bstack1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᲺ"): env.get(bstack1l_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥ᲻"))
        }
    if env.get(bstack1l_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡢࡶ࡫࡯ࡨࡓࡻ࡭ࡣࡧࡵࠦ᲼")):
        return {
            bstack1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᲽ"): bstack1l_opy_ (u"ࠣࡄࡤࡱࡧࡵ࡯ࠣᲾ"),
            bstack1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᲿ"): env.get(bstack1l_opy_ (u"ࠥࡦࡦࡳࡢࡰࡱࡢࡦࡺ࡯࡬ࡥࡔࡨࡷࡺࡲࡴࡴࡗࡵࡰࠧ᳀")),
            bstack1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᳁"): env.get(bstack1l_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡹࡨࡰࡴࡷࡎࡴࡨࡎࡢ࡯ࡨࠦ᳂")),
            bstack1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ᳃"): env.get(bstack1l_opy_ (u"ࠢࡣࡣࡰࡦࡴࡵ࡟ࡣࡷ࡬ࡰࡩࡔࡵ࡮ࡤࡨࡶࠧ᳄"))
        }
    if env.get(bstack1l_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࠤ᳅")) or env.get(bstack1l_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࡢࡑࡆࡏࡎࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡗ࡙ࡇࡒࡕࡇࡇࠦ᳆")):
        return {
            bstack1l_opy_ (u"ࠥࡲࡦࡳࡥࠣ᳇"): bstack1l_opy_ (u"ࠦ࡜࡫ࡲࡤ࡭ࡨࡶࠧ᳈"),
            bstack1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣ᳉"): env.get(bstack1l_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥ᳊")),
            bstack1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᳋"): bstack1l_opy_ (u"ࠣࡏࡤ࡭ࡳࠦࡐࡪࡲࡨࡰ࡮ࡴࡥࠣ᳌") if env.get(bstack1l_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࡢࡑࡆࡏࡎࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡗ࡙ࡇࡒࡕࡇࡇࠦ᳍")) else None,
            bstack1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᳎"): env.get(bstack1l_opy_ (u"ࠦ࡜ࡋࡒࡄࡍࡈࡖࡤࡍࡉࡕࡡࡆࡓࡒࡓࡉࡕࠤ᳏"))
        }
    if any([env.get(bstack1l_opy_ (u"ࠧࡍࡃࡑࡡࡓࡖࡔࡐࡅࡄࡖࠥ᳐")), env.get(bstack1l_opy_ (u"ࠨࡇࡄࡎࡒ࡙ࡉࡥࡐࡓࡑࡍࡉࡈ࡚ࠢ᳑")), env.get(bstack1l_opy_ (u"ࠢࡈࡑࡒࡋࡑࡋ࡟ࡄࡎࡒ࡙ࡉࡥࡐࡓࡑࡍࡉࡈ࡚ࠢ᳒"))]):
        return {
            bstack1l_opy_ (u"ࠣࡰࡤࡱࡪࠨ᳓"): bstack1l_opy_ (u"ࠤࡊࡳࡴ࡭࡬ࡦࠢࡆࡰࡴࡻࡤ᳔ࠣ"),
            bstack1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᳕"): None,
            bstack1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᳖"): env.get(bstack1l_opy_ (u"ࠧࡖࡒࡐࡌࡈࡇ࡙ࡥࡉࡅࠤ᳗")),
            bstack1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶ᳘ࠧ"): env.get(bstack1l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡉࡅࠤ᳙"))
        }
    if env.get(bstack1l_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࠦ᳚")):
        return {
            bstack1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᳛"): bstack1l_opy_ (u"ࠥࡗ࡭࡯ࡰࡱࡣࡥࡰࡪࠨ᳜"),
            bstack1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲ᳝ࠢ"): env.get(bstack1l_opy_ (u"࡙ࠧࡈࡊࡒࡓࡅࡇࡒࡅࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏ᳞ࠦ")),
            bstack1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥ᳟ࠣ"): bstack1l_opy_ (u"ࠢࡋࡱࡥࠤࠨࢁࡽࠣ᳠").format(env.get(bstack1l_opy_ (u"ࠨࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡏࡕࡂࡠࡋࡇࠫ᳡"))) if env.get(bstack1l_opy_ (u"ࠤࡖࡌࡎࡖࡐࡂࡄࡏࡉࡤࡐࡏࡃࡡࡌࡈ᳢ࠧ")) else None,
            bstack1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᳣"): env.get(bstack1l_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨ᳤"))
        }
    if bstack1l11l1ll1l_opy_(env.get(bstack1l_opy_ (u"ࠧࡔࡅࡕࡎࡌࡊ࡞ࠨ᳥"))):
        return {
            bstack1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨ᳦ࠦ"): bstack1l_opy_ (u"ࠢࡏࡧࡷࡰ࡮࡬ࡹ᳧ࠣ"),
            bstack1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯᳨ࠦ"): env.get(bstack1l_opy_ (u"ࠤࡇࡉࡕࡒࡏ࡚ࡡࡘࡖࡑࠨᳩ")),
            bstack1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᳪ"): env.get(bstack1l_opy_ (u"ࠦࡘࡏࡔࡆࡡࡑࡅࡒࡋࠢᳫ")),
            bstack1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᳬ"): env.get(bstack1l_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡏࡄ᳭ࠣ"))
        }
    if bstack1l11l1ll1l_opy_(env.get(bstack1l_opy_ (u"ࠢࡈࡋࡗࡌ࡚ࡈ࡟ࡂࡅࡗࡍࡔࡔࡓࠣᳮ"))):
        return {
            bstack1l_opy_ (u"ࠣࡰࡤࡱࡪࠨᳯ"): bstack1l_opy_ (u"ࠤࡊ࡭ࡹࡎࡵࡣࠢࡄࡧࡹ࡯࡯࡯ࡵࠥᳰ"),
            bstack1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᳱ"): bstack1l_opy_ (u"ࠦࢀࢃ࠯ࡼࡿ࠲ࡥࡨࡺࡩࡰࡰࡶ࠳ࡷࡻ࡮ࡴ࠱ࡾࢁࠧᳲ").format(env.get(bstack1l_opy_ (u"ࠬࡍࡉࡕࡊࡘࡆࡤ࡙ࡅࡓࡘࡈࡖࡤ࡛ࡒࡍࠩᳳ")), env.get(bstack1l_opy_ (u"࠭ࡇࡊࡖࡋ࡙ࡇࡥࡒࡆࡒࡒࡗࡎ࡚ࡏࡓ࡛ࠪ᳴")), env.get(bstack1l_opy_ (u"ࠧࡈࡋࡗࡌ࡚ࡈ࡟ࡓࡗࡑࡣࡎࡊࠧᳵ"))),
            bstack1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᳶ"): env.get(bstack1l_opy_ (u"ࠤࡊࡍ࡙ࡎࡕࡃࡡ࡚ࡓࡗࡑࡆࡍࡑ࡚ࠦ᳷")),
            bstack1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᳸"): env.get(bstack1l_opy_ (u"ࠦࡌࡏࡔࡉࡗࡅࡣࡗ࡛ࡎࡠࡋࡇࠦ᳹"))
        }
    if env.get(bstack1l_opy_ (u"ࠧࡉࡉࠣᳺ")) == bstack1l_opy_ (u"ࠨࡴࡳࡷࡨࠦ᳻") and env.get(bstack1l_opy_ (u"ࠢࡗࡇࡕࡇࡊࡒࠢ᳼")) == bstack1l_opy_ (u"ࠣ࠳ࠥ᳽"):
        return {
            bstack1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᳾"): bstack1l_opy_ (u"࡚ࠥࡪࡸࡣࡦ࡮ࠥ᳿"),
            bstack1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᴀ"): bstack1l_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࢁࡽࠣᴁ").format(env.get(bstack1l_opy_ (u"࠭ࡖࡆࡔࡆࡉࡑࡥࡕࡓࡎࠪᴂ"))),
            bstack1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᴃ"): None,
            bstack1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᴄ"): None,
        }
    if env.get(bstack1l_opy_ (u"ࠤࡗࡉࡆࡓࡃࡊࡖ࡜ࡣ࡛ࡋࡒࡔࡋࡒࡒࠧᴅ")):
        return {
            bstack1l_opy_ (u"ࠥࡲࡦࡳࡥࠣᴆ"): bstack1l_opy_ (u"࡙ࠦ࡫ࡡ࡮ࡥ࡬ࡸࡾࠨᴇ"),
            bstack1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᴈ"): None,
            bstack1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᴉ"): env.get(bstack1l_opy_ (u"ࠢࡕࡇࡄࡑࡈࡏࡔ࡚ࡡࡓࡖࡔࡐࡅࡄࡖࡢࡒࡆࡓࡅࠣᴊ")),
            bstack1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᴋ"): env.get(bstack1l_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣᴌ"))
        }
    if any([env.get(bstack1l_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࠨᴍ")), env.get(bstack1l_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋ࡟ࡖࡔࡏࠦᴎ")), env.get(bstack1l_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࡠࡗࡖࡉࡗࡔࡁࡎࡇࠥᴏ")), env.get(bstack1l_opy_ (u"ࠨࡃࡐࡐࡆࡓ࡚ࡘࡓࡆࡡࡗࡉࡆࡓࠢᴐ"))]):
        return {
            bstack1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᴑ"): bstack1l_opy_ (u"ࠣࡅࡲࡲࡨࡵࡵࡳࡵࡨࠦᴒ"),
            bstack1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᴓ"): None,
            bstack1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᴔ"): env.get(bstack1l_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧᴕ")) or None,
            bstack1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᴖ"): env.get(bstack1l_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡏࡄࠣᴗ"), 0)
        }
    if env.get(bstack1l_opy_ (u"ࠢࡈࡑࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧᴘ")):
        return {
            bstack1l_opy_ (u"ࠣࡰࡤࡱࡪࠨᴙ"): bstack1l_opy_ (u"ࠤࡊࡳࡈࡊࠢᴚ"),
            bstack1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᴛ"): None,
            bstack1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᴜ"): env.get(bstack1l_opy_ (u"ࠧࡍࡏࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᴝ")),
            bstack1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᴞ"): env.get(bstack1l_opy_ (u"ࠢࡈࡑࡢࡔࡎࡖࡅࡍࡋࡑࡉࡤࡉࡏࡖࡐࡗࡉࡗࠨᴟ"))
        }
    if env.get(bstack1l_opy_ (u"ࠣࡅࡉࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᴠ")):
        return {
            bstack1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᴡ"): bstack1l_opy_ (u"ࠥࡇࡴࡪࡥࡇࡴࡨࡷ࡭ࠨᴢ"),
            bstack1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᴣ"): env.get(bstack1l_opy_ (u"ࠧࡉࡆࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦᴤ")),
            bstack1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᴥ"): env.get(bstack1l_opy_ (u"ࠢࡄࡈࡢࡔࡎࡖࡅࡍࡋࡑࡉࡤࡔࡁࡎࡇࠥᴦ")),
            bstack1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᴧ"): env.get(bstack1l_opy_ (u"ࠤࡆࡊࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢᴨ"))
        }
    return {bstack1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᴩ"): None}
def get_host_info():
    return {
        bstack1l_opy_ (u"ࠦ࡭ࡵࡳࡵࡰࡤࡱࡪࠨᴪ"): platform.node(),
        bstack1l_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࠢᴫ"): platform.system(),
        bstack1l_opy_ (u"ࠨࡴࡺࡲࡨࠦᴬ"): platform.machine(),
        bstack1l_opy_ (u"ࠢࡷࡧࡵࡷ࡮ࡵ࡮ࠣᴭ"): platform.version(),
        bstack1l_opy_ (u"ࠣࡣࡵࡧ࡭ࠨᴮ"): platform.architecture()[0]
    }
def bstack11l11l1l11_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack111l1ll1l11_opy_():
    if bstack1lll1ll1l_opy_.get_property(bstack1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪᴯ")):
        return bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩᴰ")
    return bstack1l_opy_ (u"ࠫࡺࡴ࡫࡯ࡱࡺࡲࡤ࡭ࡲࡪࡦࠪᴱ")
def bstack1111lll11ll_opy_(driver):
    info = {
        bstack1l_opy_ (u"ࠬࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫᴲ"): driver.capabilities,
        bstack1l_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠪᴳ"): driver.session_id,
        bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨᴴ"): driver.capabilities.get(bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ᴵ"), None),
        bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫᴶ"): driver.capabilities.get(bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫᴷ"), None),
        bstack1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࠭ᴸ"): driver.capabilities.get(bstack1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠫᴹ"), None),
        bstack1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᴺ"):driver.capabilities.get(bstack1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩᴻ"), None),
    }
    if bstack111l1ll1l11_opy_() == bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᴼ"):
        if bstack111lll1lll_opy_():
            info[bstack1l_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࠪᴽ")] = bstack1l_opy_ (u"ࠪࡥࡵࡶ࠭ࡢࡷࡷࡳࡲࡧࡴࡦࠩᴾ")
        elif driver.capabilities.get(bstack1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᴿ"), {}).get(bstack1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩᵀ"), False):
            info[bstack1l_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺࠧᵁ")] = bstack1l_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫᵂ")
        else:
            info[bstack1l_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࠩᵃ")] = bstack1l_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫᵄ")
    return info
def bstack111lll1lll_opy_():
    if bstack1lll1ll1l_opy_.get_property(bstack1l_opy_ (u"ࠪࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠩᵅ")):
        return True
    if bstack1l11l1ll1l_opy_(os.environ.get(bstack1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬᵆ"), None)):
        return True
    return False
def bstack1ll1llll11_opy_(bstack111l11l1l11_opy_, url, data, config):
    headers = config.get(bstack1l_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭ᵇ"), None)
    proxies = bstack1111l1ll1l_opy_(config, url)
    auth = config.get(bstack1l_opy_ (u"࠭ࡡࡶࡶ࡫ࠫᵈ"), None)
    response = requests.request(
            bstack111l11l1l11_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1111llllll_opy_(bstack11l1l111ll_opy_, size):
    bstack111l1l1ll_opy_ = []
    while len(bstack11l1l111ll_opy_) > size:
        bstack1l1l1lll11_opy_ = bstack11l1l111ll_opy_[:size]
        bstack111l1l1ll_opy_.append(bstack1l1l1lll11_opy_)
        bstack11l1l111ll_opy_ = bstack11l1l111ll_opy_[size:]
    bstack111l1l1ll_opy_.append(bstack11l1l111ll_opy_)
    return bstack111l1l1ll_opy_
def bstack1111ll111ll_opy_(message, bstack1111ll1l111_opy_=False):
    os.write(1, bytes(message, bstack1l_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ᵉ")))
    os.write(1, bytes(bstack1l_opy_ (u"ࠨ࡞ࡱࠫᵊ"), bstack1l_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᵋ")))
    if bstack1111ll1l111_opy_:
        with open(bstack1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠰ࡳ࠶࠷ࡹ࠮ࠩᵌ") + os.environ[bstack1l_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡉࡃࡖࡌࡊࡊ࡟ࡊࡆࠪᵍ")] + bstack1l_opy_ (u"ࠬ࠴࡬ࡰࡩࠪᵎ"), bstack1l_opy_ (u"࠭ࡡࠨᵏ")) as f:
            f.write(message + bstack1l_opy_ (u"ࠧ࡝ࡰࠪᵐ"))
def bstack1lll1l1llll_opy_():
    return os.environ[bstack1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫᵑ")].lower() == bstack1l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧᵒ")
def bstack1ll11l1l_opy_():
    return bstack1l1l1lll_opy_().replace(tzinfo=None).isoformat() + bstack1l_opy_ (u"ࠪ࡞ࠬᵓ")
def bstack111ll11111l_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack1l_opy_ (u"ࠫ࡟࠭ᵔ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack1l_opy_ (u"ࠬࡠࠧᵕ")))).total_seconds() * 1000
def bstack111l1l111l1_opy_(timestamp):
    return bstack1111llll11l_opy_(timestamp).isoformat() + bstack1l_opy_ (u"࡚࠭ࠨᵖ")
def bstack1111ll1ll1l_opy_(bstack1111lll11l1_opy_):
    date_format = bstack1l_opy_ (u"࡛ࠧࠦࠨࡱࠪࡪࠠࠦࡊ࠽ࠩࡒࡀࠥࡔ࠰ࠨࡪࠬᵗ")
    bstack111l11ll1ll_opy_ = datetime.datetime.strptime(bstack1111lll11l1_opy_, date_format)
    return bstack111l11ll1ll_opy_.isoformat() + bstack1l_opy_ (u"ࠨ࡜ࠪᵘ")
def bstack1111lll1ll1_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᵙ")
    else:
        return bstack1l_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᵚ")
def bstack1l11l1ll1l_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack1l_opy_ (u"ࠫࡹࡸࡵࡦࠩᵛ")
def bstack111l11l11l1_opy_(val):
    return val.__str__().lower() == bstack1l_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫᵜ")
def error_handler(bstack111l1lllll1_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack111l1lllll1_opy_ as e:
                print(bstack1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡼࡿࠣ࠱ࡃࠦࡻࡾ࠼ࠣࡿࢂࠨᵝ").format(func.__name__, bstack111l1lllll1_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack111l111111l_opy_(bstack111l1ll1111_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack111l1ll1111_opy_(cls, *args, **kwargs)
            except bstack111l1lllll1_opy_ as e:
                print(bstack1l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡽࢀࠤ࠲ࡄࠠࡼࡿ࠽ࠤࢀࢃࠢᵞ").format(bstack111l1ll1111_opy_.__name__, bstack111l1lllll1_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack111l111111l_opy_
    else:
        return decorator
def bstack1l1l11llll_opy_(bstack111l1l1l_opy_):
    if os.getenv(bstack1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫᵟ")) is not None:
        return bstack1l11l1ll1l_opy_(os.getenv(bstack1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬᵠ")))
    if bstack1l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᵡ") in bstack111l1l1l_opy_ and bstack111l11l11l1_opy_(bstack111l1l1l_opy_[bstack1l_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᵢ")]):
        return False
    if bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᵣ") in bstack111l1l1l_opy_ and bstack111l11l11l1_opy_(bstack111l1l1l_opy_[bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᵤ")]):
        return False
    return True
def bstack11ll1l1lll_opy_():
    try:
        from pytest_bdd import reporting
        bstack1111llllll1_opy_ = os.environ.get(bstack1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡕࡔࡇࡕࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠢᵥ"), None)
        return bstack1111llllll1_opy_ is None or bstack1111llllll1_opy_ == bstack1l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠧᵦ")
    except Exception as e:
        return False
def bstack11l1l11ll1_opy_(hub_url, CONFIG):
    if bstack1lll1lll1l_opy_() <= version.parse(bstack1l_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩᵧ")):
        if hub_url:
            return bstack1l_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦᵨ") + hub_url + bstack1l_opy_ (u"ࠦ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠣᵩ")
        return bstack11ll1ll1l_opy_
    if hub_url:
        return bstack1l_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢᵪ") + hub_url + bstack1l_opy_ (u"ࠨ࠯ࡸࡦ࠲࡬ࡺࡨࠢᵫ")
    return bstack1l1l1l1lll_opy_
def bstack1111ll11ll1_opy_():
    return isinstance(os.getenv(bstack1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐ࡚ࡖࡈࡗ࡙ࡥࡐࡍࡗࡊࡍࡓ࠭ᵬ")), str)
def bstack1111l1ll11_opy_(url):
    return urlparse(url).hostname
def bstack1l1ll111l1_opy_(hostname):
    for bstack1ll1l11111_opy_ in bstack1ll1lll11_opy_:
        regex = re.compile(bstack1ll1l11111_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11ll11l11ll_opy_(bstack111l1111l11_opy_, file_name, logger):
    bstack1l11llll1l_opy_ = os.path.join(os.path.expanduser(bstack1l_opy_ (u"ࠨࢀࠪᵭ")), bstack111l1111l11_opy_)
    try:
        if not os.path.exists(bstack1l11llll1l_opy_):
            os.makedirs(bstack1l11llll1l_opy_)
        file_path = os.path.join(os.path.expanduser(bstack1l_opy_ (u"ࠩࢁࠫᵮ")), bstack111l1111l11_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack1l_opy_ (u"ࠪࡻࠬᵯ")):
                pass
            with open(file_path, bstack1l_opy_ (u"ࠦࡼ࠱ࠢᵰ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack1l1l1111l_opy_.format(str(e)))
def bstack11ll111ll1l_opy_(file_name, key, value, logger):
    file_path = bstack11ll11l11ll_opy_(bstack1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᵱ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack11lllll1l_opy_ = json.load(open(file_path, bstack1l_opy_ (u"࠭ࡲࡣࠩᵲ")))
        else:
            bstack11lllll1l_opy_ = {}
        bstack11lllll1l_opy_[key] = value
        with open(file_path, bstack1l_opy_ (u"ࠢࡸ࠭ࠥᵳ")) as outfile:
            json.dump(bstack11lllll1l_opy_, outfile)
def bstack1l1llll1ll_opy_(file_name, logger):
    file_path = bstack11ll11l11ll_opy_(bstack1l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᵴ"), file_name, logger)
    bstack11lllll1l_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack1l_opy_ (u"ࠩࡵࠫᵵ")) as bstack11l11l11l_opy_:
            bstack11lllll1l_opy_ = json.load(bstack11l11l11l_opy_)
    return bstack11lllll1l_opy_
def bstack1lll11l11_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡪࡥ࡭ࡧࡷ࡭ࡳ࡭ࠠࡧ࡫࡯ࡩ࠿ࠦࠧᵶ") + file_path + bstack1l_opy_ (u"ࠫࠥ࠭ᵷ") + str(e))
def bstack1lll1lll1l_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack1l_opy_ (u"ࠧࡂࡎࡐࡖࡖࡉ࡙ࡄࠢᵸ")
def bstack1l1111llll_opy_(config):
    if bstack1l_opy_ (u"࠭ࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬᵹ") in config:
        del (config[bstack1l_opy_ (u"ࠧࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ᵺ")])
        return False
    if bstack1lll1lll1l_opy_() < version.parse(bstack1l_opy_ (u"ࠨ࠵࠱࠸࠳࠶ࠧᵻ")):
        return False
    if bstack1lll1lll1l_opy_() >= version.parse(bstack1l_opy_ (u"ࠩ࠷࠲࠶࠴࠵ࠨᵼ")):
        return True
    if bstack1l_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪᵽ") in config and config[bstack1l_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫᵾ")] is False:
        return False
    else:
        return True
def bstack111ll1ll1_opy_(args_list, bstack111l1ll1l1l_opy_):
    index = -1
    for value in bstack111l1ll1l1l_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
def bstack1111l1lll11_opy_(a, b):
  for k, v in b.items():
    if isinstance(v, dict) and k in a and isinstance(a[k], dict):
        bstack1111l1lll11_opy_(a[k], v)
    else:
        a[k] = v
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1l111ll1_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1l111ll1_opy_ = bstack1l111ll1_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᵿ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᶀ"), exception=exception)
    def bstack11111l11ll_opy_(self):
        if self.result != bstack1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᶁ"):
            return None
        if isinstance(self.exception_type, str) and bstack1l_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࠦᶂ") in self.exception_type:
            return bstack1l_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࡊࡸࡲࡰࡴࠥᶃ")
        return bstack1l_opy_ (u"࡙ࠥࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠦᶄ")
    def bstack111l1l1l1ll_opy_(self):
        if self.result != bstack1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᶅ"):
            return None
        if self.bstack1l111ll1_opy_:
            return self.bstack1l111ll1_opy_
        return bstack111l111l1ll_opy_(self.exception)
def bstack111l111l1ll_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack111l1111111_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1llll11l_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1lll11ll1_opy_(config, logger):
    try:
        import playwright
        bstack111l1ll111l_opy_ = playwright.__file__
        bstack1111lll1l11_opy_ = os.path.split(bstack111l1ll111l_opy_)
        bstack111l1l11l11_opy_ = bstack1111lll1l11_opy_[0] + bstack1l_opy_ (u"ࠬ࠵ࡤࡳ࡫ࡹࡩࡷ࠵ࡰࡢࡥ࡮ࡥ࡬࡫࠯࡭࡫ࡥ࠳ࡨࡲࡩ࠰ࡥ࡯࡭࠳ࡰࡳࠨᶆ")
        os.environ[bstack1l_opy_ (u"࠭ࡇࡍࡑࡅࡅࡑࡥࡁࡈࡇࡑࡘࡤࡎࡔࡕࡒࡢࡔࡗࡕࡘ࡚ࠩᶇ")] = bstack1l1llllll_opy_(config)
        with open(bstack111l1l11l11_opy_, bstack1l_opy_ (u"ࠧࡳࠩᶈ")) as f:
            file_content = f.read()
            bstack1111ll111l1_opy_ = bstack1l_opy_ (u"ࠨࡩ࡯ࡳࡧࡧ࡬࠮ࡣࡪࡩࡳࡺࠧᶉ")
            bstack111l1ll11ll_opy_ = file_content.find(bstack1111ll111l1_opy_)
            if bstack111l1ll11ll_opy_ == -1:
              process = subprocess.Popen(bstack1l_opy_ (u"ࠤࡱࡴࡲࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡨ࡮ࡲࡦࡦࡲ࠭ࡢࡩࡨࡲࡹࠨᶊ"), shell=True, cwd=bstack1111lll1l11_opy_[0])
              process.wait()
              bstack1111l1ll111_opy_ = bstack1l_opy_ (u"ࠪࠦࡺࡹࡥࠡࡵࡷࡶ࡮ࡩࡴࠣ࠽ࠪᶋ")
              bstack111l1l11ll1_opy_ = bstack1l_opy_ (u"ࠦࠧࠨࠠ࡝ࠤࡸࡷࡪࠦࡳࡵࡴ࡬ࡧࡹࡢࠢ࠼ࠢࡦࡳࡳࡹࡴࠡࡽࠣࡦࡴࡵࡴࡴࡶࡵࡥࡵࠦࡽࠡ࠿ࠣࡶࡪࡷࡵࡪࡴࡨࠬࠬ࡭࡬ࡰࡤࡤࡰ࠲ࡧࡧࡦࡰࡷࠫ࠮ࡁࠠࡪࡨࠣࠬࡵࡸ࡯ࡤࡧࡶࡷ࠳࡫࡮ࡷ࠰ࡊࡐࡔࡈࡁࡍࡡࡄࡋࡊࡔࡔࡠࡊࡗࡘࡕࡥࡐࡓࡑ࡛࡝࠮ࠦࡢࡰࡱࡷࡷࡹࡸࡡࡱࠪࠬ࠿ࠥࠨࠢࠣᶌ")
              bstack1111lllll1l_opy_ = file_content.replace(bstack1111l1ll111_opy_, bstack111l1l11ll1_opy_)
              with open(bstack111l1l11l11_opy_, bstack1l_opy_ (u"ࠬࡽࠧᶍ")) as f:
                f.write(bstack1111lllll1l_opy_)
    except Exception as e:
        logger.error(bstack1ll1ll11ll_opy_.format(str(e)))
def bstack111l11llll_opy_():
  try:
    bstack111ll1111ll_opy_ = os.path.join(tempfile.gettempdir(), bstack1l_opy_ (u"࠭࡯ࡱࡶ࡬ࡱࡦࡲ࡟ࡩࡷࡥࡣࡺࡸ࡬࠯࡬ࡶࡳࡳ࠭ᶎ"))
    bstack1111ll1l1ll_opy_ = []
    if os.path.exists(bstack111ll1111ll_opy_):
      with open(bstack111ll1111ll_opy_) as f:
        bstack1111ll1l1ll_opy_ = json.load(f)
      os.remove(bstack111ll1111ll_opy_)
    return bstack1111ll1l1ll_opy_
  except:
    pass
  return []
def bstack1111l11l11_opy_(bstack111111lll_opy_):
  try:
    bstack1111ll1l1ll_opy_ = []
    bstack111ll1111ll_opy_ = os.path.join(tempfile.gettempdir(), bstack1l_opy_ (u"ࠧࡰࡲࡷ࡭ࡲࡧ࡬ࡠࡪࡸࡦࡤࡻࡲ࡭࠰࡭ࡷࡴࡴࠧᶏ"))
    if os.path.exists(bstack111ll1111ll_opy_):
      with open(bstack111ll1111ll_opy_) as f:
        bstack1111ll1l1ll_opy_ = json.load(f)
    bstack1111ll1l1ll_opy_.append(bstack111111lll_opy_)
    with open(bstack111ll1111ll_opy_, bstack1l_opy_ (u"ࠨࡹࠪᶐ")) as f:
        json.dump(bstack1111ll1l1ll_opy_, f)
  except:
    pass
def bstack1llll1l1l1_opy_(logger, bstack1111l1l1l11_opy_ = False):
  try:
    test_name = os.environ.get(bstack1l_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕࡡࡗࡉࡘ࡚࡟ࡏࡃࡐࡉࠬᶑ"), bstack1l_opy_ (u"ࠪࠫᶒ"))
    if test_name == bstack1l_opy_ (u"ࠫࠬᶓ"):
        test_name = threading.current_thread().__dict__.get(bstack1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡇࡪࡤࡠࡶࡨࡷࡹࡥ࡮ࡢ࡯ࡨࠫᶔ"), bstack1l_opy_ (u"࠭ࠧᶕ"))
    bstack1111lll111l_opy_ = bstack1l_opy_ (u"ࠧ࠭ࠢࠪᶖ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack1111l1l1l11_opy_:
        bstack11l111l1l_opy_ = os.environ.get(bstack1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨᶗ"), bstack1l_opy_ (u"ࠩ࠳ࠫᶘ"))
        bstack1111111ll_opy_ = {bstack1l_opy_ (u"ࠪࡲࡦࡳࡥࠨᶙ"): test_name, bstack1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᶚ"): bstack1111lll111l_opy_, bstack1l_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫᶛ"): bstack11l111l1l_opy_}
        bstack111l11llll1_opy_ = []
        bstack1111ll11lll_opy_ = os.path.join(tempfile.gettempdir(), bstack1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡰࡱࡲࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬᶜ"))
        if os.path.exists(bstack1111ll11lll_opy_):
            with open(bstack1111ll11lll_opy_) as f:
                bstack111l11llll1_opy_ = json.load(f)
        bstack111l11llll1_opy_.append(bstack1111111ll_opy_)
        with open(bstack1111ll11lll_opy_, bstack1l_opy_ (u"ࠧࡸࠩᶝ")) as f:
            json.dump(bstack111l11llll1_opy_, f)
    else:
        bstack1111111ll_opy_ = {bstack1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᶞ"): test_name, bstack1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᶟ"): bstack1111lll111l_opy_, bstack1l_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩᶠ"): str(multiprocessing.current_process().name)}
        if bstack1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴࠨᶡ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack1111111ll_opy_)
  except Exception as e:
      logger.warn(bstack1l_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡳࡷ࡫ࠠࡱࡻࡷࡩࡸࡺࠠࡧࡷࡱࡲࡪࡲࠠࡥࡣࡷࡥ࠿ࠦࡻࡾࠤᶢ").format(e))
def bstack1l1l1l111_opy_(error_message, test_name, index, logger):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡰࡴࡩ࡫ࠡࡰࡲࡸࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥ࠭ࠢࡸࡷ࡮ࡴࡧࠡࡤࡤࡷ࡮ࡩࠠࡧ࡫࡯ࡩࠥࡵࡰࡦࡴࡤࡸ࡮ࡵ࡮ࡴࠩᶣ"))
    try:
      bstack1111llll1ll_opy_ = []
      bstack1111111ll_opy_ = {bstack1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᶤ"): test_name, bstack1l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᶥ"): error_message, bstack1l_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨᶦ"): index}
      bstack111l11lllll_opy_ = os.path.join(tempfile.gettempdir(), bstack1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫᶧ"))
      if os.path.exists(bstack111l11lllll_opy_):
          with open(bstack111l11lllll_opy_) as f:
              bstack1111llll1ll_opy_ = json.load(f)
      bstack1111llll1ll_opy_.append(bstack1111111ll_opy_)
      with open(bstack111l11lllll_opy_, bstack1l_opy_ (u"ࠫࡼ࠭ᶨ")) as f:
          json.dump(bstack1111llll1ll_opy_, f)
    except Exception as e:
      logger.warn(bstack1l_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡳࡷ࡫ࠠࡳࡱࡥࡳࡹࠦࡦࡶࡰࡱࡩࡱࠦࡤࡢࡶࡤ࠾ࠥࢁࡽࠣᶩ").format(e))
    return
  bstack1111llll1ll_opy_ = []
  bstack1111111ll_opy_ = {bstack1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᶪ"): test_name, bstack1l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᶫ"): error_message, bstack1l_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧᶬ"): index}
  bstack111l11lllll_opy_ = os.path.join(tempfile.gettempdir(), bstack1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪᶭ"))
  lock_file = bstack111l11lllll_opy_ + bstack1l_opy_ (u"ࠪ࠲ࡱࡵࡣ࡬ࠩᶮ")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack111l11lllll_opy_):
          with open(bstack111l11lllll_opy_, bstack1l_opy_ (u"ࠫࡷ࠭ᶯ")) as f:
              content = f.read().strip()
              if content:
                  bstack1111llll1ll_opy_ = json.load(open(bstack111l11lllll_opy_))
      bstack1111llll1ll_opy_.append(bstack1111111ll_opy_)
      with open(bstack111l11lllll_opy_, bstack1l_opy_ (u"ࠬࡽࠧᶰ")) as f:
          json.dump(bstack1111llll1ll_opy_, f)
  except Exception as e:
    logger.warn(bstack1l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡴࡸࡥࠡࡴࡲࡦࡴࡺࠠࡧࡷࡱࡲࡪࡲࠠࡥࡣࡷࡥࠥࡽࡩࡵࡪࠣࡪ࡮ࡲࡥࠡ࡮ࡲࡧࡰ࡯࡮ࡨ࠼ࠣࡿࢂࠨᶱ").format(e))
def bstack1ll11l11l1_opy_(bstack11ll1l111_opy_, name, logger):
  try:
    bstack1111111ll_opy_ = {bstack1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᶲ"): name, bstack1l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᶳ"): bstack11ll1l111_opy_, bstack1l_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨᶴ"): str(threading.current_thread()._name)}
    return bstack1111111ll_opy_
  except Exception as e:
    logger.warn(bstack1l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡱࡵࡩࠥࡨࡥࡩࡣࡹࡩࠥ࡬ࡵ࡯ࡰࡨࡰࠥࡪࡡࡵࡣ࠽ࠤࢀࢃࠢᶵ").format(e))
  return
def bstack111l1l1l1l1_opy_():
    return platform.system() == bstack1l_opy_ (u"ࠫ࡜࡯࡮ࡥࡱࡺࡷࠬᶶ")
def bstack111lllll1_opy_(bstack111l1lll1ll_opy_, config, logger):
    bstack111l1l111ll_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack111l1lll1ll_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack1l_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡨ࡬ࡰࡹ࡫ࡲࠡࡥࡲࡲ࡫࡯ࡧࠡ࡭ࡨࡽࡸࠦࡢࡺࠢࡵࡩ࡬࡫ࡸࠡ࡯ࡤࡸࡨ࡮࠺ࠡࡽࢀࠦᶷ").format(e))
    return bstack111l1l111ll_opy_
def bstack11l1ll111l1_opy_(bstack1111ll1llll_opy_, bstack111ll111ll1_opy_):
    bstack1111lll1111_opy_ = version.parse(bstack1111ll1llll_opy_)
    bstack111l111ll1l_opy_ = version.parse(bstack111ll111ll1_opy_)
    if bstack1111lll1111_opy_ > bstack111l111ll1l_opy_:
        return 1
    elif bstack1111lll1111_opy_ < bstack111l111ll1l_opy_:
        return -1
    else:
        return 0
def bstack1l1l1lll_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack1111llll11l_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack111l1l11lll_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack1lll11lll1_opy_(options, framework, config, bstack1111llll11_opy_={}):
    if options is None:
        return
    if getattr(options, bstack1l_opy_ (u"࠭ࡧࡦࡶࠪᶸ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack1l11ll1ll1_opy_ = caps.get(bstack1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᶹ"))
    bstack111l111l111_opy_ = True
    bstack11lll1ll11_opy_ = os.environ[bstack1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ᶺ")]
    bstack1l111l111ll_opy_ = config.get(bstack1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᶻ"), False)
    if bstack1l111l111ll_opy_:
        bstack1l1l1l1lll1_opy_ = config.get(bstack1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᶼ"), {})
        bstack1l1l1l1lll1_opy_[bstack1l_opy_ (u"ࠫࡦࡻࡴࡩࡖࡲ࡯ࡪࡴࠧᶽ")] = os.getenv(bstack1l_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪᶾ"))
        bstack111l11lll1l_opy_ = json.loads(os.getenv(bstack1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧᶿ"), bstack1l_opy_ (u"ࠧࡼࡿࠪ᷀"))).get(bstack1l_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ᷁"))
    if bstack111l11l11l1_opy_(caps.get(bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡷࡶࡩ࡜࠹ࡃࠨ᷂"))) or bstack111l11l11l1_opy_(caps.get(bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡸࡷࡪࡥࡷ࠴ࡥࠪ᷃"))):
        bstack111l111l111_opy_ = False
    if bstack1l1111llll_opy_({bstack1l_opy_ (u"ࠦࡺࡹࡥࡘ࠵ࡆࠦ᷄"): bstack111l111l111_opy_}):
        bstack1l11ll1ll1_opy_ = bstack1l11ll1ll1_opy_ or {}
        bstack1l11ll1ll1_opy_[bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧ᷅")] = bstack111l1l11lll_opy_(framework)
        bstack1l11ll1ll1_opy_[bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨ᷆")] = bstack1lll1l1llll_opy_()
        bstack1l11ll1ll1_opy_[bstack1l_opy_ (u"ࠧࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪ᷇")] = bstack11lll1ll11_opy_
        bstack1l11ll1ll1_opy_[bstack1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪ᷈")] = bstack1111llll11_opy_
        if bstack1l111l111ll_opy_:
            bstack1l11ll1ll1_opy_[bstack1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ᷉")] = bstack1l111l111ll_opy_
            bstack1l11ll1ll1_opy_[bstack1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵ᷊ࠪ")] = bstack1l1l1l1lll1_opy_
            bstack1l11ll1ll1_opy_[bstack1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ᷋")][bstack1l_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭᷌")] = bstack111l11lll1l_opy_
        if getattr(options, bstack1l_opy_ (u"࠭ࡳࡦࡶࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹࡿࠧ᷍"), None):
            options.set_capability(bstack1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ᷎"), bstack1l11ll1ll1_opy_)
        else:
            options[bstack1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴ᷏ࠩ")] = bstack1l11ll1ll1_opy_
    else:
        if getattr(options, bstack1l_opy_ (u"ࠩࡶࡩࡹࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵࡻ᷐ࠪ"), None):
            options.set_capability(bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫ᷑"), bstack111l1l11lll_opy_(framework))
            options.set_capability(bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ᷒"), bstack1lll1l1llll_opy_())
            options.set_capability(bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧᷓ"), bstack11lll1ll11_opy_)
            options.set_capability(bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧᷔ"), bstack1111llll11_opy_)
            if bstack1l111l111ll_opy_:
                options.set_capability(bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᷕ"), bstack1l111l111ll_opy_)
                options.set_capability(bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᷖ"), bstack1l1l1l1lll1_opy_)
                options.set_capability(bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳ࠯ࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᷗ"), bstack111l11lll1l_opy_)
        else:
            options[bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫᷘ")] = bstack111l1l11lll_opy_(framework)
            options[bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᷙ")] = bstack1lll1l1llll_opy_()
            options[bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧᷚ")] = bstack11lll1ll11_opy_
            options[bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧᷛ")] = bstack1111llll11_opy_
            if bstack1l111l111ll_opy_:
                options[bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᷜ")] = bstack1l111l111ll_opy_
                options[bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᷝ")] = bstack1l1l1l1lll1_opy_
                options[bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨᷞ")][bstack1l_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫᷟ")] = bstack111l11lll1l_opy_
    return options
def bstack111l11l1lll_opy_(ws_endpoint, framework):
    bstack1111llll11_opy_ = bstack1lll1ll1l_opy_.get_property(bstack1l_opy_ (u"ࠦࡕࡒࡁ࡚࡙ࡕࡍࡌࡎࡔࡠࡒࡕࡓࡉ࡛ࡃࡕࡡࡐࡅࡕࠨᷠ"))
    if ws_endpoint and len(ws_endpoint.split(bstack1l_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫᷡ"))) > 1:
        ws_url = ws_endpoint.split(bstack1l_opy_ (u"࠭ࡣࡢࡲࡶࡁࠬᷢ"))[0]
        if bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪᷣ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack1111ll1l11l_opy_ = json.loads(urllib.parse.unquote(ws_endpoint.split(bstack1l_opy_ (u"ࠨࡥࡤࡴࡸࡃࠧᷤ"))[1]))
            bstack1111ll1l11l_opy_ = bstack1111ll1l11l_opy_ or {}
            bstack11lll1ll11_opy_ = os.environ[bstack1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧᷥ")]
            bstack1111ll1l11l_opy_[bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫᷦ")] = str(framework) + str(__version__)
            bstack1111ll1l11l_opy_[bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᷧ")] = bstack1lll1l1llll_opy_()
            bstack1111ll1l11l_opy_[bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧᷨ")] = bstack11lll1ll11_opy_
            bstack1111ll1l11l_opy_[bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧᷩ")] = bstack1111llll11_opy_
            ws_endpoint = ws_endpoint.split(bstack1l_opy_ (u"ࠧࡤࡣࡳࡷࡂ࠭ᷪ"))[0] + bstack1l_opy_ (u"ࠨࡥࡤࡴࡸࡃࠧᷫ") + urllib.parse.quote(json.dumps(bstack1111ll1l11l_opy_))
    return ws_endpoint
def bstack111lll111_opy_():
    global bstack1ll1l111l1_opy_
    from playwright._impl._browser_type import BrowserType
    bstack1ll1l111l1_opy_ = BrowserType.connect
    return bstack1ll1l111l1_opy_
def bstack1ll11lll1l_opy_(framework_name):
    global bstack11l1lll1l_opy_
    bstack11l1lll1l_opy_ = framework_name
    return framework_name
def bstack11lllll111_opy_(self, *args, **kwargs):
    global bstack1ll1l111l1_opy_
    try:
        global bstack11l1lll1l_opy_
        if bstack1l_opy_ (u"ࠩࡺࡷࡊࡴࡤࡱࡱ࡬ࡲࡹ࠭ᷬ") in kwargs:
            kwargs[bstack1l_opy_ (u"ࠪࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺࠧᷭ")] = bstack111l11l1lll_opy_(
                kwargs.get(bstack1l_opy_ (u"ࠫࡼࡹࡅ࡯ࡦࡳࡳ࡮ࡴࡴࠨᷮ"), None),
                bstack11l1lll1l_opy_
            )
    except Exception as e:
        logger.error(bstack1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡥ࡯ࠢࡳࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡓࡅࡍࠣࡧࡦࡶࡳ࠻ࠢࡾࢁࠧᷯ").format(str(e)))
    return bstack1ll1l111l1_opy_(self, *args, **kwargs)
def bstack111l11l1ll1_opy_(bstack111l1l1lll1_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack1111l1ll1l_opy_(bstack111l1l1lll1_opy_, bstack1l_opy_ (u"ࠨࠢᷰ"))
        if proxies and proxies.get(bstack1l_opy_ (u"ࠢࡩࡶࡷࡴࡸࠨᷱ")):
            parsed_url = urlparse(proxies.get(bstack1l_opy_ (u"ࠣࡪࡷࡸࡵࡹࠢᷲ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡉࡱࡶࡸࠬᷳ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡲࡶࡹ࠭ᷴ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡘࡷࡪࡸࠧ᷵")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡦࡹࡳࠨ᷶")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack1111l1l1ll_opy_(bstack111l1l1lll1_opy_):
    bstack1111l1ll1l1_opy_ = {
        bstack11l1l1l1111_opy_[bstack1111ll1l1l1_opy_]: bstack111l1l1lll1_opy_[bstack1111ll1l1l1_opy_]
        for bstack1111ll1l1l1_opy_ in bstack111l1l1lll1_opy_
        if bstack1111ll1l1l1_opy_ in bstack11l1l1l1111_opy_
    }
    bstack1111l1ll1l1_opy_[bstack1l_opy_ (u"ࠨࡰࡳࡱࡻࡽࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸࠨ᷷")] = bstack111l11l1ll1_opy_(bstack111l1l1lll1_opy_, bstack1lll1ll1l_opy_.get_property(bstack1l_opy_ (u"ࠢࡱࡴࡲࡼࡾ࡙ࡥࡵࡶ࡬ࡲ࡬ࡹ᷸ࠢ")))
    bstack111l1111l1l_opy_ = [element.lower() for element in bstack11l1l11lll1_opy_]
    bstack111l1l1l11l_opy_(bstack1111l1ll1l1_opy_, bstack111l1111l1l_opy_)
    return bstack1111l1ll1l1_opy_
def bstack111l1l1l11l_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack1l_opy_ (u"ࠣࠬ࠭࠮࠯ࠨ᷹")
    for value in d.values():
        if isinstance(value, dict):
            bstack111l1l1l11l_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack111l1l1l11l_opy_(item, keys)
def bstack1ll111l11l1_opy_():
    bstack111l1ll1ll1_opy_ = [os.environ.get(bstack1l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡌࡐࡊ࡙࡟ࡅࡋࡕ᷺ࠦ")), os.path.join(os.path.expanduser(bstack1l_opy_ (u"ࠥࢂࠧ᷻")), bstack1l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫ᷼")), os.path.join(bstack1l_opy_ (u"ࠬ࠵ࡴ࡮ࡲ᷽ࠪ"), bstack1l_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭᷾"))]
    for path in bstack111l1ll1ll1_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack1l_opy_ (u"ࠢࡇ࡫࡯ࡩ᷿ࠥ࠭ࠢ") + str(path) + bstack1l_opy_ (u"ࠣࠩࠣࡩࡽ࡯ࡳࡵࡵ࠱ࠦḀ"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack1l_opy_ (u"ࠤࡊ࡭ࡻ࡯࡮ࡨࠢࡳࡩࡷࡳࡩࡴࡵ࡬ࡳࡳࡹࠠࡧࡱࡵࠤࠬࠨḁ") + str(path) + bstack1l_opy_ (u"ࠥࠫࠧḂ"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack1l_opy_ (u"ࠦࡋ࡯࡬ࡦࠢࠪࠦḃ") + str(path) + bstack1l_opy_ (u"ࠧ࠭ࠠࡢ࡮ࡵࡩࡦࡪࡹࠡࡪࡤࡷࠥࡺࡨࡦࠢࡵࡩࡶࡻࡩࡳࡧࡧࠤࡵ࡫ࡲ࡮࡫ࡶࡷ࡮ࡵ࡮ࡴ࠰ࠥḄ"))
            else:
                logger.debug(bstack1l_opy_ (u"ࠨࡃࡳࡧࡤࡸ࡮ࡴࡧࠡࡨ࡬ࡰࡪࠦࠧࠣḅ") + str(path) + bstack1l_opy_ (u"ࠢࠨࠢࡺ࡭ࡹ࡮ࠠࡸࡴ࡬ࡸࡪࠦࡰࡦࡴࡰ࡭ࡸࡹࡩࡰࡰ࠱ࠦḆ"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack1l_opy_ (u"ࠣࡑࡳࡩࡷࡧࡴࡪࡱࡱࠤࡸࡻࡣࡤࡧࡨࡨࡪࡪࠠࡧࡱࡵࠤࠬࠨḇ") + str(path) + bstack1l_opy_ (u"ࠤࠪ࠲ࠧḈ"))
            return path
        except Exception as e:
            logger.debug(bstack1l_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡹࡵࠦࡦࡪ࡮ࡨࠤࠬࢁࡰࡢࡶ࡫ࢁࠬࡀࠠࠣḉ") + str(e) + bstack1l_opy_ (u"ࠦࠧḊ"))
    logger.debug(bstack1l_opy_ (u"ࠧࡇ࡬࡭ࠢࡳࡥࡹ࡮ࡳࠡࡨࡤ࡭ࡱ࡫ࡤ࠯ࠤḋ"))
    return None
@measure(event_name=EVENTS.bstack11l1l11l1ll_opy_, stage=STAGE.bstack11ll111111_opy_)
def bstack1l1l1111lll_opy_(binary_path, bstack1l1l1ll1lll_opy_, bs_config):
    logger.debug(bstack1l_opy_ (u"ࠨࡃࡶࡴࡵࡩࡳࡺࠠࡄࡎࡌࠤࡕࡧࡴࡩࠢࡩࡳࡺࡴࡤ࠻ࠢࡾࢁࠧḌ").format(binary_path))
    bstack111ll111l1l_opy_ = bstack1l_opy_ (u"ࠧࠨḍ")
    bstack111l1lll11l_opy_ = {
        bstack1l_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭Ḏ"): __version__,
        bstack1l_opy_ (u"ࠤࡲࡷࠧḏ"): platform.system(),
        bstack1l_opy_ (u"ࠥࡳࡸࡥࡡࡳࡥ࡫ࠦḐ"): platform.machine(),
        bstack1l_opy_ (u"ࠦࡨࡲࡩࡠࡸࡨࡶࡸ࡯࡯࡯ࠤḑ"): bstack1l_opy_ (u"ࠬ࠶ࠧḒ"),
        bstack1l_opy_ (u"ࠨࡳࡥ࡭ࡢࡰࡦࡴࡧࡶࡣࡪࡩࠧḓ"): bstack1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧḔ")
    }
    bstack111l111l1l1_opy_(bstack111l1lll11l_opy_)
    try:
        if binary_path:
            bstack111l1lll11l_opy_[bstack1l_opy_ (u"ࠨࡥ࡯࡭ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ḕ")] = subprocess.check_output([binary_path, bstack1l_opy_ (u"ࠤࡹࡩࡷࡹࡩࡰࡰࠥḖ")]).strip().decode(bstack1l_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩḗ"))
        response = requests.request(
            bstack1l_opy_ (u"ࠫࡌࡋࡔࠨḘ"),
            url=bstack11lllll11_opy_(bstack11l1l1lll11_opy_),
            headers=None,
            auth=(bs_config[bstack1l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧḙ")], bs_config[bstack1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩḚ")]),
            json=None,
            params=bstack111l1lll11l_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack1l_opy_ (u"ࠧࡶࡴ࡯ࠫḛ") in data.keys() and bstack1l_opy_ (u"ࠨࡷࡳࡨࡦࡺࡥࡥࡡࡦࡰ࡮ࡥࡶࡦࡴࡶ࡭ࡴࡴࠧḜ") in data.keys():
            logger.debug(bstack1l_opy_ (u"ࠤࡑࡩࡪࡪࠠࡵࡱࠣࡹࡵࡪࡡࡵࡧࠣࡦ࡮ࡴࡡࡳࡻ࠯ࠤࡨࡻࡲࡳࡧࡱࡸࠥࡨࡩ࡯ࡣࡵࡽࠥࡼࡥࡳࡵ࡬ࡳࡳࡀࠠࡼࡿࠥḝ").format(bstack111l1lll11l_opy_[bstack1l_opy_ (u"ࠪࡧࡱ࡯࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨḞ")]))
            if bstack1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆࡎࡔࡁࡓ࡛ࡢ࡙ࡗࡒࠧḟ") in os.environ:
                logger.debug(bstack1l_opy_ (u"࡙ࠧ࡫ࡪࡲࡳ࡭ࡳ࡭ࠠࡣ࡫ࡱࡥࡷࡿࠠࡥࡱࡺࡲࡱࡵࡡࡥࠢࡤࡷࠥࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇࡏࡎࡂࡔ࡜ࡣ࡚ࡘࡌࠡ࡫ࡶࠤࡸ࡫ࡴࠣḠ"))
                data[bstack1l_opy_ (u"࠭ࡵࡳ࡮ࠪḡ")] = os.environ[bstack1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡊࡐࡄࡖ࡞ࡥࡕࡓࡎࠪḢ")]
            bstack1111l1l11l1_opy_ = bstack1111lll1l1l_opy_(data[bstack1l_opy_ (u"ࠨࡷࡵࡰࠬḣ")], bstack1l1l1ll1lll_opy_)
            bstack111ll111l1l_opy_ = os.path.join(bstack1l1l1ll1lll_opy_, bstack1111l1l11l1_opy_)
            os.chmod(bstack111ll111l1l_opy_, 0o777) # bstack111l1l11l1l_opy_ permission
            return bstack111ll111l1l_opy_
    except Exception as e:
        logger.debug(bstack1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡥࡱࡺࡲࡱࡵࡡࡥ࡫ࡱ࡫ࠥࡴࡥࡸࠢࡖࡈࡐࠦࡻࡾࠤḤ").format(e))
    return binary_path
def bstack111l111l1l1_opy_(bstack111l1lll11l_opy_):
    try:
        if bstack1l_opy_ (u"ࠪࡰ࡮ࡴࡵࡹࠩḥ") not in bstack111l1lll11l_opy_[bstack1l_opy_ (u"ࠫࡴࡹࠧḦ")].lower():
            return
        if os.path.exists(bstack1l_opy_ (u"ࠧ࠵ࡥࡵࡥ࠲ࡳࡸ࠳ࡲࡦ࡮ࡨࡥࡸ࡫ࠢḧ")):
            with open(bstack1l_opy_ (u"ࠨ࠯ࡦࡶࡦ࠳ࡴࡹ࠭ࡳࡧ࡯ࡩࡦࡹࡥࠣḨ"), bstack1l_opy_ (u"ࠢࡳࠤḩ")) as f:
                bstack111l1llllll_opy_ = {}
                for line in f:
                    if bstack1l_opy_ (u"ࠣ࠿ࠥḪ") in line:
                        key, value = line.rstrip().split(bstack1l_opy_ (u"ࠤࡀࠦḫ"), 1)
                        bstack111l1llllll_opy_[key] = value.strip(bstack1l_opy_ (u"ࠪࠦࡡ࠭ࠧḬ"))
                bstack111l1lll11l_opy_[bstack1l_opy_ (u"ࠫࡩ࡯ࡳࡵࡴࡲࠫḭ")] = bstack111l1llllll_opy_.get(bstack1l_opy_ (u"ࠧࡏࡄࠣḮ"), bstack1l_opy_ (u"ࠨࠢḯ"))
        elif os.path.exists(bstack1l_opy_ (u"ࠢ࠰ࡧࡷࡧ࠴ࡧ࡬ࡱ࡫ࡱࡩ࠲ࡸࡥ࡭ࡧࡤࡷࡪࠨḰ")):
            bstack111l1lll11l_opy_[bstack1l_opy_ (u"ࠨࡦ࡬ࡷࡹࡸ࡯ࠨḱ")] = bstack1l_opy_ (u"ࠩࡤࡰࡵ࡯࡮ࡦࠩḲ")
    except Exception as e:
        logger.debug(bstack1l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡧࡦࡶࠣࡨ࡮ࡹࡴࡳࡱࠣࡳ࡫ࠦ࡬ࡪࡰࡸࡼࠧḳ") + e)
@measure(event_name=EVENTS.bstack11l11llllll_opy_, stage=STAGE.bstack11ll111111_opy_)
def bstack1111lll1l1l_opy_(bstack111ll111111_opy_, bstack1111l1lll1l_opy_):
    logger.debug(bstack1l_opy_ (u"ࠦࡉࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡖࡈࡐࠦࡢࡪࡰࡤࡶࡾࠦࡦࡳࡱࡰ࠾ࠥࠨḴ") + str(bstack111ll111111_opy_) + bstack1l_opy_ (u"ࠧࠨḵ"))
    zip_path = os.path.join(bstack1111l1lll1l_opy_, bstack1l_opy_ (u"ࠨࡤࡰࡹࡱࡰࡴࡧࡤࡦࡦࡢࡪ࡮ࡲࡥ࠯ࡼ࡬ࡴࠧḶ"))
    bstack1111l1l11l1_opy_ = bstack1l_opy_ (u"ࠧࠨḷ")
    with requests.get(bstack111ll111111_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack1l_opy_ (u"ࠣࡹࡥࠦḸ")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack1l_opy_ (u"ࠤࡉ࡭ࡱ࡫ࠠࡥࡱࡺࡲࡱࡵࡡࡥࡧࡧࠤࡸࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬࡭ࡻ࠱ࠦḹ"))
    with zipfile.ZipFile(zip_path, bstack1l_opy_ (u"ࠪࡶࠬḺ")) as zip_ref:
        bstack111l11l11ll_opy_ = zip_ref.namelist()
        if len(bstack111l11l11ll_opy_) > 0:
            bstack1111l1l11l1_opy_ = bstack111l11l11ll_opy_[0] # bstack1111l1l1l1l_opy_ bstack11l1l1l1ll1_opy_ will be bstack111l1111ll1_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack1111l1lll1l_opy_)
        logger.debug(bstack1l_opy_ (u"ࠦࡋ࡯࡬ࡦࡵࠣࡷࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺࠢࡨࡼࡹࡸࡡࡤࡶࡨࡨࠥࡺ࡯ࠡࠩࠥḻ") + str(bstack1111l1lll1l_opy_) + bstack1l_opy_ (u"ࠧ࠭ࠢḼ"))
    os.remove(zip_path)
    return bstack1111l1l11l1_opy_
def get_cli_dir():
    bstack1111l1l1lll_opy_ = bstack1ll111l11l1_opy_()
    if bstack1111l1l1lll_opy_:
        bstack1l1l1ll1lll_opy_ = os.path.join(bstack1111l1l1lll_opy_, bstack1l_opy_ (u"ࠨࡣ࡭࡫ࠥḽ"))
        if not os.path.exists(bstack1l1l1ll1lll_opy_):
            os.makedirs(bstack1l1l1ll1lll_opy_, mode=0o777, exist_ok=True)
        return bstack1l1l1ll1lll_opy_
    else:
        raise FileNotFoundError(bstack1l_opy_ (u"ࠢࡏࡱࠣࡻࡷ࡯ࡴࡢࡤ࡯ࡩࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨࠤ࡫ࡵࡲࠡࡶ࡫ࡩ࡙ࠥࡄࡌࠢࡥ࡭ࡳࡧࡲࡺ࠰ࠥḾ"))
def bstack1l1l11lllll_opy_(bstack1l1l1ll1lll_opy_):
    bstack1l_opy_ (u"ࠣࠤࠥࡋࡪࡺࠠࡵࡪࡨࠤࡵࡧࡴࡩࠢࡩࡳࡷࠦࡴࡩࡧࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡖࡈࡐࠦࡢࡪࡰࡤࡶࡾࠦࡩ࡯ࠢࡤࠤࡼࡸࡩࡵࡣࡥࡰࡪࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺ࠰ࠥࠦࠧḿ")
    bstack111l11l1l1l_opy_ = [
        os.path.join(bstack1l1l1ll1lll_opy_, f)
        for f in os.listdir(bstack1l1l1ll1lll_opy_)
        if os.path.isfile(os.path.join(bstack1l1l1ll1lll_opy_, f)) and f.startswith(bstack1l_opy_ (u"ࠤࡥ࡭ࡳࡧࡲࡺ࠯ࠥṀ"))
    ]
    if len(bstack111l11l1l1l_opy_) > 0:
        return max(bstack111l11l1l1l_opy_, key=os.path.getmtime) # get bstack111l1llll11_opy_ binary
    return bstack1l_opy_ (u"ࠥࠦṁ")
def bstack1111l1lllll_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l111l1l1ll_opy_(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = bstack1l111l1l1ll_opy_(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack1l111ll1ll_opy_(data, keys, default=None):
    bstack1l_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡘࡧࡦࡦ࡮ࡼࠤ࡬࡫ࡴࠡࡣࠣࡲࡪࡹࡴࡦࡦࠣࡺࡦࡲࡵࡦࠢࡩࡶࡴࡳࠠࡢࠢࡧ࡭ࡨࡺࡩࡰࡰࡤࡶࡾࠦ࡯ࡳࠢ࡯࡭ࡸࡺ࠮ࠋࠢࠣࠤࠥࡀࡰࡢࡴࡤࡱࠥࡪࡡࡵࡣ࠽ࠤ࡙࡮ࡥࠡࡦ࡬ࡧࡹ࡯࡯࡯ࡣࡵࡽࠥࡵࡲࠡ࡮࡬ࡷࡹࠦࡴࡰࠢࡷࡶࡦࡼࡥࡳࡵࡨ࠲ࠏࠦࠠࠡࠢ࠽ࡴࡦࡸࡡ࡮ࠢ࡮ࡩࡾࡹ࠺ࠡࡃࠣࡰ࡮ࡹࡴࠡࡱࡩࠤࡰ࡫ࡹࡴ࠱࡬ࡲࡩ࡯ࡣࡦࡵࠣࡶࡪࡶࡲࡦࡵࡨࡲࡹ࡯࡮ࡨࠢࡷ࡬ࡪࠦࡰࡢࡶ࡫࠲ࠏࠦࠠࠡࠢ࠽ࡴࡦࡸࡡ࡮ࠢࡧࡩ࡫ࡧࡵ࡭ࡶ࠽ࠤ࡛ࡧ࡬ࡶࡧࠣࡸࡴࠦࡲࡦࡶࡸࡶࡳࠦࡩࡧࠢࡷ࡬ࡪࠦࡰࡢࡶ࡫ࠤࡩࡵࡥࡴࠢࡱࡳࡹࠦࡥࡹ࡫ࡶࡸ࠳ࠐࠠࠡࠢࠣ࠾ࡷ࡫ࡴࡶࡴࡱ࠾࡚ࠥࡨࡦࠢࡹࡥࡱࡻࡥࠡࡣࡷࠤࡹ࡮ࡥࠡࡰࡨࡷࡹ࡫ࡤࠡࡲࡤࡸ࡭࠲ࠠࡰࡴࠣࡨࡪ࡬ࡡࡶ࡮ࡷࠤ࡮࡬ࠠ࡯ࡱࡷࠤ࡫ࡵࡵ࡯ࡦ࠱ࠎࠥࠦࠠࠡࠤࠥࠦṂ")
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