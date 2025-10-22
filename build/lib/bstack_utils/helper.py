# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
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
from bstack_utils.constants import (bstack1l1l11ll11_opy_, bstack1l11l1l1l_opy_, bstack1lll11l11l_opy_,
                                    bstack11l11l1lll1_opy_, bstack11l11l1llll_opy_, bstack11l11lll1ll_opy_, bstack11l1l111l1l_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack11lll1l111_opy_, bstack11llll11l1_opy_
from bstack_utils.proxy import bstack1llll11111_opy_, bstack11lll1l1l_opy_
from bstack_utils.constants import *
from bstack_utils import bstack11ll1ll1l_opy_
from bstack_utils.bstack1l1ll1ll1_opy_ import bstack11llllll11_opy_
from browserstack_sdk._version import __version__
bstack111l11ll_opy_ = Config.bstack111l11l1_opy_()
logger = bstack11ll1ll1l_opy_.get_logger(__name__, bstack11ll1ll1l_opy_.bstack1l11llll111_opy_())
def bstack1111l1ll1ll_opy_(config):
    return config[bstack1l111ll_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ᯨ")]
def bstack111l11ll11l_opy_(config):
    return config[bstack1l111ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨᯩ")]
def bstack11l111l1l1_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack111l1lll11l_opy_(obj):
    values = []
    bstack111l11l111l_opy_ = re.compile(bstack1l111ll_opy_ (u"ࡸࠢ࡟ࡅࡘࡗ࡙ࡕࡍࡠࡖࡄࡋࡤࡢࡤࠬࠦࠥᯪ"), re.I)
    for key in obj.keys():
        if bstack111l11l111l_opy_.match(key):
            values.append(obj[key])
    return values
def bstack111l1l1ll11_opy_(config):
    tags = []
    tags.extend(bstack111l1lll11l_opy_(os.environ))
    tags.extend(bstack111l1lll11l_opy_(config))
    return tags
def bstack111l1111l11_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack1111ll1ll11_opy_(bstack111l1l1ll1l_opy_):
    if not bstack111l1l1ll1l_opy_:
        return bstack1l111ll_opy_ (u"ࠧࠨᯫ")
    return bstack1l111ll_opy_ (u"ࠣࡽࢀࠤ࠭ࢁࡽࠪࠤᯬ").format(bstack111l1l1ll1l_opy_.name, bstack111l1l1ll1l_opy_.email)
def bstack111l1111ll1_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack1111l1l11l1_opy_ = repo.common_dir
        info = {
            bstack1l111ll_opy_ (u"ࠤࡶ࡬ࡦࠨᯭ"): repo.head.commit.hexsha,
            bstack1l111ll_opy_ (u"ࠥࡷ࡭ࡵࡲࡵࡡࡶ࡬ࡦࠨᯮ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack1l111ll_opy_ (u"ࠦࡧࡸࡡ࡯ࡥ࡫ࠦᯯ"): repo.active_branch.name,
            bstack1l111ll_opy_ (u"ࠧࡺࡡࡨࠤᯰ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack1l111ll_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡺࡥࡳࠤᯱ"): bstack1111ll1ll11_opy_(repo.head.commit.committer),
            bstack1l111ll_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡴࡦࡴࡢࡨࡦࡺࡥ᯲ࠣ"): repo.head.commit.committed_datetime.isoformat(),
            bstack1l111ll_opy_ (u"ࠣࡣࡸࡸ࡭ࡵࡲ᯳ࠣ"): bstack1111ll1ll11_opy_(repo.head.commit.author),
            bstack1l111ll_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࡡࡧࡥࡹ࡫ࠢ᯴"): repo.head.commit.authored_datetime.isoformat(),
            bstack1l111ll_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡢࡱࡪࡹࡳࡢࡩࡨࠦ᯵"): repo.head.commit.message,
            bstack1l111ll_opy_ (u"ࠦࡷࡵ࡯ࡵࠤ᯶"): repo.git.rev_parse(bstack1l111ll_opy_ (u"ࠧ࠳࠭ࡴࡪࡲࡻ࠲ࡺ࡯ࡱ࡮ࡨࡺࡪࡲࠢ᯷")),
            bstack1l111ll_opy_ (u"ࠨࡣࡰ࡯ࡰࡳࡳࡥࡧࡪࡶࡢࡨ࡮ࡸࠢ᯸"): bstack1111l1l11l1_opy_,
            bstack1l111ll_opy_ (u"ࠢࡸࡱࡵ࡯ࡹࡸࡥࡦࡡࡪ࡭ࡹࡥࡤࡪࡴࠥ᯹"): subprocess.check_output([bstack1l111ll_opy_ (u"ࠣࡩ࡬ࡸࠧ᯺"), bstack1l111ll_opy_ (u"ࠤࡵࡩࡻ࠳ࡰࡢࡴࡶࡩࠧ᯻"), bstack1l111ll_opy_ (u"ࠥ࠱࠲࡭ࡩࡵ࠯ࡦࡳࡲࡳ࡯࡯࠯ࡧ࡭ࡷࠨ᯼")]).strip().decode(
                bstack1l111ll_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪ᯽")),
            bstack1l111ll_opy_ (u"ࠧࡲࡡࡴࡶࡢࡸࡦ࡭ࠢ᯾"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack1l111ll_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡹ࡟ࡴ࡫ࡱࡧࡪࡥ࡬ࡢࡵࡷࡣࡹࡧࡧࠣ᯿"): repo.git.rev_list(
                bstack1l111ll_opy_ (u"ࠢࡼࡿ࠱࠲ࢀࢃࠢᰀ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack1111l1l111l_opy_ = []
        for remote in remotes:
            bstack1111l11ll1l_opy_ = {
                bstack1l111ll_opy_ (u"ࠣࡰࡤࡱࡪࠨᰁ"): remote.name,
                bstack1l111ll_opy_ (u"ࠤࡸࡶࡱࠨᰂ"): remote.url,
            }
            bstack1111l1l111l_opy_.append(bstack1111l11ll1l_opy_)
        bstack111l1ll11ll_opy_ = {
            bstack1l111ll_opy_ (u"ࠥࡲࡦࡳࡥࠣᰃ"): bstack1l111ll_opy_ (u"ࠦ࡬࡯ࡴࠣᰄ"),
            **info,
            bstack1l111ll_opy_ (u"ࠧࡸࡥ࡮ࡱࡷࡩࡸࠨᰅ"): bstack1111l1l111l_opy_
        }
        bstack111l1ll11ll_opy_ = bstack111l1l11l1l_opy_(bstack111l1ll11ll_opy_)
        return bstack111l1ll11ll_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack1l111ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡯ࡱࡷ࡯ࡥࡹ࡯࡮ࡨࠢࡊ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡹ࡬ࡸ࡭ࠦࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠤᰆ").format(err))
        return {}
def bstack11ll1lll11l_opy_(bstack1111lll1l11_opy_=None):
    bstack1l111ll_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡈࡧࡷࠤ࡬࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡷࡵ࡫ࡣࡪࡨ࡬ࡧࡦࡲ࡬ࡺࠢࡩࡳࡷࡳࡡࡵࡶࡨࡨࠥ࡬࡯ࡳࠢࡄࡍࠥࡹࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠡࡷࡶࡩࠥࡩࡡࡴࡧࡶࠤ࡫ࡵࡲࠡࡧࡤࡧ࡭ࠦࡦࡰ࡮ࡧࡩࡷࠦࡩ࡯ࠢࡷ࡬ࡪࠦ࡬ࡪࡵࡷ࠲ࠏࠦࠠࠡࠢࡄࡶ࡬ࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡩࡳࡱࡪࡥࡳࡵࠣࠬࡱ࡯ࡳࡵ࠮ࠣࡳࡵࡺࡩࡰࡰࡤࡰ࠮ࡀࠠࡍ࡫ࡶࡸࠥࡵࡦࠡࡨࡲࡰࡩ࡫ࡲࠡࡲࡤࡸ࡭ࡹࠠࡵࡱࠣࡩࡽࡺࡲࡢࡥࡷࠤ࡬࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡪࡷࡵ࡭࠯ࠢࡇࡩ࡫ࡧࡵ࡭ࡶࡶࠤࡹࡵࠠ࡜ࡱࡶ࠲࡬࡫ࡴࡤࡹࡧࠬ࠮ࡣ࠮ࠋࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡮࡬ࡷࡹࡀࠠࡍ࡫ࡶࡸࠥࡵࡦࠡࡦ࡬ࡧࡹࡹࠬࠡࡧࡤࡧ࡭ࠦࡣࡰࡰࡷࡥ࡮ࡴࡩ࡯ࡩࠣ࡫࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡩࡳࡷࠦࡡࠡࡨࡲࡰࡩ࡫ࡲ࠯ࠌࠣࠤࠥࠦࠢࠣࠤᰇ")
    if bstack1111lll1l11_opy_ == None: # bstack111l1ll1l1l_opy_ for bstack11ll1l1ll11_opy_-repo
        bstack1111lll1l11_opy_ = [os.getcwd()]
    results = []
    for folder in bstack1111lll1l11_opy_:
        try:
            repo = git.Repo(folder, search_parent_directories=True)
            result = {
                bstack1l111ll_opy_ (u"ࠣࡲࡵࡍࡩࠨᰈ"): bstack1l111ll_opy_ (u"ࠤࠥᰉ"),
                bstack1l111ll_opy_ (u"ࠥࡪ࡮ࡲࡥࡴࡅ࡫ࡥࡳ࡭ࡥࡥࠤᰊ"): [],
                bstack1l111ll_opy_ (u"ࠦࡦࡻࡴࡩࡱࡵࡷࠧᰋ"): [],
                bstack1l111ll_opy_ (u"ࠧࡶࡲࡅࡣࡷࡩࠧᰌ"): bstack1l111ll_opy_ (u"ࠨࠢᰍ"),
                bstack1l111ll_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡍࡦࡵࡶࡥ࡬࡫ࡳࠣᰎ"): [],
                bstack1l111ll_opy_ (u"ࠣࡲࡵࡘ࡮ࡺ࡬ࡦࠤᰏ"): bstack1l111ll_opy_ (u"ࠤࠥᰐ"),
                bstack1l111ll_opy_ (u"ࠥࡴࡷࡊࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠥᰑ"): bstack1l111ll_opy_ (u"ࠦࠧᰒ"),
                bstack1l111ll_opy_ (u"ࠧࡶࡲࡓࡣࡺࡈ࡮࡬ࡦࠣᰓ"): bstack1l111ll_opy_ (u"ࠨࠢᰔ")
            }
            bstack111l1ll1ll1_opy_ = repo.active_branch.name
            bstack1111ll11l1l_opy_ = repo.head.commit
            result[bstack1l111ll_opy_ (u"ࠢࡱࡴࡌࡨࠧᰕ")] = bstack1111ll11l1l_opy_.hexsha
            bstack1111lll1lll_opy_ = _1111lll1l1l_opy_(repo)
            logger.debug(bstack1l111ll_opy_ (u"ࠣࡄࡤࡷࡪࠦࡢࡳࡣࡱࡧ࡭ࠦࡦࡰࡴࠣࡧࡴࡳࡰࡢࡴ࡬ࡷࡴࡴ࠺ࠡࠤᰖ") + str(bstack1111lll1lll_opy_) + bstack1l111ll_opy_ (u"ࠤࠥᰗ"))
            if bstack1111lll1lll_opy_:
                try:
                    bstack1111l1ll1l1_opy_ = repo.git.diff(bstack1l111ll_opy_ (u"ࠥ࠱࠲ࡴࡡ࡮ࡧ࠰ࡳࡳࡲࡹࠣᰘ"), bstack1lll11lllll_opy_ (u"ࠦࢀࡨࡡࡴࡧࡢࡦࡷࡧ࡮ࡤࡪࢀ࠲࠳࠴ࡻࡤࡷࡵࡶࡪࡴࡴࡠࡤࡵࡥࡳࡩࡨࡾࠤᰙ")).split(bstack1l111ll_opy_ (u"ࠬࡢ࡮ࠨᰚ"))
                    logger.debug(bstack1l111ll_opy_ (u"ࠨࡃࡩࡣࡱ࡫ࡪࡪࠠࡧ࡫࡯ࡩࡸࠦࡢࡦࡶࡺࡩࡪࡴࠠࡼࡤࡤࡷࡪࡥࡢࡳࡣࡱࡧ࡭ࢃࠠࡢࡰࡧࠤࢀࡩࡵࡳࡴࡨࡲࡹࡥࡢࡳࡣࡱࡧ࡭ࢃ࠺ࠡࠤᰛ") + str(bstack1111l1ll1l1_opy_) + bstack1l111ll_opy_ (u"ࠢࠣᰜ"))
                    result[bstack1l111ll_opy_ (u"ࠣࡨ࡬ࡰࡪࡹࡃࡩࡣࡱ࡫ࡪࡪࠢᰝ")] = [f.strip() for f in bstack1111l1ll1l1_opy_ if f.strip()]
                    commits = list(repo.iter_commits(bstack1lll11lllll_opy_ (u"ࠤࡾࡦࡦࡹࡥࡠࡤࡵࡥࡳࡩࡨࡾ࠰࠱ࡿࡨࡻࡲࡳࡧࡱࡸࡤࡨࡲࡢࡰࡦ࡬ࢂࠨᰞ")))
                except Exception:
                    logger.debug(bstack1l111ll_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡧࡦࡶࠣࡧ࡭ࡧ࡮ࡨࡧࡧࠤ࡫࡯࡬ࡦࡵࠣࡪࡷࡵ࡭ࠡࡤࡵࡥࡳࡩࡨࠡࡥࡲࡱࡵࡧࡲࡪࡵࡲࡲ࠳ࠦࡆࡢ࡮࡯࡭ࡳ࡭ࠠࡣࡣࡦ࡯ࠥࡺ࡯ࠡࡴࡨࡧࡪࡴࡴࠡࡥࡲࡱࡲ࡯ࡴࡴ࠰ࠥᰟ"))
                    commits = list(repo.iter_commits(max_count=10))
                    if commits:
                        result[bstack1l111ll_opy_ (u"ࠦ࡫࡯࡬ࡦࡵࡆ࡬ࡦࡴࡧࡦࡦࠥᰠ")] = _111l11111ll_opy_(commits[:5])
            else:
                commits = list(repo.iter_commits(max_count=10))
                if commits:
                    result[bstack1l111ll_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡶࡇ࡭ࡧ࡮ࡨࡧࡧࠦᰡ")] = _111l11111ll_opy_(commits[:5])
            bstack1111l111ll1_opy_ = set()
            bstack1111ll1111l_opy_ = []
            for commit in commits:
                logger.debug(bstack1l111ll_opy_ (u"ࠨࡐࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡧࡴࡳ࡭ࡪࡶ࠽ࠤࠧᰢ") + str(commit.message) + bstack1l111ll_opy_ (u"ࠢࠣᰣ"))
                bstack1111lllll11_opy_ = commit.author.name if commit.author else bstack1l111ll_opy_ (u"ࠣࡗࡱ࡯ࡳࡵࡷ࡯ࠤᰤ")
                bstack1111l111ll1_opy_.add(bstack1111lllll11_opy_)
                bstack1111ll1111l_opy_.append({
                    bstack1l111ll_opy_ (u"ࠤࡰࡩࡸࡹࡡࡨࡧࠥᰥ"): commit.message.strip(),
                    bstack1l111ll_opy_ (u"ࠥࡹࡸ࡫ࡲࠣᰦ"): bstack1111lllll11_opy_
                })
            result[bstack1l111ll_opy_ (u"ࠦࡦࡻࡴࡩࡱࡵࡷࠧᰧ")] = list(bstack1111l111ll1_opy_)
            result[bstack1l111ll_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡒ࡫ࡳࡴࡣࡪࡩࡸࠨᰨ")] = bstack1111ll1111l_opy_
            result[bstack1l111ll_opy_ (u"ࠨࡰࡳࡆࡤࡸࡪࠨᰩ")] = bstack1111ll11l1l_opy_.committed_datetime.strftime(bstack1l111ll_opy_ (u"࡛ࠢࠦ࠰ࠩࡲ࠳ࠥࡥࠤᰪ"))
            if (not result[bstack1l111ll_opy_ (u"ࠣࡲࡵࡘ࡮ࡺ࡬ࡦࠤᰫ")] or result[bstack1l111ll_opy_ (u"ࠤࡳࡶ࡙࡯ࡴ࡭ࡧࠥᰬ")].strip() == bstack1l111ll_opy_ (u"ࠥࠦᰭ")) and bstack1111ll11l1l_opy_.message:
                bstack1111ll1ll1l_opy_ = bstack1111ll11l1l_opy_.message.strip().splitlines()
                result[bstack1l111ll_opy_ (u"ࠦࡵࡸࡔࡪࡶ࡯ࡩࠧᰮ")] = bstack1111ll1ll1l_opy_[0] if bstack1111ll1ll1l_opy_ else bstack1l111ll_opy_ (u"ࠧࠨᰯ")
                if len(bstack1111ll1ll1l_opy_) > 2:
                    result[bstack1l111ll_opy_ (u"ࠨࡰࡳࡆࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳࠨᰰ")] = bstack1l111ll_opy_ (u"ࠧ࡝ࡰࠪᰱ").join(bstack1111ll1ll1l_opy_[2:]).strip()
            results.append(result)
        except Exception as err:
            logger.error(bstack1l111ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡱࡳࡹࡱࡧࡴࡪࡰࡪࠤࡌ࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡪࡴࡸࠠࡂࡋࠣࡷࡪࡲࡥࡤࡶ࡬ࡳࡳࠦࠨࡧࡱ࡯ࡨࡪࡸ࠺ࠡࡽࡩࡳࡱࡪࡥࡳࡿࠬ࠾ࠥࠨᰲ") + str(err) + bstack1l111ll_opy_ (u"ࠤࠥᰳ"))
    filtered_results = [
        result
        for result in results
        if _1111ll1lll1_opy_(result)
    ]
    return filtered_results
def _1111ll1lll1_opy_(result):
    bstack1l111ll_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡌࡪࡲࡰࡦࡴࠣࡸࡴࠦࡣࡩࡧࡦ࡯ࠥ࡯ࡦࠡࡣࠣ࡫࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡵࡩࡸࡻ࡬ࡵࠢ࡬ࡷࠥࡼࡡ࡭࡫ࡧࠤ࠭ࡴ࡯࡯࠯ࡨࡱࡵࡺࡹࠡࡨ࡬ࡰࡪࡹࡃࡩࡣࡱ࡫ࡪࡪࠠࡢࡰࡧࠤࡦࡻࡴࡩࡱࡵࡷ࠮࠴ࠊࠡࠢࠣࠤࠧࠨࠢᰴ")
    return (
        isinstance(result.get(bstack1l111ll_opy_ (u"ࠦ࡫࡯࡬ࡦࡵࡆ࡬ࡦࡴࡧࡦࡦࠥᰵ"), None), list)
        and len(result[bstack1l111ll_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡶࡇ࡭ࡧ࡮ࡨࡧࡧࠦᰶ")]) > 0
        and isinstance(result.get(bstack1l111ll_opy_ (u"ࠨࡡࡶࡶ࡫ࡳࡷࡹ᰷ࠢ"), None), list)
        and len(result[bstack1l111ll_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸࡳࠣ᰸")]) > 0
    )
def _1111lll1l1l_opy_(repo):
    bstack1l111ll_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡖࡵࡽࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤࡹ࡮ࡥࠡࡤࡤࡷࡪࠦࡢࡳࡣࡱࡧ࡭ࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡨ࡫ࡹࡩࡳࠦࡲࡦࡲࡲࠤࡼ࡯ࡴࡩࡱࡸࡸࠥ࡮ࡡࡳࡦࡦࡳࡩ࡫ࡤࠡࡰࡤࡱࡪࡹࠠࡢࡰࡧࠤࡼࡵࡲ࡬ࠢࡺ࡭ࡹ࡮ࠠࡢ࡮࡯ࠤ࡛ࡉࡓࠡࡲࡵࡳࡻ࡯ࡤࡦࡴࡶ࠲ࠏࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵࠣࡸ࡭࡫ࠠࡥࡧࡩࡥࡺࡲࡴࠡࡤࡵࡥࡳࡩࡨࠡ࡫ࡩࠤࡵࡵࡳࡴ࡫ࡥࡰࡪ࠲ࠠࡦ࡮ࡶࡩࠥࡔ࡯࡯ࡧ࠱ࠎࠥࠦࠠࠡࠤࠥࠦ᰹")
    try:
        try:
            origin = repo.remotes.origin
            bstack1111llll1l1_opy_ = origin.refs[bstack1l111ll_opy_ (u"ࠩࡋࡉࡆࡊࠧ᰺")]
            target = bstack1111llll1l1_opy_.reference.name
            if target.startswith(bstack1l111ll_opy_ (u"ࠪࡳࡷ࡯ࡧࡪࡰ࠲ࠫ᰻")):
                return target
        except Exception:
            pass
        if repo.remotes and repo.remotes.origin.refs:
            for ref in repo.remotes.origin.refs:
                if ref.name.startswith(bstack1l111ll_opy_ (u"ࠫࡴࡸࡩࡨ࡫ࡱ࠳ࠬ᰼")):
                    return ref.name
        if repo.heads:
            return repo.heads[0].name
    except Exception:
        pass
    return None
def _111l11111ll_opy_(commits):
    bstack1l111ll_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡍࡥࡵࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡧ࡭ࡧ࡮ࡨࡧࡧࠤ࡫࡯࡬ࡦࡵࠣࡪࡷࡵ࡭ࠡࡣࠣࡰ࡮ࡹࡴࠡࡱࡩࠤࡨࡵ࡭࡮࡫ࡷࡷ࠳ࠐࠠࠡࠢࠣࠦࠧࠨ᰽")
    bstack1111l1ll1l1_opy_ = set()
    try:
        for commit in commits:
            if commit.parents:
                for parent in commit.parents:
                    diff = commit.diff(parent)
                    for bstack1111lll11ll_opy_ in diff:
                        if bstack1111lll11ll_opy_.a_path:
                            bstack1111l1ll1l1_opy_.add(bstack1111lll11ll_opy_.a_path)
                        if bstack1111lll11ll_opy_.b_path:
                            bstack1111l1ll1l1_opy_.add(bstack1111lll11ll_opy_.b_path)
    except Exception:
        pass
    return list(bstack1111l1ll1l1_opy_)
def bstack111l1l11l1l_opy_(bstack111l1ll11ll_opy_):
    bstack111l111l11l_opy_ = bstack1111l1l1ll1_opy_(bstack111l1ll11ll_opy_)
    if bstack111l111l11l_opy_ and bstack111l111l11l_opy_ > bstack11l11l1lll1_opy_:
        bstack1111llll1ll_opy_ = bstack111l111l11l_opy_ - bstack11l11l1lll1_opy_
        bstack1111ll11l11_opy_ = bstack111l1ll1l11_opy_(bstack111l1ll11ll_opy_[bstack1l111ll_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡥ࡭ࡦࡵࡶࡥ࡬࡫ࠢ᰾")], bstack1111llll1ll_opy_)
        bstack111l1ll11ll_opy_[bstack1l111ll_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠣ᰿")] = bstack1111ll11l11_opy_
        logger.info(bstack1l111ll_opy_ (u"ࠣࡖ࡫ࡩࠥࡩ࡯࡮࡯࡬ࡸࠥ࡮ࡡࡴࠢࡥࡩࡪࡴࠠࡵࡴࡸࡲࡨࡧࡴࡦࡦ࠱ࠤࡘ࡯ࡺࡦࠢࡲࡪࠥࡩ࡯࡮࡯࡬ࡸࠥࡧࡦࡵࡧࡵࠤࡹࡸࡵ࡯ࡥࡤࡸ࡮ࡵ࡮ࠡ࡫ࡶࠤࢀࢃࠠࡌࡄࠥ᱀")
                    .format(bstack1111l1l1ll1_opy_(bstack111l1ll11ll_opy_) / 1024))
    return bstack111l1ll11ll_opy_
def bstack1111l1l1ll1_opy_(json_data):
    try:
        if json_data:
            bstack111l11l1111_opy_ = json.dumps(json_data)
            bstack111l111llll_opy_ = sys.getsizeof(bstack111l11l1111_opy_)
            return bstack111l111llll_opy_
    except Exception as e:
        logger.debug(bstack1l111ll_opy_ (u"ࠤࡖࡳࡲ࡫ࡴࡩ࡫ࡱ࡫ࠥࡽࡥ࡯ࡶࠣࡻࡷࡵ࡮ࡨࠢࡺ࡬࡮ࡲࡥࠡࡥࡤࡰࡨࡻ࡬ࡢࡶ࡬ࡲ࡬ࠦࡳࡪࡼࡨࠤࡴ࡬ࠠࡋࡕࡒࡒࠥࡵࡢ࡫ࡧࡦࡸ࠿ࠦࡻࡾࠤ᱁").format(e))
    return -1
def bstack111l1ll1l11_opy_(field, bstack1111l1l1l11_opy_):
    try:
        bstack1111l11l111_opy_ = len(bytes(bstack11l11l1llll_opy_, bstack1l111ll_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩ᱂")))
        bstack111l1l11l11_opy_ = bytes(field, bstack1l111ll_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪ᱃"))
        bstack1111l11l1ll_opy_ = len(bstack111l1l11l11_opy_)
        bstack111l1l1l1ll_opy_ = ceil(bstack1111l11l1ll_opy_ - bstack1111l1l1l11_opy_ - bstack1111l11l111_opy_)
        if bstack111l1l1l1ll_opy_ > 0:
            bstack111l1l1l111_opy_ = bstack111l1l11l11_opy_[:bstack111l1l1l1ll_opy_].decode(bstack1l111ll_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫ᱄"), errors=bstack1l111ll_opy_ (u"࠭ࡩࡨࡰࡲࡶࡪ࠭᱅")) + bstack11l11l1llll_opy_
            return bstack111l1l1l111_opy_
    except Exception as e:
        logger.debug(bstack1l111ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡺࡲࡶࡰࡦࡥࡹ࡯࡮ࡨࠢࡩ࡭ࡪࡲࡤ࠭ࠢࡱࡳࡹ࡮ࡩ࡯ࡩࠣࡻࡦࡹࠠࡵࡴࡸࡲࡨࡧࡴࡦࡦࠣ࡬ࡪࡸࡥ࠻ࠢࡾࢁࠧ᱆").format(e))
    return field
def bstack11ll111lll_opy_():
    env = os.environ
    if (bstack1l111ll_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡘࡖࡑࠨ᱇") in env and len(env[bstack1l111ll_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢ࡙ࡗࡒࠢ᱈")]) > 0) or (
            bstack1l111ll_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣࡍࡕࡍࡆࠤ᱉") in env and len(env[bstack1l111ll_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤࡎࡏࡎࡇࠥ᱊")]) > 0):
        return {
            bstack1l111ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᱋"): bstack1l111ll_opy_ (u"ࠨࡊࡦࡰ࡮࡭ࡳࡹࠢ᱌"),
            bstack1l111ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᱍ"): env.get(bstack1l111ll_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦᱎ")),
            bstack1l111ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᱏ"): env.get(bstack1l111ll_opy_ (u"ࠥࡎࡔࡈ࡟ࡏࡃࡐࡉࠧ᱐")),
            bstack1l111ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ᱑"): env.get(bstack1l111ll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦ᱒"))
        }
    if env.get(bstack1l111ll_opy_ (u"ࠨࡃࡊࠤ᱓")) == bstack1l111ll_opy_ (u"ࠢࡵࡴࡸࡩࠧ᱔") and bstack1lll1l1ll1_opy_(env.get(bstack1l111ll_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡄࡋࠥ᱕"))):
        return {
            bstack1l111ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᱖"): bstack1l111ll_opy_ (u"ࠥࡇ࡮ࡸࡣ࡭ࡧࡆࡍࠧ᱗"),
            bstack1l111ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ᱘"): env.get(bstack1l111ll_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣ᱙")),
            bstack1l111ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᱚ"): env.get(bstack1l111ll_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋ࡟ࡋࡑࡅࠦᱛ")),
            bstack1l111ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᱜ"): env.get(bstack1l111ll_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࠧᱝ"))
        }
    if env.get(bstack1l111ll_opy_ (u"ࠥࡇࡎࠨᱞ")) == bstack1l111ll_opy_ (u"ࠦࡹࡸࡵࡦࠤᱟ") and bstack1lll1l1ll1_opy_(env.get(bstack1l111ll_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࠧᱠ"))):
        return {
            bstack1l111ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᱡ"): bstack1l111ll_opy_ (u"ࠢࡕࡴࡤࡺ࡮ࡹࠠࡄࡋࠥᱢ"),
            bstack1l111ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᱣ"): env.get(bstack1l111ll_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࡡࡅ࡙ࡎࡒࡄࡠ࡙ࡈࡆࡤ࡛ࡒࡍࠤᱤ")),
            bstack1l111ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᱥ"): env.get(bstack1l111ll_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᱦ")),
            bstack1l111ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᱧ"): env.get(bstack1l111ll_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᱨ"))
        }
    if env.get(bstack1l111ll_opy_ (u"ࠢࡄࡋࠥᱩ")) == bstack1l111ll_opy_ (u"ࠣࡶࡵࡹࡪࠨᱪ") and env.get(bstack1l111ll_opy_ (u"ࠤࡆࡍࡤࡔࡁࡎࡇࠥᱫ")) == bstack1l111ll_opy_ (u"ࠥࡧࡴࡪࡥࡴࡪ࡬ࡴࠧᱬ"):
        return {
            bstack1l111ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᱭ"): bstack1l111ll_opy_ (u"ࠧࡉ࡯ࡥࡧࡶ࡬࡮ࡶࠢᱮ"),
            bstack1l111ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᱯ"): None,
            bstack1l111ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᱰ"): None,
            bstack1l111ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᱱ"): None
        }
    if env.get(bstack1l111ll_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡈࡒࡂࡐࡆࡌࠧᱲ")) and env.get(bstack1l111ll_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡃࡐࡏࡐࡍ࡙ࠨᱳ")):
        return {
            bstack1l111ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᱴ"): bstack1l111ll_opy_ (u"ࠧࡈࡩࡵࡤࡸࡧࡰ࡫ࡴࠣᱵ"),
            bstack1l111ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᱶ"): env.get(bstack1l111ll_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡋࡎ࡚࡟ࡉࡖࡗࡔࡤࡕࡒࡊࡉࡌࡒࠧᱷ")),
            bstack1l111ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᱸ"): None,
            bstack1l111ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᱹ"): env.get(bstack1l111ll_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᱺ"))
        }
    if env.get(bstack1l111ll_opy_ (u"ࠦࡈࡏࠢᱻ")) == bstack1l111ll_opy_ (u"ࠧࡺࡲࡶࡧࠥᱼ") and bstack1lll1l1ll1_opy_(env.get(bstack1l111ll_opy_ (u"ࠨࡄࡓࡑࡑࡉࠧᱽ"))):
        return {
            bstack1l111ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᱾"): bstack1l111ll_opy_ (u"ࠣࡆࡵࡳࡳ࡫ࠢ᱿"),
            bstack1l111ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᲀ"): env.get(bstack1l111ll_opy_ (u"ࠥࡈࡗࡕࡎࡆࡡࡅ࡙ࡎࡒࡄࡠࡎࡌࡒࡐࠨᲁ")),
            bstack1l111ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᲂ"): None,
            bstack1l111ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᲃ"): env.get(bstack1l111ll_opy_ (u"ࠨࡄࡓࡑࡑࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᲄ"))
        }
    if env.get(bstack1l111ll_opy_ (u"ࠢࡄࡋࠥᲅ")) == bstack1l111ll_opy_ (u"ࠣࡶࡵࡹࡪࠨᲆ") and bstack1lll1l1ll1_opy_(env.get(bstack1l111ll_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࠧᲇ"))):
        return {
            bstack1l111ll_opy_ (u"ࠥࡲࡦࡳࡥࠣᲈ"): bstack1l111ll_opy_ (u"ࠦࡘ࡫࡭ࡢࡲ࡫ࡳࡷ࡫ࠢᲉ"),
            bstack1l111ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᲊ"): env.get(bstack1l111ll_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࡡࡒࡖࡌࡇࡎࡊ࡜ࡄࡘࡎࡕࡎࡠࡗࡕࡐࠧ᲋")),
            bstack1l111ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᲌"): env.get(bstack1l111ll_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨ᲍")),
            bstack1l111ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᲎"): env.get(bstack1l111ll_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࡥࡊࡐࡄࡢࡍࡉࠨ᲏"))
        }
    if env.get(bstack1l111ll_opy_ (u"ࠦࡈࡏࠢᲐ")) == bstack1l111ll_opy_ (u"ࠧࡺࡲࡶࡧࠥᲑ") and bstack1lll1l1ll1_opy_(env.get(bstack1l111ll_opy_ (u"ࠨࡇࡊࡖࡏࡅࡇࡥࡃࡊࠤᲒ"))):
        return {
            bstack1l111ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᲓ"): bstack1l111ll_opy_ (u"ࠣࡉ࡬ࡸࡑࡧࡢࠣᲔ"),
            bstack1l111ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᲕ"): env.get(bstack1l111ll_opy_ (u"ࠥࡇࡎࡥࡊࡐࡄࡢ࡙ࡗࡒࠢᲖ")),
            bstack1l111ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᲗ"): env.get(bstack1l111ll_opy_ (u"ࠧࡉࡉࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᲘ")),
            bstack1l111ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᲙ"): env.get(bstack1l111ll_opy_ (u"ࠢࡄࡋࡢࡎࡔࡈ࡟ࡊࡆࠥᲚ"))
        }
    if env.get(bstack1l111ll_opy_ (u"ࠣࡅࡌࠦᲛ")) == bstack1l111ll_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᲜ") and bstack1lll1l1ll1_opy_(env.get(bstack1l111ll_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࠨᲝ"))):
        return {
            bstack1l111ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᲞ"): bstack1l111ll_opy_ (u"ࠧࡈࡵࡪ࡮ࡧ࡯࡮ࡺࡥࠣᲟ"),
            bstack1l111ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᲠ"): env.get(bstack1l111ll_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᲡ")),
            bstack1l111ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᲢ"): env.get(bstack1l111ll_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡒࡁࡃࡇࡏࠦᲣ")) or env.get(bstack1l111ll_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡐࡄࡑࡊࠨᲤ")),
            bstack1l111ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᲥ"): env.get(bstack1l111ll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᲦ"))
        }
    if bstack1lll1l1ll1_opy_(env.get(bstack1l111ll_opy_ (u"ࠨࡔࡇࡡࡅ࡙ࡎࡒࡄࠣᲧ"))):
        return {
            bstack1l111ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᲨ"): bstack1l111ll_opy_ (u"ࠣࡘ࡬ࡷࡺࡧ࡬ࠡࡕࡷࡹࡩ࡯࡯ࠡࡖࡨࡥࡲࠦࡓࡦࡴࡹ࡭ࡨ࡫ࡳࠣᲩ"),
            bstack1l111ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᲪ"): bstack1l111ll_opy_ (u"ࠥࡿࢂࢁࡽࠣᲫ").format(env.get(bstack1l111ll_opy_ (u"ࠫࡘ࡟ࡓࡕࡇࡐࡣ࡙ࡋࡁࡎࡈࡒ࡙ࡓࡊࡁࡕࡋࡒࡒࡘࡋࡒࡗࡇࡕ࡙ࡗࡏࠧᲬ")), env.get(bstack1l111ll_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡓࡖࡔࡐࡅࡄࡖࡌࡈࠬᲭ"))),
            bstack1l111ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᲮ"): env.get(bstack1l111ll_opy_ (u"ࠢࡔ࡛ࡖࡘࡊࡓ࡟ࡅࡇࡉࡍࡓࡏࡔࡊࡑࡑࡍࡉࠨᲯ")),
            bstack1l111ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᲰ"): env.get(bstack1l111ll_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠤᲱ"))
        }
    if bstack1lll1l1ll1_opy_(env.get(bstack1l111ll_opy_ (u"ࠥࡅࡕࡖࡖࡆ࡛ࡒࡖࠧᲲ"))):
        return {
            bstack1l111ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᲳ"): bstack1l111ll_opy_ (u"ࠧࡇࡰࡱࡸࡨࡽࡴࡸࠢᲴ"),
            bstack1l111ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᲵ"): bstack1l111ll_opy_ (u"ࠢࡼࡿ࠲ࡴࡷࡵࡪࡦࡥࡷ࠳ࢀࢃ࠯ࡼࡿ࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂࠨᲶ").format(env.get(bstack1l111ll_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢ࡙ࡗࡒࠧᲷ")), env.get(bstack1l111ll_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡆࡉࡃࡐࡗࡑࡘࡤࡔࡁࡎࡇࠪᲸ")), env.get(bstack1l111ll_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡖࡒࡐࡌࡈࡇ࡙ࡥࡓࡍࡗࡊࠫᲹ")), env.get(bstack1l111ll_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨᲺ"))),
            bstack1l111ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ᲻"): env.get(bstack1l111ll_opy_ (u"ࠨࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥ᲼")),
            bstack1l111ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᲽ"): env.get(bstack1l111ll_opy_ (u"ࠣࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᲾ"))
        }
    if env.get(bstack1l111ll_opy_ (u"ࠤࡄ࡞࡚ࡘࡅࡠࡊࡗࡘࡕࡥࡕࡔࡇࡕࡣࡆࡍࡅࡏࡖࠥᲿ")) and env.get(bstack1l111ll_opy_ (u"ࠥࡘࡋࡥࡂࡖࡋࡏࡈࠧ᳀")):
        return {
            bstack1l111ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᳁"): bstack1l111ll_opy_ (u"ࠧࡇࡺࡶࡴࡨࠤࡈࡏࠢ᳂"),
            bstack1l111ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᳃"): bstack1l111ll_opy_ (u"ࠢࡼࡿࡾࢁ࠴ࡥࡢࡶ࡫࡯ࡨ࠴ࡸࡥࡴࡷ࡯ࡸࡸࡅࡢࡶ࡫࡯ࡨࡎࡪ࠽ࡼࡿࠥ᳄").format(env.get(bstack1l111ll_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡌࡏࡖࡐࡇࡅ࡙ࡏࡏࡏࡕࡈࡖ࡛ࡋࡒࡖࡔࡌࠫ᳅")), env.get(bstack1l111ll_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡐࡓࡑࡍࡉࡈ࡚ࠧ᳆")), env.get(bstack1l111ll_opy_ (u"ࠪࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠪ᳇"))),
            bstack1l111ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᳈"): env.get(bstack1l111ll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠧ᳉")),
            bstack1l111ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ᳊"): env.get(bstack1l111ll_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠢ᳋"))
        }
    if any([env.get(bstack1l111ll_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨ᳌")), env.get(bstack1l111ll_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡘࡅࡔࡑࡏ࡚ࡊࡊ࡟ࡔࡑࡘࡖࡈࡋ࡟ࡗࡇࡕࡗࡎࡕࡎࠣ᳍")), env.get(bstack1l111ll_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡓࡐࡗࡕࡇࡊࡥࡖࡆࡔࡖࡍࡔࡔࠢ᳎"))]):
        return {
            bstack1l111ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᳏"): bstack1l111ll_opy_ (u"ࠧࡇࡗࡔࠢࡆࡳࡩ࡫ࡂࡶ࡫࡯ࡨࠧ᳐"),
            bstack1l111ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᳑"): env.get(bstack1l111ll_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡔ࡚ࡈࡌࡊࡅࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨ᳒")),
            bstack1l111ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᳓"): env.get(bstack1l111ll_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊ᳔ࠢ")),
            bstack1l111ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᳕"): env.get(bstack1l111ll_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤ᳖"))
        }
    if env.get(bstack1l111ll_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡨࡵࡪ࡮ࡧࡒࡺࡳࡢࡦࡴ᳗ࠥ")):
        return {
            bstack1l111ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨ᳘ࠦ"): bstack1l111ll_opy_ (u"ࠢࡃࡣࡰࡦࡴࡵ᳙ࠢ"),
            bstack1l111ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ᳚"): env.get(bstack1l111ll_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡥࡹ࡮ࡲࡤࡓࡧࡶࡹࡱࡺࡳࡖࡴ࡯ࠦ᳛")),
            bstack1l111ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩ᳜ࠧ"): env.get(bstack1l111ll_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡸ࡮࡯ࡳࡶࡍࡳࡧࡔࡡ࡮ࡧ᳝ࠥ")),
            bstack1l111ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵ᳞ࠦ"): env.get(bstack1l111ll_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡢࡶ࡫࡯ࡨࡓࡻ࡭ࡣࡧࡵ᳟ࠦ"))
        }
    if env.get(bstack1l111ll_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࠣ᳠")) or env.get(bstack1l111ll_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡐࡅࡎࡔ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡖࡘࡆࡘࡔࡆࡆࠥ᳡")):
        return {
            bstack1l111ll_opy_ (u"ࠤࡱࡥࡲ࡫᳢ࠢ"): bstack1l111ll_opy_ (u"࡛ࠥࡪࡸࡣ࡬ࡧࡵ᳣ࠦ"),
            bstack1l111ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲ᳤ࠢ"): env.get(bstack1l111ll_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤ᳥")),
            bstack1l111ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥ᳦ࠣ"): bstack1l111ll_opy_ (u"ࠢࡎࡣ࡬ࡲࠥࡖࡩࡱࡧ࡯࡭ࡳ࡫᳧ࠢ") if env.get(bstack1l111ll_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡐࡅࡎࡔ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡖࡘࡆࡘࡔࡆࡆ᳨ࠥ")) else None,
            bstack1l111ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᳩ"): env.get(bstack1l111ll_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡌࡏࡔࡠࡅࡒࡑࡒࡏࡔࠣᳪ"))
        }
    if any([env.get(bstack1l111ll_opy_ (u"ࠦࡌࡉࡐࡠࡒࡕࡓࡏࡋࡃࡕࠤᳫ")), env.get(bstack1l111ll_opy_ (u"ࠧࡍࡃࡍࡑࡘࡈࡤࡖࡒࡐࡌࡈࡇ࡙ࠨᳬ")), env.get(bstack1l111ll_opy_ (u"ࠨࡇࡐࡑࡊࡐࡊࡥࡃࡍࡑࡘࡈࡤࡖࡒࡐࡌࡈࡇ࡙ࠨ᳭"))]):
        return {
            bstack1l111ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᳮ"): bstack1l111ll_opy_ (u"ࠣࡉࡲࡳ࡬ࡲࡥࠡࡅ࡯ࡳࡺࡪࠢᳯ"),
            bstack1l111ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᳰ"): None,
            bstack1l111ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᳱ"): env.get(bstack1l111ll_opy_ (u"ࠦࡕࡘࡏࡋࡇࡆࡘࡤࡏࡄࠣᳲ")),
            bstack1l111ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᳳ"): env.get(bstack1l111ll_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡏࡄࠣ᳴"))
        }
    if env.get(bstack1l111ll_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࠥᳵ")):
        return {
            bstack1l111ll_opy_ (u"ࠣࡰࡤࡱࡪࠨᳶ"): bstack1l111ll_opy_ (u"ࠤࡖ࡬࡮ࡶࡰࡢࡤ࡯ࡩࠧ᳷"),
            bstack1l111ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᳸"): env.get(bstack1l111ll_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥ᳹")),
            bstack1l111ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᳺ"): bstack1l111ll_opy_ (u"ࠨࡊࡰࡤࠣࠧࢀࢃࠢ᳻").format(env.get(bstack1l111ll_opy_ (u"ࠧࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡎࡔࡈ࡟ࡊࡆࠪ᳼"))) if env.get(bstack1l111ll_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡏࡕࡂࡠࡋࡇࠦ᳽")) else None,
            bstack1l111ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᳾"): env.get(bstack1l111ll_opy_ (u"ࠥࡗࡍࡏࡐࡑࡃࡅࡐࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧ᳿"))
        }
    if bstack1lll1l1ll1_opy_(env.get(bstack1l111ll_opy_ (u"ࠦࡓࡋࡔࡍࡋࡉ࡝ࠧᴀ"))):
        return {
            bstack1l111ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᴁ"): bstack1l111ll_opy_ (u"ࠨࡎࡦࡶ࡯࡭࡫ࡿࠢᴂ"),
            bstack1l111ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᴃ"): env.get(bstack1l111ll_opy_ (u"ࠣࡆࡈࡔࡑࡕ࡙ࡠࡗࡕࡐࠧᴄ")),
            bstack1l111ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᴅ"): env.get(bstack1l111ll_opy_ (u"ࠥࡗࡎ࡚ࡅࡠࡐࡄࡑࡊࠨᴆ")),
            bstack1l111ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᴇ"): env.get(bstack1l111ll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢᴈ"))
        }
    if bstack1lll1l1ll1_opy_(env.get(bstack1l111ll_opy_ (u"ࠨࡇࡊࡖࡋ࡙ࡇࡥࡁࡄࡖࡌࡓࡓ࡙ࠢᴉ"))):
        return {
            bstack1l111ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᴊ"): bstack1l111ll_opy_ (u"ࠣࡉ࡬ࡸࡍࡻࡢࠡࡃࡦࡸ࡮ࡵ࡮ࡴࠤᴋ"),
            bstack1l111ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᴌ"): bstack1l111ll_opy_ (u"ࠥࡿࢂ࠵ࡻࡾ࠱ࡤࡧࡹ࡯࡯࡯ࡵ࠲ࡶࡺࡴࡳ࠰ࡽࢀࠦᴍ").format(env.get(bstack1l111ll_opy_ (u"ࠫࡌࡏࡔࡉࡗࡅࡣࡘࡋࡒࡗࡇࡕࡣ࡚ࡘࡌࠨᴎ")), env.get(bstack1l111ll_opy_ (u"ࠬࡍࡉࡕࡊࡘࡆࡤࡘࡅࡑࡑࡖࡍ࡙ࡕࡒ࡚ࠩᴏ")), env.get(bstack1l111ll_opy_ (u"࠭ࡇࡊࡖࡋ࡙ࡇࡥࡒࡖࡐࡢࡍࡉ࠭ᴐ"))),
            bstack1l111ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᴑ"): env.get(bstack1l111ll_opy_ (u"ࠣࡉࡌࡘࡍ࡛ࡂࡠ࡙ࡒࡖࡐࡌࡌࡐ࡙ࠥᴒ")),
            bstack1l111ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᴓ"): env.get(bstack1l111ll_opy_ (u"ࠥࡋࡎ࡚ࡈࡖࡄࡢࡖ࡚ࡔ࡟ࡊࡆࠥᴔ"))
        }
    if env.get(bstack1l111ll_opy_ (u"ࠦࡈࡏࠢᴕ")) == bstack1l111ll_opy_ (u"ࠧࡺࡲࡶࡧࠥᴖ") and env.get(bstack1l111ll_opy_ (u"ࠨࡖࡆࡔࡆࡉࡑࠨᴗ")) == bstack1l111ll_opy_ (u"ࠢ࠲ࠤᴘ"):
        return {
            bstack1l111ll_opy_ (u"ࠣࡰࡤࡱࡪࠨᴙ"): bstack1l111ll_opy_ (u"ࠤ࡙ࡩࡷࡩࡥ࡭ࠤᴚ"),
            bstack1l111ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᴛ"): bstack1l111ll_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࢀࢃࠢᴜ").format(env.get(bstack1l111ll_opy_ (u"ࠬ࡜ࡅࡓࡅࡈࡐࡤ࡛ࡒࡍࠩᴝ"))),
            bstack1l111ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᴞ"): None,
            bstack1l111ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᴟ"): None,
        }
    if env.get(bstack1l111ll_opy_ (u"ࠣࡖࡈࡅࡒࡉࡉࡕ࡛ࡢ࡚ࡊࡘࡓࡊࡑࡑࠦᴠ")):
        return {
            bstack1l111ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᴡ"): bstack1l111ll_opy_ (u"ࠥࡘࡪࡧ࡭ࡤ࡫ࡷࡽࠧᴢ"),
            bstack1l111ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᴣ"): None,
            bstack1l111ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᴤ"): env.get(bstack1l111ll_opy_ (u"ࠨࡔࡆࡃࡐࡇࡎ࡚࡙ࡠࡒࡕࡓࡏࡋࡃࡕࡡࡑࡅࡒࡋࠢᴥ")),
            bstack1l111ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᴦ"): env.get(bstack1l111ll_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᴧ"))
        }
    if any([env.get(bstack1l111ll_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࠧᴨ")), env.get(bstack1l111ll_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࡥࡕࡓࡎࠥᴩ")), env.get(bstack1l111ll_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠤᴪ")), env.get(bstack1l111ll_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࡠࡖࡈࡅࡒࠨᴫ"))]):
        return {
            bstack1l111ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᴬ"): bstack1l111ll_opy_ (u"ࠢࡄࡱࡱࡧࡴࡻࡲࡴࡧࠥᴭ"),
            bstack1l111ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᴮ"): None,
            bstack1l111ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᴯ"): env.get(bstack1l111ll_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᴰ")) or None,
            bstack1l111ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᴱ"): env.get(bstack1l111ll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢᴲ"), 0)
        }
    if env.get(bstack1l111ll_opy_ (u"ࠨࡇࡐࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᴳ")):
        return {
            bstack1l111ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᴴ"): bstack1l111ll_opy_ (u"ࠣࡉࡲࡇࡉࠨᴵ"),
            bstack1l111ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᴶ"): None,
            bstack1l111ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᴷ"): env.get(bstack1l111ll_opy_ (u"ࠦࡌࡕ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᴸ")),
            bstack1l111ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᴹ"): env.get(bstack1l111ll_opy_ (u"ࠨࡇࡐࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡈࡕࡕࡏࡖࡈࡖࠧᴺ"))
        }
    if env.get(bstack1l111ll_opy_ (u"ࠢࡄࡈࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᴻ")):
        return {
            bstack1l111ll_opy_ (u"ࠣࡰࡤࡱࡪࠨᴼ"): bstack1l111ll_opy_ (u"ࠤࡆࡳࡩ࡫ࡆࡳࡧࡶ࡬ࠧᴽ"),
            bstack1l111ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᴾ"): env.get(bstack1l111ll_opy_ (u"ࠦࡈࡌ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᴿ")),
            bstack1l111ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᵀ"): env.get(bstack1l111ll_opy_ (u"ࠨࡃࡇࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡓࡇࡍࡆࠤᵁ")),
            bstack1l111ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᵂ"): env.get(bstack1l111ll_opy_ (u"ࠣࡅࡉࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᵃ"))
        }
    return {bstack1l111ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᵄ"): None}
def get_host_info():
    return {
        bstack1l111ll_opy_ (u"ࠥ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠧᵅ"): platform.node(),
        bstack1l111ll_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࠨᵆ"): platform.system(),
        bstack1l111ll_opy_ (u"ࠧࡺࡹࡱࡧࠥᵇ"): platform.machine(),
        bstack1l111ll_opy_ (u"ࠨࡶࡦࡴࡶ࡭ࡴࡴࠢᵈ"): platform.version(),
        bstack1l111ll_opy_ (u"ࠢࡢࡴࡦ࡬ࠧᵉ"): platform.architecture()[0]
    }
def bstack11l11111l1_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack111l1ll1lll_opy_():
    if bstack111l11ll_opy_.get_property(bstack1l111ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩᵊ")):
        return bstack1l111ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᵋ")
    return bstack1l111ll_opy_ (u"ࠪࡹࡳࡱ࡮ࡰࡹࡱࡣ࡬ࡸࡩࡥࠩᵌ")
def bstack1111l1l1111_opy_(driver):
    info = {
        bstack1l111ll_opy_ (u"ࠫࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪᵍ"): driver.capabilities,
        bstack1l111ll_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠩᵎ"): driver.session_id,
        bstack1l111ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧᵏ"): driver.capabilities.get(bstack1l111ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬᵐ"), None),
        bstack1l111ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪᵑ"): driver.capabilities.get(bstack1l111ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᵒ"), None),
        bstack1l111ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࠬᵓ"): driver.capabilities.get(bstack1l111ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠪᵔ"), None),
        bstack1l111ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᵕ"):driver.capabilities.get(bstack1l111ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᵖ"), None),
    }
    if bstack111l1ll1lll_opy_() == bstack1l111ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᵗ"):
        if bstack1llll1l11l_opy_():
            info[bstack1l111ll_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࠩᵘ")] = bstack1l111ll_opy_ (u"ࠩࡤࡴࡵ࠳ࡡࡶࡶࡲࡱࡦࡺࡥࠨᵙ")
        elif driver.capabilities.get(bstack1l111ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᵚ"), {}).get(bstack1l111ll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨᵛ"), False):
            info[bstack1l111ll_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭ᵜ")] = bstack1l111ll_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪᵝ")
        else:
            info[bstack1l111ll_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࠨᵞ")] = bstack1l111ll_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪᵟ")
    return info
def bstack1llll1l11l_opy_():
    if bstack111l11ll_opy_.get_property(bstack1l111ll_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨᵠ")):
        return True
    if bstack1lll1l1ll1_opy_(os.environ.get(bstack1l111ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫᵡ"), None)):
        return True
    return False
def bstack11l1lllll1_opy_(bstack1111l1l11ll_opy_, url, data, config):
    headers = config.get(bstack1l111ll_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬᵢ"), None)
    proxies = bstack1llll11111_opy_(config, url)
    auth = config.get(bstack1l111ll_opy_ (u"ࠬࡧࡵࡵࡪࠪᵣ"), None)
    response = requests.request(
            bstack1111l1l11ll_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack11l1ll1lll_opy_(bstack1l11l1lll1_opy_, size):
    bstack1111l1ll11_opy_ = []
    while len(bstack1l11l1lll1_opy_) > size:
        bstack1llll111ll_opy_ = bstack1l11l1lll1_opy_[:size]
        bstack1111l1ll11_opy_.append(bstack1llll111ll_opy_)
        bstack1l11l1lll1_opy_ = bstack1l11l1lll1_opy_[size:]
    bstack1111l1ll11_opy_.append(bstack1l11l1lll1_opy_)
    return bstack1111l1ll11_opy_
def bstack111l1l11lll_opy_(message, bstack1111ll1l1l1_opy_=False):
    os.write(1, bytes(message, bstack1l111ll_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᵤ")))
    os.write(1, bytes(bstack1l111ll_opy_ (u"ࠧ࡝ࡰࠪᵥ"), bstack1l111ll_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧᵦ")))
    if bstack1111ll1l1l1_opy_:
        with open(bstack1l111ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠯ࡲ࠵࠶ࡿ࠭ࠨᵧ") + os.environ[bstack1l111ll_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩᵨ")] + bstack1l111ll_opy_ (u"ࠫ࠳ࡲ࡯ࡨࠩᵩ"), bstack1l111ll_opy_ (u"ࠬࡧࠧᵪ")) as f:
            f.write(message + bstack1l111ll_opy_ (u"࠭࡜࡯ࠩᵫ"))
def bstack1lll1ll1lll_opy_():
    return os.environ[bstack1l111ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪᵬ")].lower() == bstack1l111ll_opy_ (u"ࠨࡶࡵࡹࡪ࠭ᵭ")
def bstack1ll11lll_opy_():
    return bstack1llll1l1_opy_().replace(tzinfo=None).isoformat() + bstack1l111ll_opy_ (u"ࠩ࡝ࠫᵮ")
def bstack111l1111111_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack1l111ll_opy_ (u"ࠪ࡞ࠬᵯ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack1l111ll_opy_ (u"ࠫ࡟࠭ᵰ")))).total_seconds() * 1000
def bstack1111llllll1_opy_(timestamp):
    return bstack111l1l111l1_opy_(timestamp).isoformat() + bstack1l111ll_opy_ (u"ࠬࡠࠧᵱ")
def bstack1111ll11ll1_opy_(bstack111l111ll1l_opy_):
    date_format = bstack1l111ll_opy_ (u"࡚࠭ࠥࠧࡰࠩࡩࠦࠥࡉ࠼ࠨࡑ࠿ࠫࡓ࠯ࠧࡩࠫᵲ")
    bstack111l1l111ll_opy_ = datetime.datetime.strptime(bstack111l111ll1l_opy_, date_format)
    return bstack111l1l111ll_opy_.isoformat() + bstack1l111ll_opy_ (u"࡛ࠧࠩᵳ")
def bstack111l11lll11_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack1l111ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᵴ")
    else:
        return bstack1l111ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᵵ")
def bstack1lll1l1ll1_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack1l111ll_opy_ (u"ࠪࡸࡷࡻࡥࠨᵶ")
def bstack111l11lllll_opy_(val):
    return val.__str__().lower() == bstack1l111ll_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪᵷ")
def error_handler(bstack111l11l1l1l_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack111l11l1l1l_opy_ as e:
                print(bstack1l111ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࡻࡾࠢ࠰ࡂࠥࢁࡽ࠻ࠢࡾࢁࠧᵸ").format(func.__name__, bstack111l11l1l1l_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack1111lllllll_opy_(bstack111l111ll11_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack111l111ll11_opy_(cls, *args, **kwargs)
            except bstack111l11l1l1l_opy_ as e:
                print(bstack1l111ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡼࡿࠣ࠱ࡃࠦࡻࡾ࠼ࠣࡿࢂࠨᵹ").format(bstack111l111ll11_opy_.__name__, bstack111l11l1l1l_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack1111lllllll_opy_
    else:
        return decorator
def bstack1111lllll_opy_(bstack1lll1l111_opy_):
    if os.getenv(bstack1l111ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪᵺ")) is not None:
        return bstack1lll1l1ll1_opy_(os.getenv(bstack1l111ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫᵻ")))
    if bstack1l111ll_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᵼ") in bstack1lll1l111_opy_ and bstack111l11lllll_opy_(bstack1lll1l111_opy_[bstack1l111ll_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᵽ")]):
        return False
    if bstack1l111ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᵾ") in bstack1lll1l111_opy_ and bstack111l11lllll_opy_(bstack1lll1l111_opy_[bstack1l111ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᵿ")]):
        return False
    return True
def bstack1ll1l1ll1_opy_():
    try:
        from pytest_bdd import reporting
        bstack111l111l1l1_opy_ = os.environ.get(bstack1l111ll_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡛ࡓࡆࡔࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࠨᶀ"), None)
        return bstack111l111l1l1_opy_ is None or bstack111l111l1l1_opy_ == bstack1l111ll_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠦᶁ")
    except Exception as e:
        return False
def bstack1l1111ll1l_opy_(hub_url, CONFIG):
    if bstack11llll1l1l_opy_() <= version.parse(bstack1l111ll_opy_ (u"ࠨ࠵࠱࠵࠸࠴࠰ࠨᶂ")):
        if hub_url:
            return bstack1l111ll_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥᶃ") + hub_url + bstack1l111ll_opy_ (u"ࠥ࠾࠽࠶࠯ࡸࡦ࠲࡬ࡺࡨࠢᶄ")
        return bstack1l11l1l1l_opy_
    if hub_url:
        return bstack1l111ll_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨᶅ") + hub_url + bstack1l111ll_opy_ (u"ࠧ࠵ࡷࡥ࠱࡫ࡹࡧࠨᶆ")
    return bstack1lll11l11l_opy_
def bstack1111lll1ll1_opy_():
    return isinstance(os.getenv(bstack1l111ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖ࡙ࡕࡇࡖࡘࡤࡖࡌࡖࡉࡌࡒࠬᶇ")), str)
def bstack1l11ll1ll1_opy_(url):
    return urlparse(url).hostname
def bstack1l11l1lll_opy_(hostname):
    for bstack1ll1ll111_opy_ in bstack1l1l11ll11_opy_:
        regex = re.compile(bstack1ll1ll111_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11ll1111ll1_opy_(bstack1111l11ll11_opy_, file_name, logger):
    bstack1l111ll1l1_opy_ = os.path.join(os.path.expanduser(bstack1l111ll_opy_ (u"ࠧࡿࠩᶈ")), bstack1111l11ll11_opy_)
    try:
        if not os.path.exists(bstack1l111ll1l1_opy_):
            os.makedirs(bstack1l111ll1l1_opy_)
        file_path = os.path.join(os.path.expanduser(bstack1l111ll_opy_ (u"ࠨࢀࠪᶉ")), bstack1111l11ll11_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack1l111ll_opy_ (u"ࠩࡺࠫᶊ")):
                pass
            with open(file_path, bstack1l111ll_opy_ (u"ࠥࡻ࠰ࠨᶋ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack11lll1l111_opy_.format(str(e)))
def bstack11ll111111l_opy_(file_name, key, value, logger):
    file_path = bstack11ll1111ll1_opy_(bstack1l111ll_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᶌ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1ll1l11l1_opy_ = json.load(open(file_path, bstack1l111ll_opy_ (u"ࠬࡸࡢࠨᶍ")))
        else:
            bstack1ll1l11l1_opy_ = {}
        bstack1ll1l11l1_opy_[key] = value
        with open(file_path, bstack1l111ll_opy_ (u"ࠨࡷࠬࠤᶎ")) as outfile:
            json.dump(bstack1ll1l11l1_opy_, outfile)
def bstack1l111llll_opy_(file_name, logger):
    file_path = bstack11ll1111ll1_opy_(bstack1l111ll_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᶏ"), file_name, logger)
    bstack1ll1l11l1_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack1l111ll_opy_ (u"ࠨࡴࠪᶐ")) as bstack111l1l1l1l_opy_:
            bstack1ll1l11l1_opy_ = json.load(bstack111l1l1l1l_opy_)
    return bstack1ll1l11l1_opy_
def bstack111ll1l1l_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack1l111ll_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡩ࡫࡬ࡦࡶ࡬ࡲ࡬ࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ᶑ") + file_path + bstack1l111ll_opy_ (u"ࠪࠤࠬᶒ") + str(e))
def bstack11llll1l1l_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack1l111ll_opy_ (u"ࠦࡁࡔࡏࡕࡕࡈࡘࡃࠨᶓ")
def bstack111l11llll_opy_(config):
    if bstack1l111ll_opy_ (u"ࠬ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫᶔ") in config:
        del (config[bstack1l111ll_opy_ (u"࠭ࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬᶕ")])
        return False
    if bstack11llll1l1l_opy_() < version.parse(bstack1l111ll_opy_ (u"ࠧ࠴࠰࠷࠲࠵࠭ᶖ")):
        return False
    if bstack11llll1l1l_opy_() >= version.parse(bstack1l111ll_opy_ (u"ࠨ࠶࠱࠵࠳࠻ࠧᶗ")):
        return True
    if bstack1l111ll_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩᶘ") in config and config[bstack1l111ll_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪᶙ")] is False:
        return False
    else:
        return True
def bstack11l11111ll_opy_(args_list, bstack111l1l1111l_opy_):
    index = -1
    for value in bstack111l1l1111l_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
def bstack1111ll11lll_opy_(a, b):
  for k, v in b.items():
    if isinstance(v, dict) and k in a and isinstance(a[k], dict):
        bstack1111ll11lll_opy_(a[k], v)
    else:
        a[k] = v
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1ll11l11_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1ll11l11_opy_ = bstack1ll11l11_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack1l111ll_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᶚ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack1l111ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᶛ"), exception=exception)
    def bstack1111111l1l_opy_(self):
        if self.result != bstack1l111ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᶜ"):
            return None
        if isinstance(self.exception_type, str) and bstack1l111ll_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥᶝ") in self.exception_type:
            return bstack1l111ll_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠤᶞ")
        return bstack1l111ll_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥᶟ")
    def bstack111l11ll1ll_opy_(self):
        if self.result != bstack1l111ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᶠ"):
            return None
        if self.bstack1ll11l11_opy_:
            return self.bstack1ll11l11_opy_
        return bstack111l111lll1_opy_(self.exception)
def bstack111l111lll1_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack1111l11l1l1_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1l1111ll_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack11l1ll11ll_opy_(config, logger):
    try:
        import playwright
        bstack111l1l11ll1_opy_ = playwright.__file__
        bstack1111l1llll1_opy_ = os.path.split(bstack111l1l11ll1_opy_)
        bstack1111ll1l1ll_opy_ = bstack1111l1llll1_opy_[0] + bstack1l111ll_opy_ (u"ࠫ࠴ࡪࡲࡪࡸࡨࡶ࠴ࡶࡡࡤ࡭ࡤ࡫ࡪ࠵࡬ࡪࡤ࠲ࡧࡱ࡯࠯ࡤ࡮࡬࠲࡯ࡹࠧᶡ")
        os.environ[bstack1l111ll_opy_ (u"ࠬࡍࡌࡐࡄࡄࡐࡤࡇࡇࡆࡐࡗࡣࡍ࡚ࡔࡑࡡࡓࡖࡔ࡞࡙ࠨᶢ")] = bstack11lll1l1l_opy_(config)
        with open(bstack1111ll1l1ll_opy_, bstack1l111ll_opy_ (u"࠭ࡲࠨᶣ")) as f:
            file_content = f.read()
            bstack1111lll111l_opy_ = bstack1l111ll_opy_ (u"ࠧࡨ࡮ࡲࡦࡦࡲ࠭ࡢࡩࡨࡲࡹ࠭ᶤ")
            bstack111l1ll11l1_opy_ = file_content.find(bstack1111lll111l_opy_)
            if bstack111l1ll11l1_opy_ == -1:
              process = subprocess.Popen(bstack1l111ll_opy_ (u"ࠣࡰࡳࡱࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡧ࡭ࡱࡥࡥࡱ࠳ࡡࡨࡧࡱࡸࠧᶥ"), shell=True, cwd=bstack1111l1llll1_opy_[0])
              process.wait()
              bstack111l1111lll_opy_ = bstack1l111ll_opy_ (u"ࠩࠥࡹࡸ࡫ࠠࡴࡶࡵ࡭ࡨࡺࠢ࠼ࠩᶦ")
              bstack1111l111lll_opy_ = bstack1l111ll_opy_ (u"ࠥࠦࠧࠦ࡜ࠣࡷࡶࡩࠥࡹࡴࡳ࡫ࡦࡸࡡࠨ࠻ࠡࡥࡲࡲࡸࡺࠠࡼࠢࡥࡳࡴࡺࡳࡵࡴࡤࡴࠥࢃࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࠫ࡬ࡲ࡯ࡣࡣ࡯࠱ࡦ࡭ࡥ࡯ࡶࠪ࠭ࡀࠦࡩࡧࠢࠫࡴࡷࡵࡣࡦࡵࡶ࠲ࡪࡴࡶ࠯ࡉࡏࡓࡇࡇࡌࡠࡃࡊࡉࡓ࡚࡟ࡉࡖࡗࡔࡤࡖࡒࡐ࡚࡜࠭ࠥࡨ࡯ࡰࡶࡶࡸࡷࡧࡰࠩࠫ࠾ࠤࠧࠨࠢᶧ")
              bstack111l11l1l11_opy_ = file_content.replace(bstack111l1111lll_opy_, bstack1111l111lll_opy_)
              with open(bstack1111ll1l1ll_opy_, bstack1l111ll_opy_ (u"ࠫࡼ࠭ᶨ")) as f:
                f.write(bstack111l11l1l11_opy_)
    except Exception as e:
        logger.error(bstack11llll11l1_opy_.format(str(e)))
def bstack1l1l1l11l1_opy_():
  try:
    bstack1111l111l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1l111ll_opy_ (u"ࠬࡵࡰࡵ࡫ࡰࡥࡱࡥࡨࡶࡤࡢࡹࡷࡲ࠮࡫ࡵࡲࡲࠬᶩ"))
    bstack111l111111l_opy_ = []
    if os.path.exists(bstack1111l111l1l_opy_):
      with open(bstack1111l111l1l_opy_) as f:
        bstack111l111111l_opy_ = json.load(f)
      os.remove(bstack1111l111l1l_opy_)
    return bstack111l111111l_opy_
  except:
    pass
  return []
def bstack111llll1l1_opy_(bstack1ll1l1llll_opy_):
  try:
    bstack111l111111l_opy_ = []
    bstack1111l111l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1l111ll_opy_ (u"࠭࡯ࡱࡶ࡬ࡱࡦࡲ࡟ࡩࡷࡥࡣࡺࡸ࡬࠯࡬ࡶࡳࡳ࠭ᶪ"))
    if os.path.exists(bstack1111l111l1l_opy_):
      with open(bstack1111l111l1l_opy_) as f:
        bstack111l111111l_opy_ = json.load(f)
    bstack111l111111l_opy_.append(bstack1ll1l1llll_opy_)
    with open(bstack1111l111l1l_opy_, bstack1l111ll_opy_ (u"ࠧࡸࠩᶫ")) as f:
        json.dump(bstack111l111111l_opy_, f)
  except:
    pass
def bstack11lll1111_opy_(logger, bstack1111l1lll11_opy_ = False):
  try:
    test_name = os.environ.get(bstack1l111ll_opy_ (u"ࠨࡒ࡜ࡘࡊ࡙ࡔࡠࡖࡈࡗ࡙ࡥࡎࡂࡏࡈࠫᶬ"), bstack1l111ll_opy_ (u"ࠩࠪᶭ"))
    if test_name == bstack1l111ll_opy_ (u"ࠪࠫᶮ"):
        test_name = threading.current_thread().__dict__.get(bstack1l111ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡆࡩࡪ࡟ࡵࡧࡶࡸࡤࡴࡡ࡮ࡧࠪᶯ"), bstack1l111ll_opy_ (u"ࠬ࠭ᶰ"))
    bstack111l1ll111l_opy_ = bstack1l111ll_opy_ (u"࠭ࠬࠡࠩᶱ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack1111l1lll11_opy_:
        bstack111111l11_opy_ = os.environ.get(bstack1l111ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧᶲ"), bstack1l111ll_opy_ (u"ࠨ࠲ࠪᶳ"))
        bstack11lll11111_opy_ = {bstack1l111ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᶴ"): test_name, bstack1l111ll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᶵ"): bstack111l1ll111l_opy_, bstack1l111ll_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪᶶ"): bstack111111l11_opy_}
        bstack111l11ll1l1_opy_ = []
        bstack1111l1l1lll_opy_ = os.path.join(tempfile.gettempdir(), bstack1l111ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡶࡰࡱࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫᶷ"))
        if os.path.exists(bstack1111l1l1lll_opy_):
            with open(bstack1111l1l1lll_opy_) as f:
                bstack111l11ll1l1_opy_ = json.load(f)
        bstack111l11ll1l1_opy_.append(bstack11lll11111_opy_)
        with open(bstack1111l1l1lll_opy_, bstack1l111ll_opy_ (u"࠭ࡷࠨᶸ")) as f:
            json.dump(bstack111l11ll1l1_opy_, f)
    else:
        bstack11lll11111_opy_ = {bstack1l111ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᶹ"): test_name, bstack1l111ll_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᶺ"): bstack111l1ll111l_opy_, bstack1l111ll_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨᶻ"): str(multiprocessing.current_process().name)}
        if bstack1l111ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺࠧᶼ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack11lll11111_opy_)
  except Exception as e:
      logger.warn(bstack1l111ll_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡲࡶࡪࠦࡰࡺࡶࡨࡷࡹࠦࡦࡶࡰࡱࡩࡱࠦࡤࡢࡶࡤ࠾ࠥࢁࡽࠣᶽ").format(e))
def bstack1l1l1111ll_opy_(error_message, test_name, index, logger):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1l111ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧ࡯ࡳࡨࡱࠠ࡯ࡱࡷࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠬࠡࡷࡶ࡭ࡳ࡭ࠠࡣࡣࡶ࡭ࡨࠦࡦࡪ࡮ࡨࠤࡴࡶࡥࡳࡣࡷ࡭ࡴࡴࡳࠨᶾ"))
    try:
      bstack1111l1lll1l_opy_ = []
      bstack11lll11111_opy_ = {bstack1l111ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᶿ"): test_name, bstack1l111ll_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭᷀"): error_message, bstack1l111ll_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧ᷁"): index}
      bstack111l1111l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1l111ll_opy_ (u"ࠩࡵࡳࡧࡵࡴࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰ᷂ࠪ"))
      if os.path.exists(bstack111l1111l1l_opy_):
          with open(bstack111l1111l1l_opy_) as f:
              bstack1111l1lll1l_opy_ = json.load(f)
      bstack1111l1lll1l_opy_.append(bstack11lll11111_opy_)
      with open(bstack111l1111l1l_opy_, bstack1l111ll_opy_ (u"ࠪࡻࠬ᷃")) as f:
          json.dump(bstack1111l1lll1l_opy_, f)
    except Exception as e:
      logger.warn(bstack1l111ll_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡲࡶࡪࠦࡲࡰࡤࡲࡸࠥ࡬ࡵ࡯ࡰࡨࡰࠥࡪࡡࡵࡣ࠽ࠤࢀࢃࠢ᷄").format(e))
    return
  bstack1111l1lll1l_opy_ = []
  bstack11lll11111_opy_ = {bstack1l111ll_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ᷅"): test_name, bstack1l111ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ᷆"): error_message, bstack1l111ll_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭᷇"): index}
  bstack111l1111l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1l111ll_opy_ (u"ࠨࡴࡲࡦࡴࡺ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩ᷈"))
  lock_file = bstack111l1111l1l_opy_ + bstack1l111ll_opy_ (u"ࠩ࠱ࡰࡴࡩ࡫ࠨ᷉")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack111l1111l1l_opy_):
          with open(bstack111l1111l1l_opy_, bstack1l111ll_opy_ (u"ࠪࡶ᷊ࠬ")) as f:
              content = f.read().strip()
              if content:
                  bstack1111l1lll1l_opy_ = json.load(open(bstack111l1111l1l_opy_))
      bstack1111l1lll1l_opy_.append(bstack11lll11111_opy_)
      with open(bstack111l1111l1l_opy_, bstack1l111ll_opy_ (u"ࠫࡼ࠭᷋")) as f:
          json.dump(bstack1111l1lll1l_opy_, f)
  except Exception as e:
    logger.warn(bstack1l111ll_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡳࡷ࡫ࠠࡳࡱࡥࡳࡹࠦࡦࡶࡰࡱࡩࡱࠦࡤࡢࡶࡤࠤࡼ࡯ࡴࡩࠢࡩ࡭ࡱ࡫ࠠ࡭ࡱࡦ࡯࡮ࡴࡧ࠻ࠢࡾࢁࠧ᷌").format(e))
def bstack11l11l11ll_opy_(bstack1lll1111l1_opy_, name, logger):
  try:
    bstack11lll11111_opy_ = {bstack1l111ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ᷍"): name, bstack1l111ll_opy_ (u"ࠧࡦࡴࡵࡳࡷ᷎࠭"): bstack1lll1111l1_opy_, bstack1l111ll_opy_ (u"ࠨ࡫ࡱࡨࡪࡾ᷏ࠧ"): str(threading.current_thread()._name)}
    return bstack11lll11111_opy_
  except Exception as e:
    logger.warn(bstack1l111ll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡧ࡫ࡨࡢࡸࡨࠤ࡫ࡻ࡮࡯ࡧ࡯ࠤࡩࡧࡴࡢ࠼ࠣࡿࢂࠨ᷐").format(e))
  return
def bstack1111lll11l1_opy_():
    return platform.system() == bstack1l111ll_opy_ (u"࡛ࠪ࡮ࡴࡤࡰࡹࡶࠫ᷑")
def bstack1l1111l11_opy_(bstack1111ll1l11l_opy_, config, logger):
    bstack1111l11lll1_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack1111ll1l11l_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack1l111ll_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫࡯ࡸࡪࡸࠠࡤࡱࡱࡪ࡮࡭ࠠ࡬ࡧࡼࡷࠥࡨࡹࠡࡴࡨ࡫ࡪࡾࠠ࡮ࡣࡷࡧ࡭ࡀࠠࡼࡿࠥ᷒").format(e))
    return bstack1111l11lll1_opy_
def bstack11l1l1ll1ll_opy_(bstack1111ll1llll_opy_, bstack111l1l1l1l1_opy_):
    bstack111l111l111_opy_ = version.parse(bstack1111ll1llll_opy_)
    bstack1111l11llll_opy_ = version.parse(bstack111l1l1l1l1_opy_)
    if bstack111l111l111_opy_ > bstack1111l11llll_opy_:
        return 1
    elif bstack111l111l111_opy_ < bstack1111l11llll_opy_:
        return -1
    else:
        return 0
def bstack1llll1l1_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack111l1l111l1_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack1111lll1111_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack1l111111l_opy_(options, framework, config, bstack11lll1l11l_opy_={}):
    if options is None:
        return
    if getattr(options, bstack1l111ll_opy_ (u"ࠬ࡭ࡥࡵࠩᷓ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack111ll1l111_opy_ = caps.get(bstack1l111ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᷔ"))
    bstack111l11111l1_opy_ = True
    bstack111l111lll_opy_ = os.environ[bstack1l111ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬᷕ")]
    bstack1l111l1l1l1_opy_ = config.get(bstack1l111ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᷖ"), False)
    if bstack1l111l1l1l1_opy_:
        bstack1l1l1l11111_opy_ = config.get(bstack1l111ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩᷗ"), {})
        bstack1l1l1l11111_opy_[bstack1l111ll_opy_ (u"ࠪࡥࡺࡺࡨࡕࡱ࡮ࡩࡳ࠭ᷘ")] = os.getenv(bstack1l111ll_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩᷙ"))
        bstack111l1l1lll1_opy_ = json.loads(os.getenv(bstack1l111ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭ᷚ"), bstack1l111ll_opy_ (u"࠭ࡻࡾࠩᷛ"))).get(bstack1l111ll_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᷜ"))
    if bstack111l11lllll_opy_(caps.get(bstack1l111ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡶࡵࡨ࡛࠸ࡉࠧᷝ"))) or bstack111l11lllll_opy_(caps.get(bstack1l111ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡷࡶࡩࡤࡽ࠳ࡤࠩᷞ"))):
        bstack111l11111l1_opy_ = False
    if bstack111l11llll_opy_({bstack1l111ll_opy_ (u"ࠥࡹࡸ࡫ࡗ࠴ࡅࠥᷟ"): bstack111l11111l1_opy_}):
        bstack111ll1l111_opy_ = bstack111ll1l111_opy_ or {}
        bstack111ll1l111_opy_[bstack1l111ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ᷠ")] = bstack1111lll1111_opy_(framework)
        bstack111ll1l111_opy_[bstack1l111ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᷡ")] = bstack1lll1ll1lll_opy_()
        bstack111ll1l111_opy_[bstack1l111ll_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩᷢ")] = bstack111l111lll_opy_
        bstack111ll1l111_opy_[bstack1l111ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩᷣ")] = bstack11lll1l11l_opy_
        if bstack1l111l1l1l1_opy_:
            bstack111ll1l111_opy_[bstack1l111ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᷤ")] = bstack1l111l1l1l1_opy_
            bstack111ll1l111_opy_[bstack1l111ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩᷥ")] = bstack1l1l1l11111_opy_
            bstack111ll1l111_opy_[bstack1l111ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᷦ")][bstack1l111ll_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᷧ")] = bstack111l1l1lll1_opy_
        if getattr(options, bstack1l111ll_opy_ (u"ࠬࡹࡥࡵࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸࡾ࠭ᷨ"), None):
            options.set_capability(bstack1l111ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᷩ"), bstack111ll1l111_opy_)
        else:
            options[bstack1l111ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᷪ")] = bstack111ll1l111_opy_
    else:
        if getattr(options, bstack1l111ll_opy_ (u"ࠨࡵࡨࡸࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡺࠩᷫ"), None):
            options.set_capability(bstack1l111ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪᷬ"), bstack1111lll1111_opy_(framework))
            options.set_capability(bstack1l111ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᷭ"), bstack1lll1ll1lll_opy_())
            options.set_capability(bstack1l111ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ᷮ"), bstack111l111lll_opy_)
            options.set_capability(bstack1l111ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ᷯ"), bstack11lll1l11l_opy_)
            if bstack1l111l1l1l1_opy_:
                options.set_capability(bstack1l111ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᷰ"), bstack1l111l1l1l1_opy_)
                options.set_capability(bstack1l111ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ᷱ"), bstack1l1l1l11111_opy_)
                options.set_capability(bstack1l111ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹ࠮ࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᷲ"), bstack111l1l1lll1_opy_)
        else:
            options[bstack1l111ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪᷳ")] = bstack1111lll1111_opy_(framework)
            options[bstack1l111ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᷴ")] = bstack1lll1ll1lll_opy_()
            options[bstack1l111ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭᷵")] = bstack111l111lll_opy_
            options[bstack1l111ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭᷶")] = bstack11lll1l11l_opy_
            if bstack1l111l1l1l1_opy_:
                options[bstack1l111ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ᷷ࠬ")] = bstack1l111l1l1l1_opy_
                options[bstack1l111ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ᷸࠭")] = bstack1l1l1l11111_opy_
                options[bstack1l111ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹ᷹ࠧ")][bstack1l111ll_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰ᷺ࠪ")] = bstack111l1l1lll1_opy_
    return options
def bstack111l1l1llll_opy_(ws_endpoint, framework):
    bstack11lll1l11l_opy_ = bstack111l11ll_opy_.get_property(bstack1l111ll_opy_ (u"ࠥࡔࡑࡇ࡙ࡘࡔࡌࡋࡍ࡚࡟ࡑࡔࡒࡈ࡚ࡉࡔࡠࡏࡄࡔࠧ᷻"))
    if ws_endpoint and len(ws_endpoint.split(bstack1l111ll_opy_ (u"ࠫࡨࡧࡰࡴ࠿ࠪ᷼"))) > 1:
        ws_url = ws_endpoint.split(bstack1l111ll_opy_ (u"ࠬࡩࡡࡱࡵࡀ᷽ࠫ"))[0]
        if bstack1l111ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩ᷾") in ws_url:
            from browserstack_sdk._version import __version__
            bstack111l1l11111_opy_ = json.loads(urllib.parse.unquote(ws_endpoint.split(bstack1l111ll_opy_ (u"ࠧࡤࡣࡳࡷࡂ᷿࠭"))[1]))
            bstack111l1l11111_opy_ = bstack111l1l11111_opy_ or {}
            bstack111l111lll_opy_ = os.environ[bstack1l111ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭Ḁ")]
            bstack111l1l11111_opy_[bstack1l111ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪḁ")] = str(framework) + str(__version__)
            bstack111l1l11111_opy_[bstack1l111ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫḂ")] = bstack1lll1ll1lll_opy_()
            bstack111l1l11111_opy_[bstack1l111ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ḃ")] = bstack111l111lll_opy_
            bstack111l1l11111_opy_[bstack1l111ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭Ḅ")] = bstack11lll1l11l_opy_
            ws_endpoint = ws_endpoint.split(bstack1l111ll_opy_ (u"࠭ࡣࡢࡲࡶࡁࠬḅ"))[0] + bstack1l111ll_opy_ (u"ࠧࡤࡣࡳࡷࡂ࠭Ḇ") + urllib.parse.quote(json.dumps(bstack111l1l11111_opy_))
    return ws_endpoint
def bstack1ll11ll1ll_opy_():
    global bstack111ll111l_opy_
    from playwright._impl._browser_type import BrowserType
    bstack111ll111l_opy_ = BrowserType.connect
    return bstack111ll111l_opy_
def bstack111l11lll_opy_(framework_name):
    global bstack11lllllll_opy_
    bstack11lllllll_opy_ = framework_name
    return framework_name
def bstack1l1l11ll1_opy_(self, *args, **kwargs):
    global bstack111ll111l_opy_
    try:
        global bstack11lllllll_opy_
        if bstack1l111ll_opy_ (u"ࠨࡹࡶࡉࡳࡪࡰࡰ࡫ࡱࡸࠬḇ") in kwargs:
            kwargs[bstack1l111ll_opy_ (u"ࠩࡺࡷࡊࡴࡤࡱࡱ࡬ࡲࡹ࠭Ḉ")] = bstack111l1l1llll_opy_(
                kwargs.get(bstack1l111ll_opy_ (u"ࠪࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺࠧḉ"), None),
                bstack11lllllll_opy_
            )
    except Exception as e:
        logger.error(bstack1l111ll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡫࡮ࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫࡙ࠥࡄࡌࠢࡦࡥࡵࡹ࠺ࠡࡽࢀࠦḊ").format(str(e)))
    return bstack111ll111l_opy_(self, *args, **kwargs)
def bstack1111l1l1l1l_opy_(bstack1111l11l11l_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack1llll11111_opy_(bstack1111l11l11l_opy_, bstack1l111ll_opy_ (u"ࠧࠨḋ"))
        if proxies and proxies.get(bstack1l111ll_opy_ (u"ࠨࡨࡵࡶࡳࡷࠧḌ")):
            parsed_url = urlparse(proxies.get(bstack1l111ll_opy_ (u"ࠢࡩࡶࡷࡴࡸࠨḍ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack1l111ll_opy_ (u"ࠨࡲࡵࡳࡽࡿࡈࡰࡵࡷࠫḎ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack1l111ll_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡱࡵࡸࠬḏ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack1l111ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࡗࡶࡩࡷ࠭Ḑ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack1l111ll_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡥࡸࡹࠧḑ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack11l1l111ll_opy_(bstack1111l11l11l_opy_):
    bstack1111ll111ll_opy_ = {
        bstack11l1l111l1l_opy_[bstack1111llll111_opy_]: bstack1111l11l11l_opy_[bstack1111llll111_opy_]
        for bstack1111llll111_opy_ in bstack1111l11l11l_opy_
        if bstack1111llll111_opy_ in bstack11l1l111l1l_opy_
    }
    bstack1111ll111ll_opy_[bstack1l111ll_opy_ (u"ࠧࡶࡲࡰࡺࡼࡗࡪࡺࡴࡪࡰࡪࡷࠧḒ")] = bstack1111l1l1l1l_opy_(bstack1111l11l11l_opy_, bstack111l11ll_opy_.get_property(bstack1l111ll_opy_ (u"ࠨࡰࡳࡱࡻࡽࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸࠨḓ")))
    bstack1111l1ll11l_opy_ = [element.lower() for element in bstack11l11lll1ll_opy_]
    bstack111l1lll111_opy_(bstack1111ll111ll_opy_, bstack1111l1ll11l_opy_)
    return bstack1111ll111ll_opy_
def bstack111l1lll111_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack1l111ll_opy_ (u"ࠢࠫࠬ࠭࠮ࠧḔ")
    for value in d.values():
        if isinstance(value, dict):
            bstack111l1lll111_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack111l1lll111_opy_(item, keys)
def bstack1ll11ll1l11_opy_():
    bstack111l1ll1111_opy_ = [os.environ.get(bstack1l111ll_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡋࡏࡉࡘࡥࡄࡊࡔࠥḕ")), os.path.join(os.path.expanduser(bstack1l111ll_opy_ (u"ࠤࢁࠦḖ")), bstack1l111ll_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪḗ")), os.path.join(bstack1l111ll_opy_ (u"ࠫ࠴ࡺ࡭ࡱࠩḘ"), bstack1l111ll_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬḙ"))]
    for path in bstack111l1ll1111_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack1l111ll_opy_ (u"ࠨࡆࡪ࡮ࡨࠤࠬࠨḚ") + str(path) + bstack1l111ll_opy_ (u"ࠢࠨࠢࡨࡼ࡮ࡹࡴࡴ࠰ࠥḛ"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack1l111ll_opy_ (u"ࠣࡉ࡬ࡺ࡮ࡴࡧࠡࡲࡨࡶࡲ࡯ࡳࡴ࡫ࡲࡲࡸࠦࡦࡰࡴࠣࠫࠧḜ") + str(path) + bstack1l111ll_opy_ (u"ࠤࠪࠦḝ"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack1l111ll_opy_ (u"ࠥࡊ࡮ࡲࡥࠡࠩࠥḞ") + str(path) + bstack1l111ll_opy_ (u"ࠦࠬࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡩࡣࡶࠤࡹ࡮ࡥࠡࡴࡨࡵࡺ࡯ࡲࡦࡦࠣࡴࡪࡸ࡭ࡪࡵࡶ࡭ࡴࡴࡳ࠯ࠤḟ"))
            else:
                logger.debug(bstack1l111ll_opy_ (u"ࠧࡉࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡧ࡫࡯ࡩࠥ࠭ࠢḠ") + str(path) + bstack1l111ll_opy_ (u"ࠨࠧࠡࡹ࡬ࡸ࡭ࠦࡷࡳ࡫ࡷࡩࠥࡶࡥࡳ࡯࡬ࡷࡸ࡯࡯࡯࠰ࠥḡ"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack1l111ll_opy_ (u"ࠢࡐࡲࡨࡶࡦࡺࡩࡰࡰࠣࡷࡺࡩࡣࡦࡧࡧࡩࡩࠦࡦࡰࡴࠣࠫࠧḢ") + str(path) + bstack1l111ll_opy_ (u"ࠣࠩ࠱ࠦḣ"))
            return path
        except Exception as e:
            logger.debug(bstack1l111ll_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࠢࡸࡴࠥ࡬ࡩ࡭ࡧࠣࠫࢀࡶࡡࡵࡪࢀࠫ࠿ࠦࠢḤ") + str(e) + bstack1l111ll_opy_ (u"ࠥࠦḥ"))
    logger.debug(bstack1l111ll_opy_ (u"ࠦࡆࡲ࡬ࠡࡲࡤࡸ࡭ࡹࠠࡧࡣ࡬ࡰࡪࡪ࠮ࠣḦ"))
    return None
@measure(event_name=EVENTS.bstack11l1l111ll1_opy_, stage=STAGE.bstack1ll11l111l_opy_)
def bstack1l1l1111ll1_opy_(binary_path, bstack1l11ll11l1l_opy_, bs_config):
    logger.debug(bstack1l111ll_opy_ (u"ࠧࡉࡵࡳࡴࡨࡲࡹࠦࡃࡍࡋࠣࡔࡦࡺࡨࠡࡨࡲࡹࡳࡪ࠺ࠡࡽࢀࠦḧ").format(binary_path))
    bstack1111lllll1l_opy_ = bstack1l111ll_opy_ (u"࠭ࠧḨ")
    bstack1111llll11l_opy_ = {
        bstack1l111ll_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬḩ"): __version__,
        bstack1l111ll_opy_ (u"ࠣࡱࡶࠦḪ"): platform.system(),
        bstack1l111ll_opy_ (u"ࠤࡲࡷࡤࡧࡲࡤࡪࠥḫ"): platform.machine(),
        bstack1l111ll_opy_ (u"ࠥࡧࡱ࡯࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣḬ"): bstack1l111ll_opy_ (u"ࠫ࠵࠭ḭ"),
        bstack1l111ll_opy_ (u"ࠧࡹࡤ࡬ࡡ࡯ࡥࡳ࡭ࡵࡢࡩࡨࠦḮ"): bstack1l111ll_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ḯ")
    }
    bstack111l11l11l1_opy_(bstack1111llll11l_opy_)
    try:
        if binary_path:
            bstack1111llll11l_opy_[bstack1l111ll_opy_ (u"ࠧࡤ࡮࡬ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬḰ")] = subprocess.check_output([binary_path, bstack1l111ll_opy_ (u"ࠣࡸࡨࡶࡸ࡯࡯࡯ࠤḱ")]).strip().decode(bstack1l111ll_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨḲ"))
        response = requests.request(
            bstack1l111ll_opy_ (u"ࠪࡋࡊ࡚ࠧḳ"),
            url=bstack11llllll11_opy_(bstack11l11lllll1_opy_),
            headers=None,
            auth=(bs_config[bstack1l111ll_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭Ḵ")], bs_config[bstack1l111ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨḵ")]),
            json=None,
            params=bstack1111llll11l_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack1l111ll_opy_ (u"࠭ࡵࡳ࡮ࠪḶ") in data.keys() and bstack1l111ll_opy_ (u"ࠧࡶࡲࡧࡥࡹ࡫ࡤࡠࡥ࡯࡭ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ḷ") in data.keys():
            logger.debug(bstack1l111ll_opy_ (u"ࠣࡐࡨࡩࡩࠦࡴࡰࠢࡸࡴࡩࡧࡴࡦࠢࡥ࡭ࡳࡧࡲࡺ࠮ࠣࡧࡺࡸࡲࡦࡰࡷࠤࡧ࡯࡮ࡢࡴࡼࠤࡻ࡫ࡲࡴ࡫ࡲࡲ࠿ࠦࡻࡾࠤḸ").format(bstack1111llll11l_opy_[bstack1l111ll_opy_ (u"ࠩࡦࡰ࡮ࡥࡶࡦࡴࡶ࡭ࡴࡴࠧḹ")]))
            if bstack1l111ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡘࡖࡑ࠭Ḻ") in os.environ:
                logger.debug(bstack1l111ll_opy_ (u"ࠦࡘࡱࡩࡱࡲ࡬ࡲ࡬ࠦࡢࡪࡰࡤࡶࡾࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡣࡶࠤࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆࡎࡔࡁࡓ࡛ࡢ࡙ࡗࡒࠠࡪࡵࠣࡷࡪࡺࠢḻ"))
                data[bstack1l111ll_opy_ (u"ࠬࡻࡲ࡭ࠩḼ")] = os.environ[bstack1l111ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡉࡏࡃࡕ࡝ࡤ࡛ࡒࡍࠩḽ")]
            bstack1111ll1l111_opy_ = bstack111l11l1lll_opy_(data[bstack1l111ll_opy_ (u"ࠧࡶࡴ࡯ࠫḾ")], bstack1l11ll11l1l_opy_)
            bstack1111lllll1l_opy_ = os.path.join(bstack1l11ll11l1l_opy_, bstack1111ll1l111_opy_)
            os.chmod(bstack1111lllll1l_opy_, 0o777) # bstack111l11l11ll_opy_ permission
            return bstack1111lllll1l_opy_
    except Exception as e:
        logger.debug(bstack1l111ll_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡤࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡳ࡫ࡷࠡࡕࡇࡏࠥࢁࡽࠣḿ").format(e))
    return binary_path
def bstack111l11l11l1_opy_(bstack1111llll11l_opy_):
    try:
        if bstack1l111ll_opy_ (u"ࠩ࡯࡭ࡳࡻࡸࠨṀ") not in bstack1111llll11l_opy_[bstack1l111ll_opy_ (u"ࠪࡳࡸ࠭ṁ")].lower():
            return
        if os.path.exists(bstack1l111ll_opy_ (u"ࠦ࠴࡫ࡴࡤ࠱ࡲࡷ࠲ࡸࡥ࡭ࡧࡤࡷࡪࠨṂ")):
            with open(bstack1l111ll_opy_ (u"ࠧ࠵ࡥࡵࡥ࠲ࡳࡸ࠳ࡲࡦ࡮ࡨࡥࡸ࡫ࠢṃ"), bstack1l111ll_opy_ (u"ࠨࡲࠣṄ")) as f:
                bstack1111l1lllll_opy_ = {}
                for line in f:
                    if bstack1l111ll_opy_ (u"ࠢ࠾ࠤṅ") in line:
                        key, value = line.rstrip().split(bstack1l111ll_opy_ (u"ࠣ࠿ࠥṆ"), 1)
                        bstack1111l1lllll_opy_[key] = value.strip(bstack1l111ll_opy_ (u"ࠩࠥࡠࠬ࠭ṇ"))
                bstack1111llll11l_opy_[bstack1l111ll_opy_ (u"ࠪࡨ࡮ࡹࡴࡳࡱࠪṈ")] = bstack1111l1lllll_opy_.get(bstack1l111ll_opy_ (u"ࠦࡎࡊࠢṉ"), bstack1l111ll_opy_ (u"ࠧࠨṊ"))
        elif os.path.exists(bstack1l111ll_opy_ (u"ࠨ࠯ࡦࡶࡦ࠳ࡦࡲࡰࡪࡰࡨ࠱ࡷ࡫࡬ࡦࡣࡶࡩࠧṋ")):
            bstack1111llll11l_opy_[bstack1l111ll_opy_ (u"ࠧࡥ࡫ࡶࡸࡷࡵࠧṌ")] = bstack1l111ll_opy_ (u"ࠨࡣ࡯ࡴ࡮ࡴࡥࠨṍ")
    except Exception as e:
        logger.debug(bstack1l111ll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡭ࡥࡵࠢࡧ࡭ࡸࡺࡲࡰࠢࡲࡪࠥࡲࡩ࡯ࡷࡻࠦṎ") + e)
@measure(event_name=EVENTS.bstack11l11l1l111_opy_, stage=STAGE.bstack1ll11l111l_opy_)
def bstack111l11l1lll_opy_(bstack111l11ll111_opy_, bstack111l111l1ll_opy_):
    logger.debug(bstack1l111ll_opy_ (u"ࠥࡈࡴࡽ࡮࡭ࡱࡤࡨ࡮ࡴࡧࠡࡕࡇࡏࠥࡨࡩ࡯ࡣࡵࡽࠥ࡬ࡲࡰ࡯࠽ࠤࠧṏ") + str(bstack111l11ll111_opy_) + bstack1l111ll_opy_ (u"ࠦࠧṐ"))
    zip_path = os.path.join(bstack111l111l1ll_opy_, bstack1l111ll_opy_ (u"ࠧࡪ࡯ࡸࡰ࡯ࡳࡦࡪࡥࡥࡡࡩ࡭ࡱ࡫࠮ࡻ࡫ࡳࠦṑ"))
    bstack1111ll1l111_opy_ = bstack1l111ll_opy_ (u"࠭ࠧṒ")
    with requests.get(bstack111l11ll111_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack1l111ll_opy_ (u"ࠢࡸࡤࠥṓ")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack1l111ll_opy_ (u"ࠣࡈ࡬ࡰࡪࠦࡤࡰࡹࡱࡰࡴࡧࡤࡦࡦࠣࡷࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺ࠰ࠥṔ"))
    with zipfile.ZipFile(zip_path, bstack1l111ll_opy_ (u"ࠩࡵࠫṕ")) as zip_ref:
        bstack1111ll111l1_opy_ = zip_ref.namelist()
        if len(bstack1111ll111l1_opy_) > 0:
            bstack1111ll1l111_opy_ = bstack1111ll111l1_opy_[0] # bstack111l11l1ll1_opy_ bstack11l11lll1l1_opy_ will be bstack1111ll11111_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack111l111l1ll_opy_)
        logger.debug(bstack1l111ll_opy_ (u"ࠥࡊ࡮ࡲࡥࡴࠢࡶࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹࠡࡧࡻࡸࡷࡧࡣࡵࡧࡧࠤࡹࡵࠠࠨࠤṖ") + str(bstack111l111l1ll_opy_) + bstack1l111ll_opy_ (u"ࠦࠬࠨṗ"))
    os.remove(zip_path)
    return bstack1111ll1l111_opy_
def get_cli_dir():
    bstack111l11lll1l_opy_ = bstack1ll11ll1l11_opy_()
    if bstack111l11lll1l_opy_:
        bstack1l11ll11l1l_opy_ = os.path.join(bstack111l11lll1l_opy_, bstack1l111ll_opy_ (u"ࠧࡩ࡬ࡪࠤṘ"))
        if not os.path.exists(bstack1l11ll11l1l_opy_):
            os.makedirs(bstack1l11ll11l1l_opy_, mode=0o777, exist_ok=True)
        return bstack1l11ll11l1l_opy_
    else:
        raise FileNotFoundError(bstack1l111ll_opy_ (u"ࠨࡎࡰࠢࡺࡶ࡮ࡺࡡࡣ࡮ࡨࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧࠣࡪࡴࡸࠠࡵࡪࡨࠤࡘࡊࡋࠡࡤ࡬ࡲࡦࡸࡹ࠯ࠤṙ"))
def bstack1l1l1lll111_opy_(bstack1l11ll11l1l_opy_):
    bstack1l111ll_opy_ (u"ࠢࠣࠤࡊࡩࡹࠦࡴࡩࡧࠣࡴࡦࡺࡨࠡࡨࡲࡶࠥࡺࡨࡦࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡕࡇࡏࠥࡨࡩ࡯ࡣࡵࡽࠥ࡯࡮ࠡࡣࠣࡻࡷ࡯ࡴࡢࡤ࡯ࡩࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹ࠯ࠤࠥࠦṚ")
    bstack111l1l1l11l_opy_ = [
        os.path.join(bstack1l11ll11l1l_opy_, f)
        for f in os.listdir(bstack1l11ll11l1l_opy_)
        if os.path.isfile(os.path.join(bstack1l11ll11l1l_opy_, f)) and f.startswith(bstack1l111ll_opy_ (u"ࠣࡤ࡬ࡲࡦࡸࡹ࠮ࠤṛ"))
    ]
    if len(bstack111l1l1l11l_opy_) > 0:
        return max(bstack111l1l1l11l_opy_, key=os.path.getmtime) # get bstack1111l1ll111_opy_ binary
    return bstack1l111ll_opy_ (u"ࠤࠥṜ")
def bstack111l11llll1_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l1111l1lll_opy_(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = bstack1l1111l1lll_opy_(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack1l11ll1111_opy_(data, keys, default=None):
    bstack1l111ll_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡗࡦ࡬ࡥ࡭ࡻࠣ࡫ࡪࡺࠠࡢࠢࡱࡩࡸࡺࡥࡥࠢࡹࡥࡱࡻࡥࠡࡨࡵࡳࡲࠦࡡࠡࡦ࡬ࡧࡹ࡯࡯࡯ࡣࡵࡽࠥࡵࡲࠡ࡮࡬ࡷࡹ࠴ࠊࠡࠢࠣࠤ࠿ࡶࡡࡳࡣࡰࠤࡩࡧࡴࡢ࠼ࠣࡘ࡭࡫ࠠࡥ࡫ࡦࡸ࡮ࡵ࡮ࡢࡴࡼࠤࡴࡸࠠ࡭࡫ࡶࡸࠥࡺ࡯ࠡࡶࡵࡥࡻ࡫ࡲࡴࡧ࠱ࠎࠥࠦࠠࠡ࠼ࡳࡥࡷࡧ࡭ࠡ࡭ࡨࡽࡸࡀࠠࡂࠢ࡯࡭ࡸࡺࠠࡰࡨࠣ࡯ࡪࡿࡳ࠰࡫ࡱࡨ࡮ࡩࡥࡴࠢࡵࡩࡵࡸࡥࡴࡧࡱࡸ࡮ࡴࡧࠡࡶ࡫ࡩࠥࡶࡡࡵࡪ࠱ࠎࠥࠦࠠࠡ࠼ࡳࡥࡷࡧ࡭ࠡࡦࡨࡪࡦࡻ࡬ࡵ࠼࡚ࠣࡦࡲࡵࡦࠢࡷࡳࠥࡸࡥࡵࡷࡵࡲࠥ࡯ࡦࠡࡶ࡫ࡩࠥࡶࡡࡵࡪࠣࡨࡴ࡫ࡳࠡࡰࡲࡸࠥ࡫ࡸࡪࡵࡷ࠲ࠏࠦࠠࠡࠢ࠽ࡶࡪࡺࡵࡳࡰ࠽ࠤ࡙࡮ࡥࠡࡸࡤࡰࡺ࡫ࠠࡢࡶࠣࡸ࡭࡫ࠠ࡯ࡧࡶࡸࡪࡪࠠࡱࡣࡷ࡬࠱ࠦ࡯ࡳࠢࡧࡩ࡫ࡧࡵ࡭ࡶࠣ࡭࡫ࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥ࠰ࠍࠤࠥࠦࠠࠣࠤࠥṝ")
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