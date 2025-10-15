# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
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
from bstack_utils.constants import (bstack1ll1ll11l1_opy_, bstack1llll1l1ll_opy_, bstack111l1llll1_opy_,
                                    bstack11l11llllll_opy_, bstack11l1l1l11ll_opy_, bstack11l1l111111_opy_, bstack11l1l1111l1_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack11ll11llll_opy_, bstack11ll11l1l1_opy_
from bstack_utils.proxy import bstack111l1l1ll_opy_, bstack1l111l11l_opy_
from bstack_utils.constants import *
from bstack_utils import bstack1ll1ll111_opy_
from bstack_utils.bstack11l11lll11_opy_ import bstack1ll1ll11ll_opy_
from browserstack_sdk._version import __version__
bstack111111ll_opy_ = Config.bstack111l1ll1_opy_()
logger = bstack1ll1ll111_opy_.get_logger(__name__, bstack1ll1ll111_opy_.bstack1l1l1llll11_opy_())
def bstack111l11l11l1_opy_(config):
    return config[bstack1ll1l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ᯅ")]
def bstack111l11ll11l_opy_(config):
    return config[bstack1ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨᯆ")]
def bstack1lll111111_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack111l111l1l1_opy_(obj):
    values = []
    bstack111l1lll1ll_opy_ = re.compile(bstack1ll1l_opy_ (u"ࡸࠢ࡟ࡅࡘࡗ࡙ࡕࡍࡠࡖࡄࡋࡤࡢࡤࠬࠦࠥᯇ"), re.I)
    for key in obj.keys():
        if bstack111l1lll1ll_opy_.match(key):
            values.append(obj[key])
    return values
def bstack1111l1lll1l_opy_(config):
    tags = []
    tags.extend(bstack111l111l1l1_opy_(os.environ))
    tags.extend(bstack111l111l1l1_opy_(config))
    return tags
def bstack111l1ll1l11_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack111l1llllll_opy_(bstack111l11ll1l1_opy_):
    if not bstack111l11ll1l1_opy_:
        return bstack1ll1l_opy_ (u"ࠧࠨᯈ")
    return bstack1ll1l_opy_ (u"ࠣࡽࢀࠤ࠭ࢁࡽࠪࠤᯉ").format(bstack111l11ll1l1_opy_.name, bstack111l11ll1l1_opy_.email)
def bstack1111l1ll1ll_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack111l1111111_opy_ = repo.common_dir
        info = {
            bstack1ll1l_opy_ (u"ࠤࡶ࡬ࡦࠨᯊ"): repo.head.commit.hexsha,
            bstack1ll1l_opy_ (u"ࠥࡷ࡭ࡵࡲࡵࡡࡶ࡬ࡦࠨᯋ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack1ll1l_opy_ (u"ࠦࡧࡸࡡ࡯ࡥ࡫ࠦᯌ"): repo.active_branch.name,
            bstack1ll1l_opy_ (u"ࠧࡺࡡࡨࠤᯍ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack1ll1l_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡺࡥࡳࠤᯎ"): bstack111l1llllll_opy_(repo.head.commit.committer),
            bstack1ll1l_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡴࡦࡴࡢࡨࡦࡺࡥࠣᯏ"): repo.head.commit.committed_datetime.isoformat(),
            bstack1ll1l_opy_ (u"ࠣࡣࡸࡸ࡭ࡵࡲࠣᯐ"): bstack111l1llllll_opy_(repo.head.commit.author),
            bstack1ll1l_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࡡࡧࡥࡹ࡫ࠢᯑ"): repo.head.commit.authored_datetime.isoformat(),
            bstack1ll1l_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡢࡱࡪࡹࡳࡢࡩࡨࠦᯒ"): repo.head.commit.message,
            bstack1ll1l_opy_ (u"ࠦࡷࡵ࡯ࡵࠤᯓ"): repo.git.rev_parse(bstack1ll1l_opy_ (u"ࠧ࠳࠭ࡴࡪࡲࡻ࠲ࡺ࡯ࡱ࡮ࡨࡺࡪࡲࠢᯔ")),
            bstack1ll1l_opy_ (u"ࠨࡣࡰ࡯ࡰࡳࡳࡥࡧࡪࡶࡢࡨ࡮ࡸࠢᯕ"): bstack111l1111111_opy_,
            bstack1ll1l_opy_ (u"ࠢࡸࡱࡵ࡯ࡹࡸࡥࡦࡡࡪ࡭ࡹࡥࡤࡪࡴࠥᯖ"): subprocess.check_output([bstack1ll1l_opy_ (u"ࠣࡩ࡬ࡸࠧᯗ"), bstack1ll1l_opy_ (u"ࠤࡵࡩࡻ࠳ࡰࡢࡴࡶࡩࠧᯘ"), bstack1ll1l_opy_ (u"ࠥ࠱࠲࡭ࡩࡵ࠯ࡦࡳࡲࡳ࡯࡯࠯ࡧ࡭ࡷࠨᯙ")]).strip().decode(
                bstack1ll1l_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᯚ")),
            bstack1ll1l_opy_ (u"ࠧࡲࡡࡴࡶࡢࡸࡦ࡭ࠢᯛ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack1ll1l_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡹ࡟ࡴ࡫ࡱࡧࡪࡥ࡬ࡢࡵࡷࡣࡹࡧࡧࠣᯜ"): repo.git.rev_list(
                bstack1ll1l_opy_ (u"ࠢࡼࡿ࠱࠲ࢀࢃࠢᯝ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack1111lll11l1_opy_ = []
        for remote in remotes:
            bstack111l1ll111l_opy_ = {
                bstack1ll1l_opy_ (u"ࠣࡰࡤࡱࡪࠨᯞ"): remote.name,
                bstack1ll1l_opy_ (u"ࠤࡸࡶࡱࠨᯟ"): remote.url,
            }
            bstack1111lll11l1_opy_.append(bstack111l1ll111l_opy_)
        bstack1111l1llll1_opy_ = {
            bstack1ll1l_opy_ (u"ࠥࡲࡦࡳࡥࠣᯠ"): bstack1ll1l_opy_ (u"ࠦ࡬࡯ࡴࠣᯡ"),
            **info,
            bstack1ll1l_opy_ (u"ࠧࡸࡥ࡮ࡱࡷࡩࡸࠨᯢ"): bstack1111lll11l1_opy_
        }
        bstack1111l1llll1_opy_ = bstack111l1111lll_opy_(bstack1111l1llll1_opy_)
        return bstack1111l1llll1_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack1ll1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡯ࡱࡷ࡯ࡥࡹ࡯࡮ࡨࠢࡊ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡹ࡬ࡸ࡭ࠦࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠤᯣ").format(err))
        return {}
def bstack11lll111l1l_opy_(bstack111l1l11111_opy_=None):
    bstack1ll1l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡈࡧࡷࠤ࡬࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡷࡵ࡫ࡣࡪࡨ࡬ࡧࡦࡲ࡬ࡺࠢࡩࡳࡷࡳࡡࡵࡶࡨࡨࠥ࡬࡯ࡳࠢࡄࡍࠥࡹࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠡࡷࡶࡩࠥࡩࡡࡴࡧࡶࠤ࡫ࡵࡲࠡࡧࡤࡧ࡭ࠦࡦࡰ࡮ࡧࡩࡷࠦࡩ࡯ࠢࡷ࡬ࡪࠦ࡬ࡪࡵࡷ࠲ࠏࠦࠠࠡࠢࡄࡶ࡬ࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡩࡳࡱࡪࡥࡳࡵࠣࠬࡱ࡯ࡳࡵ࠮ࠣࡳࡵࡺࡩࡰࡰࡤࡰ࠮ࡀࠠࡍ࡫ࡶࡸࠥࡵࡦࠡࡨࡲࡰࡩ࡫ࡲࠡࡲࡤࡸ࡭ࡹࠠࡵࡱࠣࡩࡽࡺࡲࡢࡥࡷࠤ࡬࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡪࡷࡵ࡭࠯ࠢࡇࡩ࡫ࡧࡵ࡭ࡶࡶࠤࡹࡵࠠ࡜ࡱࡶ࠲࡬࡫ࡴࡤࡹࡧࠬ࠮ࡣ࠮ࠋࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡮࡬ࡷࡹࡀࠠࡍ࡫ࡶࡸࠥࡵࡦࠡࡦ࡬ࡧࡹࡹࠬࠡࡧࡤࡧ࡭ࠦࡣࡰࡰࡷࡥ࡮ࡴࡩ࡯ࡩࠣ࡫࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡩࡳࡷࠦࡡࠡࡨࡲࡰࡩ࡫ࡲ࠯ࠌࠣࠤࠥࠦࠢࠣࠤᯤ")
    if bstack111l1l11111_opy_ == None: # bstack111l1l1l1ll_opy_ for bstack11lll11ll11_opy_-repo
        bstack111l1l11111_opy_ = [os.getcwd()]
    results = []
    for folder in bstack111l1l11111_opy_:
        try:
            repo = git.Repo(folder, search_parent_directories=True)
            result = {
                bstack1ll1l_opy_ (u"ࠣࡲࡵࡍࡩࠨᯥ"): bstack1ll1l_opy_ (u"ࠤ᯦ࠥ"),
                bstack1ll1l_opy_ (u"ࠥࡪ࡮ࡲࡥࡴࡅ࡫ࡥࡳ࡭ࡥࡥࠤᯧ"): [],
                bstack1ll1l_opy_ (u"ࠦࡦࡻࡴࡩࡱࡵࡷࠧᯨ"): [],
                bstack1ll1l_opy_ (u"ࠧࡶࡲࡅࡣࡷࡩࠧᯩ"): bstack1ll1l_opy_ (u"ࠨࠢᯪ"),
                bstack1ll1l_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡍࡦࡵࡶࡥ࡬࡫ࡳࠣᯫ"): [],
                bstack1ll1l_opy_ (u"ࠣࡲࡵࡘ࡮ࡺ࡬ࡦࠤᯬ"): bstack1ll1l_opy_ (u"ࠤࠥᯭ"),
                bstack1ll1l_opy_ (u"ࠥࡴࡷࡊࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠥᯮ"): bstack1ll1l_opy_ (u"ࠦࠧᯯ"),
                bstack1ll1l_opy_ (u"ࠧࡶࡲࡓࡣࡺࡈ࡮࡬ࡦࠣᯰ"): bstack1ll1l_opy_ (u"ࠨࠢᯱ")
            }
            bstack1111lll1l1l_opy_ = repo.active_branch.name
            bstack111l1lllll1_opy_ = repo.head.commit
            result[bstack1ll1l_opy_ (u"ࠢࡱࡴࡌࡨ᯲ࠧ")] = bstack111l1lllll1_opy_.hexsha
            bstack111l111111l_opy_ = _111l111l111_opy_(repo)
            logger.debug(bstack1ll1l_opy_ (u"ࠣࡄࡤࡷࡪࠦࡢࡳࡣࡱࡧ࡭ࠦࡦࡰࡴࠣࡧࡴࡳࡰࡢࡴ࡬ࡷࡴࡴ࠺ࠡࠤ᯳") + str(bstack111l111111l_opy_) + bstack1ll1l_opy_ (u"ࠤࠥ᯴"))
            if bstack111l111111l_opy_:
                try:
                    bstack111l111l1ll_opy_ = repo.git.diff(bstack1ll1l_opy_ (u"ࠥ࠱࠲ࡴࡡ࡮ࡧ࠰ࡳࡳࡲࡹࠣ᯵"), bstack1lllll1l1_opy_ (u"ࠦࢀࡨࡡࡴࡧࡢࡦࡷࡧ࡮ࡤࡪࢀ࠲࠳࠴ࡻࡤࡷࡵࡶࡪࡴࡴࡠࡤࡵࡥࡳࡩࡨࡾࠤ᯶")).split(bstack1ll1l_opy_ (u"ࠬࡢ࡮ࠨ᯷"))
                    logger.debug(bstack1ll1l_opy_ (u"ࠨࡃࡩࡣࡱ࡫ࡪࡪࠠࡧ࡫࡯ࡩࡸࠦࡢࡦࡶࡺࡩࡪࡴࠠࡼࡤࡤࡷࡪࡥࡢࡳࡣࡱࡧ࡭ࢃࠠࡢࡰࡧࠤࢀࡩࡵࡳࡴࡨࡲࡹࡥࡢࡳࡣࡱࡧ࡭ࢃ࠺ࠡࠤ᯸") + str(bstack111l111l1ll_opy_) + bstack1ll1l_opy_ (u"ࠢࠣ᯹"))
                    result[bstack1ll1l_opy_ (u"ࠣࡨ࡬ࡰࡪࡹࡃࡩࡣࡱ࡫ࡪࡪࠢ᯺")] = [f.strip() for f in bstack111l111l1ll_opy_ if f.strip()]
                    commits = list(repo.iter_commits(bstack1lllll1l1_opy_ (u"ࠤࡾࡦࡦࡹࡥࡠࡤࡵࡥࡳࡩࡨࡾ࠰࠱ࡿࡨࡻࡲࡳࡧࡱࡸࡤࡨࡲࡢࡰࡦ࡬ࢂࠨ᯻")))
                except Exception:
                    logger.debug(bstack1ll1l_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡧࡦࡶࠣࡧ࡭ࡧ࡮ࡨࡧࡧࠤ࡫࡯࡬ࡦࡵࠣࡪࡷࡵ࡭ࠡࡤࡵࡥࡳࡩࡨࠡࡥࡲࡱࡵࡧࡲࡪࡵࡲࡲ࠳ࠦࡆࡢ࡮࡯࡭ࡳ࡭ࠠࡣࡣࡦ࡯ࠥࡺ࡯ࠡࡴࡨࡧࡪࡴࡴࠡࡥࡲࡱࡲ࡯ࡴࡴ࠰ࠥ᯼"))
                    commits = list(repo.iter_commits(max_count=10))
                    if commits:
                        result[bstack1ll1l_opy_ (u"ࠦ࡫࡯࡬ࡦࡵࡆ࡬ࡦࡴࡧࡦࡦࠥ᯽")] = _1111llll1l1_opy_(commits[:5])
            else:
                commits = list(repo.iter_commits(max_count=10))
                if commits:
                    result[bstack1ll1l_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡶࡇ࡭ࡧ࡮ࡨࡧࡧࠦ᯾")] = _1111llll1l1_opy_(commits[:5])
            bstack1111lllll1l_opy_ = set()
            bstack1111ll11ll1_opy_ = []
            for commit in commits:
                logger.debug(bstack1ll1l_opy_ (u"ࠨࡐࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡧࡴࡳ࡭ࡪࡶ࠽ࠤࠧ᯿") + str(commit.message) + bstack1ll1l_opy_ (u"ࠢࠣᰀ"))
                bstack111l1ll1111_opy_ = commit.author.name if commit.author else bstack1ll1l_opy_ (u"ࠣࡗࡱ࡯ࡳࡵࡷ࡯ࠤᰁ")
                bstack1111lllll1l_opy_.add(bstack111l1ll1111_opy_)
                bstack1111ll11ll1_opy_.append({
                    bstack1ll1l_opy_ (u"ࠤࡰࡩࡸࡹࡡࡨࡧࠥᰂ"): commit.message.strip(),
                    bstack1ll1l_opy_ (u"ࠥࡹࡸ࡫ࡲࠣᰃ"): bstack111l1ll1111_opy_
                })
            result[bstack1ll1l_opy_ (u"ࠦࡦࡻࡴࡩࡱࡵࡷࠧᰄ")] = list(bstack1111lllll1l_opy_)
            result[bstack1ll1l_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡒ࡫ࡳࡴࡣࡪࡩࡸࠨᰅ")] = bstack1111ll11ll1_opy_
            result[bstack1ll1l_opy_ (u"ࠨࡰࡳࡆࡤࡸࡪࠨᰆ")] = bstack111l1lllll1_opy_.committed_datetime.strftime(bstack1ll1l_opy_ (u"࡛ࠢࠦ࠰ࠩࡲ࠳ࠥࡥࠤᰇ"))
            if (not result[bstack1ll1l_opy_ (u"ࠣࡲࡵࡘ࡮ࡺ࡬ࡦࠤᰈ")] or result[bstack1ll1l_opy_ (u"ࠤࡳࡶ࡙࡯ࡴ࡭ࡧࠥᰉ")].strip() == bstack1ll1l_opy_ (u"ࠥࠦᰊ")) and bstack111l1lllll1_opy_.message:
                bstack111l11l1ll1_opy_ = bstack111l1lllll1_opy_.message.strip().splitlines()
                result[bstack1ll1l_opy_ (u"ࠦࡵࡸࡔࡪࡶ࡯ࡩࠧᰋ")] = bstack111l11l1ll1_opy_[0] if bstack111l11l1ll1_opy_ else bstack1ll1l_opy_ (u"ࠧࠨᰌ")
                if len(bstack111l11l1ll1_opy_) > 2:
                    result[bstack1ll1l_opy_ (u"ࠨࡰࡳࡆࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳࠨᰍ")] = bstack1ll1l_opy_ (u"ࠧ࡝ࡰࠪᰎ").join(bstack111l11l1ll1_opy_[2:]).strip()
            results.append(result)
        except Exception as err:
            logger.error(bstack1ll1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡱࡳࡹࡱࡧࡴࡪࡰࡪࠤࡌ࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡪࡴࡸࠠࡂࡋࠣࡷࡪࡲࡥࡤࡶ࡬ࡳࡳࠦࠨࡧࡱ࡯ࡨࡪࡸ࠺ࠡࡽࡩࡳࡱࡪࡥࡳࡿࠬ࠾ࠥࠨᰏ") + str(err) + bstack1ll1l_opy_ (u"ࠤࠥᰐ"))
    filtered_results = [
        result
        for result in results
        if _1111l1ll111_opy_(result)
    ]
    return filtered_results
def _1111l1ll111_opy_(result):
    bstack1ll1l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡌࡪࡲࡰࡦࡴࠣࡸࡴࠦࡣࡩࡧࡦ࡯ࠥ࡯ࡦࠡࡣࠣ࡫࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡵࡩࡸࡻ࡬ࡵࠢ࡬ࡷࠥࡼࡡ࡭࡫ࡧࠤ࠭ࡴ࡯࡯࠯ࡨࡱࡵࡺࡹࠡࡨ࡬ࡰࡪࡹࡃࡩࡣࡱ࡫ࡪࡪࠠࡢࡰࡧࠤࡦࡻࡴࡩࡱࡵࡷ࠮࠴ࠊࠡࠢࠣࠤࠧࠨࠢᰑ")
    return (
        isinstance(result.get(bstack1ll1l_opy_ (u"ࠦ࡫࡯࡬ࡦࡵࡆ࡬ࡦࡴࡧࡦࡦࠥᰒ"), None), list)
        and len(result[bstack1ll1l_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡶࡇ࡭ࡧ࡮ࡨࡧࡧࠦᰓ")]) > 0
        and isinstance(result.get(bstack1ll1l_opy_ (u"ࠨࡡࡶࡶ࡫ࡳࡷࡹࠢᰔ"), None), list)
        and len(result[bstack1ll1l_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸࡳࠣᰕ")]) > 0
    )
def _111l111l111_opy_(repo):
    bstack1ll1l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡖࡵࡽࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤࡹ࡮ࡥࠡࡤࡤࡷࡪࠦࡢࡳࡣࡱࡧ࡭ࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡨ࡫ࡹࡩࡳࠦࡲࡦࡲࡲࠤࡼ࡯ࡴࡩࡱࡸࡸࠥ࡮ࡡࡳࡦࡦࡳࡩ࡫ࡤࠡࡰࡤࡱࡪࡹࠠࡢࡰࡧࠤࡼࡵࡲ࡬ࠢࡺ࡭ࡹ࡮ࠠࡢ࡮࡯ࠤ࡛ࡉࡓࠡࡲࡵࡳࡻ࡯ࡤࡦࡴࡶ࠲ࠏࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵࠣࡸ࡭࡫ࠠࡥࡧࡩࡥࡺࡲࡴࠡࡤࡵࡥࡳࡩࡨࠡ࡫ࡩࠤࡵࡵࡳࡴ࡫ࡥࡰࡪ࠲ࠠࡦ࡮ࡶࡩࠥࡔ࡯࡯ࡧ࠱ࠎࠥࠦࠠࠡࠤࠥࠦᰖ")
    try:
        try:
            origin = repo.remotes.origin
            bstack111l1llll11_opy_ = origin.refs[bstack1ll1l_opy_ (u"ࠩࡋࡉࡆࡊࠧᰗ")]
            target = bstack111l1llll11_opy_.reference.name
            if target.startswith(bstack1ll1l_opy_ (u"ࠪࡳࡷ࡯ࡧࡪࡰ࠲ࠫᰘ")):
                return target
        except Exception:
            pass
        if repo.remotes and repo.remotes.origin.refs:
            for ref in repo.remotes.origin.refs:
                if ref.name.startswith(bstack1ll1l_opy_ (u"ࠫࡴࡸࡩࡨ࡫ࡱ࠳ࠬᰙ")):
                    return ref.name
        if repo.heads:
            return repo.heads[0].name
    except Exception:
        pass
    return None
def _1111llll1l1_opy_(commits):
    bstack1ll1l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡍࡥࡵࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡧ࡭ࡧ࡮ࡨࡧࡧࠤ࡫࡯࡬ࡦࡵࠣࡪࡷࡵ࡭ࠡࡣࠣࡰ࡮ࡹࡴࠡࡱࡩࠤࡨࡵ࡭࡮࡫ࡷࡷ࠳ࠐࠠࠡࠢࠣࠦࠧࠨᰚ")
    bstack111l111l1ll_opy_ = set()
    try:
        for commit in commits:
            if commit.parents:
                for parent in commit.parents:
                    diff = commit.diff(parent)
                    for bstack111l1l11l11_opy_ in diff:
                        if bstack111l1l11l11_opy_.a_path:
                            bstack111l111l1ll_opy_.add(bstack111l1l11l11_opy_.a_path)
                        if bstack111l1l11l11_opy_.b_path:
                            bstack111l111l1ll_opy_.add(bstack111l1l11l11_opy_.b_path)
    except Exception:
        pass
    return list(bstack111l111l1ll_opy_)
def bstack111l1111lll_opy_(bstack1111l1llll1_opy_):
    bstack111l1l1llll_opy_ = bstack1111lll111l_opy_(bstack1111l1llll1_opy_)
    if bstack111l1l1llll_opy_ and bstack111l1l1llll_opy_ > bstack11l11llllll_opy_:
        bstack1111ll1lll1_opy_ = bstack111l1l1llll_opy_ - bstack11l11llllll_opy_
        bstack111l11l1lll_opy_ = bstack1111l1l1l11_opy_(bstack1111l1llll1_opy_[bstack1ll1l_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡥ࡭ࡦࡵࡶࡥ࡬࡫ࠢᰛ")], bstack1111ll1lll1_opy_)
        bstack1111l1llll1_opy_[bstack1ll1l_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠣᰜ")] = bstack111l11l1lll_opy_
        logger.info(bstack1ll1l_opy_ (u"ࠣࡖ࡫ࡩࠥࡩ࡯࡮࡯࡬ࡸࠥ࡮ࡡࡴࠢࡥࡩࡪࡴࠠࡵࡴࡸࡲࡨࡧࡴࡦࡦ࠱ࠤࡘ࡯ࡺࡦࠢࡲࡪࠥࡩ࡯࡮࡯࡬ࡸࠥࡧࡦࡵࡧࡵࠤࡹࡸࡵ࡯ࡥࡤࡸ࡮ࡵ࡮ࠡ࡫ࡶࠤࢀࢃࠠࡌࡄࠥᰝ")
                    .format(bstack1111lll111l_opy_(bstack1111l1llll1_opy_) / 1024))
    return bstack1111l1llll1_opy_
def bstack1111lll111l_opy_(json_data):
    try:
        if json_data:
            bstack111ll11111l_opy_ = json.dumps(json_data)
            bstack111l1ll11ll_opy_ = sys.getsizeof(bstack111ll11111l_opy_)
            return bstack111l1ll11ll_opy_
    except Exception as e:
        logger.debug(bstack1ll1l_opy_ (u"ࠤࡖࡳࡲ࡫ࡴࡩ࡫ࡱ࡫ࠥࡽࡥ࡯ࡶࠣࡻࡷࡵ࡮ࡨࠢࡺ࡬࡮ࡲࡥࠡࡥࡤࡰࡨࡻ࡬ࡢࡶ࡬ࡲ࡬ࠦࡳࡪࡼࡨࠤࡴ࡬ࠠࡋࡕࡒࡒࠥࡵࡢ࡫ࡧࡦࡸ࠿ࠦࡻࡾࠤᰞ").format(e))
    return -1
def bstack1111l1l1l11_opy_(field, bstack111l11lll11_opy_):
    try:
        bstack111l1ll11l1_opy_ = len(bytes(bstack11l1l1l11ll_opy_, bstack1ll1l_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᰟ")))
        bstack1111ll1l1ll_opy_ = bytes(field, bstack1ll1l_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᰠ"))
        bstack1111l1lll11_opy_ = len(bstack1111ll1l1ll_opy_)
        bstack111ll1111ll_opy_ = ceil(bstack1111l1lll11_opy_ - bstack111l11lll11_opy_ - bstack111l1ll11l1_opy_)
        if bstack111ll1111ll_opy_ > 0:
            bstack1111ll1l111_opy_ = bstack1111ll1l1ll_opy_[:bstack111ll1111ll_opy_].decode(bstack1ll1l_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫᰡ"), errors=bstack1ll1l_opy_ (u"࠭ࡩࡨࡰࡲࡶࡪ࠭ᰢ")) + bstack11l1l1l11ll_opy_
            return bstack1111ll1l111_opy_
    except Exception as e:
        logger.debug(bstack1ll1l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡺࡲࡶࡰࡦࡥࡹ࡯࡮ࡨࠢࡩ࡭ࡪࡲࡤ࠭ࠢࡱࡳࡹ࡮ࡩ࡯ࡩࠣࡻࡦࡹࠠࡵࡴࡸࡲࡨࡧࡴࡦࡦࠣ࡬ࡪࡸࡥ࠻ࠢࡾࢁࠧᰣ").format(e))
    return field
def bstack1ll1l11l1_opy_():
    env = os.environ
    if (bstack1ll1l_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡘࡖࡑࠨᰤ") in env and len(env[bstack1ll1l_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢ࡙ࡗࡒࠢᰥ")]) > 0) or (
            bstack1ll1l_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣࡍࡕࡍࡆࠤᰦ") in env and len(env[bstack1ll1l_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤࡎࡏࡎࡇࠥᰧ")]) > 0):
        return {
            bstack1ll1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᰨ"): bstack1ll1l_opy_ (u"ࠨࡊࡦࡰ࡮࡭ࡳࡹࠢᰩ"),
            bstack1ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᰪ"): env.get(bstack1ll1l_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦᰫ")),
            bstack1ll1l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᰬ"): env.get(bstack1ll1l_opy_ (u"ࠥࡎࡔࡈ࡟ࡏࡃࡐࡉࠧᰭ")),
            bstack1ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᰮ"): env.get(bstack1ll1l_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᰯ"))
        }
    if env.get(bstack1ll1l_opy_ (u"ࠨࡃࡊࠤᰰ")) == bstack1ll1l_opy_ (u"ࠢࡵࡴࡸࡩࠧᰱ") and bstack1lll1ll111_opy_(env.get(bstack1ll1l_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡄࡋࠥᰲ"))):
        return {
            bstack1ll1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᰳ"): bstack1ll1l_opy_ (u"ࠥࡇ࡮ࡸࡣ࡭ࡧࡆࡍࠧᰴ"),
            bstack1ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᰵ"): env.get(bstack1ll1l_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᰶ")),
            bstack1ll1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥ᰷ࠣ"): env.get(bstack1ll1l_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋ࡟ࡋࡑࡅࠦ᰸")),
            bstack1ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ᰹"): env.get(bstack1ll1l_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࠧ᰺"))
        }
    if env.get(bstack1ll1l_opy_ (u"ࠥࡇࡎࠨ᰻")) == bstack1ll1l_opy_ (u"ࠦࡹࡸࡵࡦࠤ᰼") and bstack1lll1ll111_opy_(env.get(bstack1ll1l_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࠧ᰽"))):
        return {
            bstack1ll1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ᰾"): bstack1ll1l_opy_ (u"ࠢࡕࡴࡤࡺ࡮ࡹࠠࡄࡋࠥ᰿"),
            bstack1ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ᱀"): env.get(bstack1ll1l_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࡡࡅ࡙ࡎࡒࡄࡠ࡙ࡈࡆࡤ࡛ࡒࡍࠤ᱁")),
            bstack1ll1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ᱂"): env.get(bstack1ll1l_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨ᱃")),
            bstack1ll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ᱄"): env.get(bstack1ll1l_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧ᱅"))
        }
    if env.get(bstack1ll1l_opy_ (u"ࠢࡄࡋࠥ᱆")) == bstack1ll1l_opy_ (u"ࠣࡶࡵࡹࡪࠨ᱇") and env.get(bstack1ll1l_opy_ (u"ࠤࡆࡍࡤࡔࡁࡎࡇࠥ᱈")) == bstack1ll1l_opy_ (u"ࠥࡧࡴࡪࡥࡴࡪ࡬ࡴࠧ᱉"):
        return {
            bstack1ll1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᱊"): bstack1ll1l_opy_ (u"ࠧࡉ࡯ࡥࡧࡶ࡬࡮ࡶࠢ᱋"),
            bstack1ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᱌"): None,
            bstack1ll1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᱍ"): None,
            bstack1ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᱎ"): None
        }
    if env.get(bstack1ll1l_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡈࡒࡂࡐࡆࡌࠧᱏ")) and env.get(bstack1ll1l_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡃࡐࡏࡐࡍ࡙ࠨ᱐")):
        return {
            bstack1ll1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᱑"): bstack1ll1l_opy_ (u"ࠧࡈࡩࡵࡤࡸࡧࡰ࡫ࡴࠣ᱒"),
            bstack1ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᱓"): env.get(bstack1ll1l_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡋࡎ࡚࡟ࡉࡖࡗࡔࡤࡕࡒࡊࡉࡌࡒࠧ᱔")),
            bstack1ll1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᱕"): None,
            bstack1ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᱖"): env.get(bstack1ll1l_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧ᱗"))
        }
    if env.get(bstack1ll1l_opy_ (u"ࠦࡈࡏࠢ᱘")) == bstack1ll1l_opy_ (u"ࠧࡺࡲࡶࡧࠥ᱙") and bstack1lll1ll111_opy_(env.get(bstack1ll1l_opy_ (u"ࠨࡄࡓࡑࡑࡉࠧᱚ"))):
        return {
            bstack1ll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᱛ"): bstack1ll1l_opy_ (u"ࠣࡆࡵࡳࡳ࡫ࠢᱜ"),
            bstack1ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᱝ"): env.get(bstack1ll1l_opy_ (u"ࠥࡈࡗࡕࡎࡆࡡࡅ࡙ࡎࡒࡄࡠࡎࡌࡒࡐࠨᱞ")),
            bstack1ll1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᱟ"): None,
            bstack1ll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᱠ"): env.get(bstack1ll1l_opy_ (u"ࠨࡄࡓࡑࡑࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᱡ"))
        }
    if env.get(bstack1ll1l_opy_ (u"ࠢࡄࡋࠥᱢ")) == bstack1ll1l_opy_ (u"ࠣࡶࡵࡹࡪࠨᱣ") and bstack1lll1ll111_opy_(env.get(bstack1ll1l_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࠧᱤ"))):
        return {
            bstack1ll1l_opy_ (u"ࠥࡲࡦࡳࡥࠣᱥ"): bstack1ll1l_opy_ (u"ࠦࡘ࡫࡭ࡢࡲ࡫ࡳࡷ࡫ࠢᱦ"),
            bstack1ll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᱧ"): env.get(bstack1ll1l_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࡡࡒࡖࡌࡇࡎࡊ࡜ࡄࡘࡎࡕࡎࡠࡗࡕࡐࠧᱨ")),
            bstack1ll1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᱩ"): env.get(bstack1ll1l_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᱪ")),
            bstack1ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᱫ"): env.get(bstack1ll1l_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࡥࡊࡐࡄࡢࡍࡉࠨᱬ"))
        }
    if env.get(bstack1ll1l_opy_ (u"ࠦࡈࡏࠢᱭ")) == bstack1ll1l_opy_ (u"ࠧࡺࡲࡶࡧࠥᱮ") and bstack1lll1ll111_opy_(env.get(bstack1ll1l_opy_ (u"ࠨࡇࡊࡖࡏࡅࡇࡥࡃࡊࠤᱯ"))):
        return {
            bstack1ll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᱰ"): bstack1ll1l_opy_ (u"ࠣࡉ࡬ࡸࡑࡧࡢࠣᱱ"),
            bstack1ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᱲ"): env.get(bstack1ll1l_opy_ (u"ࠥࡇࡎࡥࡊࡐࡄࡢ࡙ࡗࡒࠢᱳ")),
            bstack1ll1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᱴ"): env.get(bstack1ll1l_opy_ (u"ࠧࡉࡉࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᱵ")),
            bstack1ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᱶ"): env.get(bstack1ll1l_opy_ (u"ࠢࡄࡋࡢࡎࡔࡈ࡟ࡊࡆࠥᱷ"))
        }
    if env.get(bstack1ll1l_opy_ (u"ࠣࡅࡌࠦᱸ")) == bstack1ll1l_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᱹ") and bstack1lll1ll111_opy_(env.get(bstack1ll1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࠨᱺ"))):
        return {
            bstack1ll1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᱻ"): bstack1ll1l_opy_ (u"ࠧࡈࡵࡪ࡮ࡧ࡯࡮ࡺࡥࠣᱼ"),
            bstack1ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᱽ"): env.get(bstack1ll1l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨ᱾")),
            bstack1ll1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᱿"): env.get(bstack1ll1l_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡒࡁࡃࡇࡏࠦᲀ")) or env.get(bstack1ll1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡐࡄࡑࡊࠨᲁ")),
            bstack1ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᲂ"): env.get(bstack1ll1l_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᲃ"))
        }
    if bstack1lll1ll111_opy_(env.get(bstack1ll1l_opy_ (u"ࠨࡔࡇࡡࡅ࡙ࡎࡒࡄࠣᲄ"))):
        return {
            bstack1ll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᲅ"): bstack1ll1l_opy_ (u"ࠣࡘ࡬ࡷࡺࡧ࡬ࠡࡕࡷࡹࡩ࡯࡯ࠡࡖࡨࡥࡲࠦࡓࡦࡴࡹ࡭ࡨ࡫ࡳࠣᲆ"),
            bstack1ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᲇ"): bstack1ll1l_opy_ (u"ࠥࡿࢂࢁࡽࠣᲈ").format(env.get(bstack1ll1l_opy_ (u"ࠫࡘ࡟ࡓࡕࡇࡐࡣ࡙ࡋࡁࡎࡈࡒ࡙ࡓࡊࡁࡕࡋࡒࡒࡘࡋࡒࡗࡇࡕ࡙ࡗࡏࠧᲉ")), env.get(bstack1ll1l_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡓࡖࡔࡐࡅࡄࡖࡌࡈࠬᲊ"))),
            bstack1ll1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ᲋"): env.get(bstack1ll1l_opy_ (u"ࠢࡔ࡛ࡖࡘࡊࡓ࡟ࡅࡇࡉࡍࡓࡏࡔࡊࡑࡑࡍࡉࠨ᲌")),
            bstack1ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ᲍"): env.get(bstack1ll1l_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠤ᲎"))
        }
    if bstack1lll1ll111_opy_(env.get(bstack1ll1l_opy_ (u"ࠥࡅࡕࡖࡖࡆ࡛ࡒࡖࠧ᲏"))):
        return {
            bstack1ll1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᲐ"): bstack1ll1l_opy_ (u"ࠧࡇࡰࡱࡸࡨࡽࡴࡸࠢᲑ"),
            bstack1ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᲒ"): bstack1ll1l_opy_ (u"ࠢࡼࡿ࠲ࡴࡷࡵࡪࡦࡥࡷ࠳ࢀࢃ࠯ࡼࡿ࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂࠨᲓ").format(env.get(bstack1ll1l_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢ࡙ࡗࡒࠧᲔ")), env.get(bstack1ll1l_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡆࡉࡃࡐࡗࡑࡘࡤࡔࡁࡎࡇࠪᲕ")), env.get(bstack1ll1l_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡖࡒࡐࡌࡈࡇ࡙ࡥࡓࡍࡗࡊࠫᲖ")), env.get(bstack1ll1l_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨᲗ"))),
            bstack1ll1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᲘ"): env.get(bstack1ll1l_opy_ (u"ࠨࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᲙ")),
            bstack1ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᲚ"): env.get(bstack1ll1l_opy_ (u"ࠣࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᲛ"))
        }
    if env.get(bstack1ll1l_opy_ (u"ࠤࡄ࡞࡚ࡘࡅࡠࡊࡗࡘࡕࡥࡕࡔࡇࡕࡣࡆࡍࡅࡏࡖࠥᲜ")) and env.get(bstack1ll1l_opy_ (u"ࠥࡘࡋࡥࡂࡖࡋࡏࡈࠧᲝ")):
        return {
            bstack1ll1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᲞ"): bstack1ll1l_opy_ (u"ࠧࡇࡺࡶࡴࡨࠤࡈࡏࠢᲟ"),
            bstack1ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᲠ"): bstack1ll1l_opy_ (u"ࠢࡼࡿࡾࢁ࠴ࡥࡢࡶ࡫࡯ࡨ࠴ࡸࡥࡴࡷ࡯ࡸࡸࡅࡢࡶ࡫࡯ࡨࡎࡪ࠽ࡼࡿࠥᲡ").format(env.get(bstack1ll1l_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡌࡏࡖࡐࡇࡅ࡙ࡏࡏࡏࡕࡈࡖ࡛ࡋࡒࡖࡔࡌࠫᲢ")), env.get(bstack1ll1l_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡐࡓࡑࡍࡉࡈ࡚ࠧᲣ")), env.get(bstack1ll1l_opy_ (u"ࠪࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠪᲤ"))),
            bstack1ll1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᲥ"): env.get(bstack1ll1l_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠧᲦ")),
            bstack1ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᲧ"): env.get(bstack1ll1l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠢᲨ"))
        }
    if any([env.get(bstack1ll1l_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᲩ")), env.get(bstack1ll1l_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡘࡅࡔࡑࡏ࡚ࡊࡊ࡟ࡔࡑࡘࡖࡈࡋ࡟ࡗࡇࡕࡗࡎࡕࡎࠣᲪ")), env.get(bstack1ll1l_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡓࡐࡗࡕࡇࡊࡥࡖࡆࡔࡖࡍࡔࡔࠢᲫ"))]):
        return {
            bstack1ll1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᲬ"): bstack1ll1l_opy_ (u"ࠧࡇࡗࡔࠢࡆࡳࡩ࡫ࡂࡶ࡫࡯ࡨࠧᲭ"),
            bstack1ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᲮ"): env.get(bstack1ll1l_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡔ࡚ࡈࡌࡊࡅࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᲯ")),
            bstack1ll1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᲰ"): env.get(bstack1ll1l_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢᲱ")),
            bstack1ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᲲ"): env.get(bstack1ll1l_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤᲳ"))
        }
    if env.get(bstack1ll1l_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡨࡵࡪ࡮ࡧࡒࡺࡳࡢࡦࡴࠥᲴ")):
        return {
            bstack1ll1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᲵ"): bstack1ll1l_opy_ (u"ࠢࡃࡣࡰࡦࡴࡵࠢᲶ"),
            bstack1ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᲷ"): env.get(bstack1ll1l_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡥࡹ࡮ࡲࡤࡓࡧࡶࡹࡱࡺࡳࡖࡴ࡯ࠦᲸ")),
            bstack1ll1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᲹ"): env.get(bstack1ll1l_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡸ࡮࡯ࡳࡶࡍࡳࡧࡔࡡ࡮ࡧࠥᲺ")),
            bstack1ll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ᲻"): env.get(bstack1ll1l_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡢࡶ࡫࡯ࡨࡓࡻ࡭ࡣࡧࡵࠦ᲼"))
        }
    if env.get(bstack1ll1l_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࠣᲽ")) or env.get(bstack1ll1l_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡐࡅࡎࡔ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡖࡘࡆࡘࡔࡆࡆࠥᲾ")):
        return {
            bstack1ll1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᲿ"): bstack1ll1l_opy_ (u"࡛ࠥࡪࡸࡣ࡬ࡧࡵࠦ᳀"),
            bstack1ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ᳁"): env.get(bstack1ll1l_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤ᳂")),
            bstack1ll1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ᳃"): bstack1ll1l_opy_ (u"ࠢࡎࡣ࡬ࡲࠥࡖࡩࡱࡧ࡯࡭ࡳ࡫ࠢ᳄") if env.get(bstack1ll1l_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡐࡅࡎࡔ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡖࡘࡆࡘࡔࡆࡆࠥ᳅")) else None,
            bstack1ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᳆"): env.get(bstack1ll1l_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡌࡏࡔࡠࡅࡒࡑࡒࡏࡔࠣ᳇"))
        }
    if any([env.get(bstack1ll1l_opy_ (u"ࠦࡌࡉࡐࡠࡒࡕࡓࡏࡋࡃࡕࠤ᳈")), env.get(bstack1ll1l_opy_ (u"ࠧࡍࡃࡍࡑࡘࡈࡤࡖࡒࡐࡌࡈࡇ࡙ࠨ᳉")), env.get(bstack1ll1l_opy_ (u"ࠨࡇࡐࡑࡊࡐࡊࡥࡃࡍࡑࡘࡈࡤࡖࡒࡐࡌࡈࡇ࡙ࠨ᳊"))]):
        return {
            bstack1ll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᳋"): bstack1ll1l_opy_ (u"ࠣࡉࡲࡳ࡬ࡲࡥࠡࡅ࡯ࡳࡺࡪࠢ᳌"),
            bstack1ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ᳍"): None,
            bstack1ll1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ᳎"): env.get(bstack1ll1l_opy_ (u"ࠦࡕࡘࡏࡋࡇࡆࡘࡤࡏࡄࠣ᳏")),
            bstack1ll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ᳐"): env.get(bstack1ll1l_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡏࡄࠣ᳑"))
        }
    if env.get(bstack1ll1l_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࠥ᳒")):
        return {
            bstack1ll1l_opy_ (u"ࠣࡰࡤࡱࡪࠨ᳓"): bstack1ll1l_opy_ (u"ࠤࡖ࡬࡮ࡶࡰࡢࡤ࡯ࡩ᳔ࠧ"),
            bstack1ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᳕"): env.get(bstack1ll1l_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎ᳖ࠥ")),
            bstack1ll1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫᳗ࠢ"): bstack1ll1l_opy_ (u"ࠨࡊࡰࡤࠣࠧࢀࢃ᳘ࠢ").format(env.get(bstack1ll1l_opy_ (u"ࠧࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡎࡔࡈ࡟ࡊࡆ᳙ࠪ"))) if env.get(bstack1ll1l_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡏࡕࡂࡠࡋࡇࠦ᳚")) else None,
            bstack1ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᳛"): env.get(bstack1ll1l_opy_ (u"ࠥࡗࡍࡏࡐࡑࡃࡅࡐࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖ᳜ࠧ"))
        }
    if bstack1lll1ll111_opy_(env.get(bstack1ll1l_opy_ (u"ࠦࡓࡋࡔࡍࡋࡉ࡝᳝ࠧ"))):
        return {
            bstack1ll1l_opy_ (u"ࠧࡴࡡ࡮ࡧ᳞ࠥ"): bstack1ll1l_opy_ (u"ࠨࡎࡦࡶ࡯࡭࡫ࡿ᳟ࠢ"),
            bstack1ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ᳠"): env.get(bstack1ll1l_opy_ (u"ࠣࡆࡈࡔࡑࡕ࡙ࡠࡗࡕࡐࠧ᳡")),
            bstack1ll1l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨ᳢ࠦ"): env.get(bstack1ll1l_opy_ (u"ࠥࡗࡎ࡚ࡅࡠࡐࡄࡑࡊࠨ᳣")),
            bstack1ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴ᳤ࠥ"): env.get(bstack1ll1l_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊ᳥ࠢ"))
        }
    if bstack1lll1ll111_opy_(env.get(bstack1ll1l_opy_ (u"ࠨࡇࡊࡖࡋ࡙ࡇࡥࡁࡄࡖࡌࡓࡓ᳦࡙ࠢ"))):
        return {
            bstack1ll1l_opy_ (u"ࠢ࡯ࡣࡰࡩ᳧ࠧ"): bstack1ll1l_opy_ (u"ࠣࡉ࡬ࡸࡍࡻࡢࠡࡃࡦࡸ࡮ࡵ࡮ࡴࠤ᳨"),
            bstack1ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᳩ"): bstack1ll1l_opy_ (u"ࠥࡿࢂ࠵ࡻࡾ࠱ࡤࡧࡹ࡯࡯࡯ࡵ࠲ࡶࡺࡴࡳ࠰ࡽࢀࠦᳪ").format(env.get(bstack1ll1l_opy_ (u"ࠫࡌࡏࡔࡉࡗࡅࡣࡘࡋࡒࡗࡇࡕࡣ࡚ࡘࡌࠨᳫ")), env.get(bstack1ll1l_opy_ (u"ࠬࡍࡉࡕࡊࡘࡆࡤࡘࡅࡑࡑࡖࡍ࡙ࡕࡒ࡚ࠩᳬ")), env.get(bstack1ll1l_opy_ (u"࠭ࡇࡊࡖࡋ࡙ࡇࡥࡒࡖࡐࡢࡍࡉ᳭࠭"))),
            bstack1ll1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᳮ"): env.get(bstack1ll1l_opy_ (u"ࠣࡉࡌࡘࡍ࡛ࡂࡠ࡙ࡒࡖࡐࡌࡌࡐ࡙ࠥᳯ")),
            bstack1ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᳰ"): env.get(bstack1ll1l_opy_ (u"ࠥࡋࡎ࡚ࡈࡖࡄࡢࡖ࡚ࡔ࡟ࡊࡆࠥᳱ"))
        }
    if env.get(bstack1ll1l_opy_ (u"ࠦࡈࡏࠢᳲ")) == bstack1ll1l_opy_ (u"ࠧࡺࡲࡶࡧࠥᳳ") and env.get(bstack1ll1l_opy_ (u"ࠨࡖࡆࡔࡆࡉࡑࠨ᳴")) == bstack1ll1l_opy_ (u"ࠢ࠲ࠤᳵ"):
        return {
            bstack1ll1l_opy_ (u"ࠣࡰࡤࡱࡪࠨᳶ"): bstack1ll1l_opy_ (u"ࠤ࡙ࡩࡷࡩࡥ࡭ࠤ᳷"),
            bstack1ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᳸"): bstack1ll1l_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࢀࢃࠢ᳹").format(env.get(bstack1ll1l_opy_ (u"ࠬ࡜ࡅࡓࡅࡈࡐࡤ࡛ࡒࡍࠩᳺ"))),
            bstack1ll1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ᳻"): None,
            bstack1ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᳼"): None,
        }
    if env.get(bstack1ll1l_opy_ (u"ࠣࡖࡈࡅࡒࡉࡉࡕ࡛ࡢ࡚ࡊࡘࡓࡊࡑࡑࠦ᳽")):
        return {
            bstack1ll1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᳾"): bstack1ll1l_opy_ (u"ࠥࡘࡪࡧ࡭ࡤ࡫ࡷࡽࠧ᳿"),
            bstack1ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᴀ"): None,
            bstack1ll1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᴁ"): env.get(bstack1ll1l_opy_ (u"ࠨࡔࡆࡃࡐࡇࡎ࡚࡙ࡠࡒࡕࡓࡏࡋࡃࡕࡡࡑࡅࡒࡋࠢᴂ")),
            bstack1ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᴃ"): env.get(bstack1ll1l_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᴄ"))
        }
    if any([env.get(bstack1ll1l_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࠧᴅ")), env.get(bstack1ll1l_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࡥࡕࡓࡎࠥᴆ")), env.get(bstack1ll1l_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠤᴇ")), env.get(bstack1ll1l_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࡠࡖࡈࡅࡒࠨᴈ"))]):
        return {
            bstack1ll1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᴉ"): bstack1ll1l_opy_ (u"ࠢࡄࡱࡱࡧࡴࡻࡲࡴࡧࠥᴊ"),
            bstack1ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᴋ"): None,
            bstack1ll1l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᴌ"): env.get(bstack1ll1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᴍ")) or None,
            bstack1ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᴎ"): env.get(bstack1ll1l_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢᴏ"), 0)
        }
    if env.get(bstack1ll1l_opy_ (u"ࠨࡇࡐࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᴐ")):
        return {
            bstack1ll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᴑ"): bstack1ll1l_opy_ (u"ࠣࡉࡲࡇࡉࠨᴒ"),
            bstack1ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᴓ"): None,
            bstack1ll1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᴔ"): env.get(bstack1ll1l_opy_ (u"ࠦࡌࡕ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᴕ")),
            bstack1ll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᴖ"): env.get(bstack1ll1l_opy_ (u"ࠨࡇࡐࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡈࡕࡕࡏࡖࡈࡖࠧᴗ"))
        }
    if env.get(bstack1ll1l_opy_ (u"ࠢࡄࡈࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᴘ")):
        return {
            bstack1ll1l_opy_ (u"ࠣࡰࡤࡱࡪࠨᴙ"): bstack1ll1l_opy_ (u"ࠤࡆࡳࡩ࡫ࡆࡳࡧࡶ࡬ࠧᴚ"),
            bstack1ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᴛ"): env.get(bstack1ll1l_opy_ (u"ࠦࡈࡌ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᴜ")),
            bstack1ll1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᴝ"): env.get(bstack1ll1l_opy_ (u"ࠨࡃࡇࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡓࡇࡍࡆࠤᴞ")),
            bstack1ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᴟ"): env.get(bstack1ll1l_opy_ (u"ࠣࡅࡉࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᴠ"))
        }
    return {bstack1ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᴡ"): None}
def get_host_info():
    return {
        bstack1ll1l_opy_ (u"ࠥ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠧᴢ"): platform.node(),
        bstack1ll1l_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࠨᴣ"): platform.system(),
        bstack1ll1l_opy_ (u"ࠧࡺࡹࡱࡧࠥᴤ"): platform.machine(),
        bstack1ll1l_opy_ (u"ࠨࡶࡦࡴࡶ࡭ࡴࡴࠢᴥ"): platform.version(),
        bstack1ll1l_opy_ (u"ࠢࡢࡴࡦ࡬ࠧᴦ"): platform.architecture()[0]
    }
def bstack111lll111_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack1111lllllll_opy_():
    if bstack111111ll_opy_.get_property(bstack1ll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩᴧ")):
        return bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᴨ")
    return bstack1ll1l_opy_ (u"ࠪࡹࡳࡱ࡮ࡰࡹࡱࡣ࡬ࡸࡩࡥࠩᴩ")
def bstack111l11ll1ll_opy_(driver):
    info = {
        bstack1ll1l_opy_ (u"ࠫࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪᴪ"): driver.capabilities,
        bstack1ll1l_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠩᴫ"): driver.session_id,
        bstack1ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧᴬ"): driver.capabilities.get(bstack1ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬᴭ"), None),
        bstack1ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪᴮ"): driver.capabilities.get(bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᴯ"), None),
        bstack1ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࠬᴰ"): driver.capabilities.get(bstack1ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠪᴱ"), None),
        bstack1ll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᴲ"):driver.capabilities.get(bstack1ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᴳ"), None),
    }
    if bstack1111lllllll_opy_() == bstack1ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᴴ"):
        if bstack11lll1l111_opy_():
            info[bstack1ll1l_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࠩᴵ")] = bstack1ll1l_opy_ (u"ࠩࡤࡴࡵ࠳ࡡࡶࡶࡲࡱࡦࡺࡥࠨᴶ")
        elif driver.capabilities.get(bstack1ll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᴷ"), {}).get(bstack1ll1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨᴸ"), False):
            info[bstack1ll1l_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭ᴹ")] = bstack1ll1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪᴺ")
        else:
            info[bstack1ll1l_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࠨᴻ")] = bstack1ll1l_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪᴼ")
    return info
def bstack11lll1l111_opy_():
    if bstack111111ll_opy_.get_property(bstack1ll1l_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨᴽ")):
        return True
    if bstack1lll1ll111_opy_(os.environ.get(bstack1ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫᴾ"), None)):
        return True
    return False
def bstack1l11lllll_opy_(bstack111l111llll_opy_, url, data, config):
    headers = config.get(bstack1ll1l_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬᴿ"), None)
    proxies = bstack111l1l1ll_opy_(config, url)
    auth = config.get(bstack1ll1l_opy_ (u"ࠬࡧࡵࡵࡪࠪᵀ"), None)
    response = requests.request(
            bstack111l111llll_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack11l1ll1ll1_opy_(bstack1111l1111_opy_, size):
    bstack1ll111l1ll_opy_ = []
    while len(bstack1111l1111_opy_) > size:
        bstack1111lll111_opy_ = bstack1111l1111_opy_[:size]
        bstack1ll111l1ll_opy_.append(bstack1111lll111_opy_)
        bstack1111l1111_opy_ = bstack1111l1111_opy_[size:]
    bstack1ll111l1ll_opy_.append(bstack1111l1111_opy_)
    return bstack1ll111l1ll_opy_
def bstack1111ll1l1l1_opy_(message, bstack1111llll111_opy_=False):
    os.write(1, bytes(message, bstack1ll1l_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᵁ")))
    os.write(1, bytes(bstack1ll1l_opy_ (u"ࠧ࡝ࡰࠪᵂ"), bstack1ll1l_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧᵃ")))
    if bstack1111llll111_opy_:
        with open(bstack1ll1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠯ࡲ࠵࠶ࡿ࠭ࠨᵄ") + os.environ[bstack1ll1l_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩᵅ")] + bstack1ll1l_opy_ (u"ࠫ࠳ࡲ࡯ࡨࠩᵆ"), bstack1ll1l_opy_ (u"ࠬࡧࠧᵇ")) as f:
            f.write(message + bstack1ll1l_opy_ (u"࠭࡜࡯ࠩᵈ"))
def bstack1lll1llll1l_opy_():
    return os.environ[bstack1ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪᵉ")].lower() == bstack1ll1l_opy_ (u"ࠨࡶࡵࡹࡪ࠭ᵊ")
def bstack1l1l1lll_opy_():
    return bstack1ll1111l_opy_().replace(tzinfo=None).isoformat() + bstack1ll1l_opy_ (u"ࠩ࡝ࠫᵋ")
def bstack1111ll1ll1l_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack1ll1l_opy_ (u"ࠪ࡞ࠬᵌ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack1ll1l_opy_ (u"ࠫ࡟࠭ᵍ")))).total_seconds() * 1000
def bstack111l1l111ll_opy_(timestamp):
    return bstack111l11lll1l_opy_(timestamp).isoformat() + bstack1ll1l_opy_ (u"ࠬࡠࠧᵎ")
def bstack1111ll111l1_opy_(bstack111ll111l11_opy_):
    date_format = bstack1ll1l_opy_ (u"࡚࠭ࠥࠧࡰࠩࡩࠦࠥࡉ࠼ࠨࡑ࠿ࠫࡓ࠯ࠧࡩࠫᵏ")
    bstack1111ll1111l_opy_ = datetime.datetime.strptime(bstack111ll111l11_opy_, date_format)
    return bstack1111ll1111l_opy_.isoformat() + bstack1ll1l_opy_ (u"࡛ࠧࠩᵐ")
def bstack111l1l1l111_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack1ll1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᵑ")
    else:
        return bstack1ll1l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᵒ")
def bstack1lll1ll111_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack1ll1l_opy_ (u"ࠪࡸࡷࡻࡥࠨᵓ")
def bstack111l1ll1lll_opy_(val):
    return val.__str__().lower() == bstack1ll1l_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪᵔ")
def error_handler(bstack111l11l1l11_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack111l11l1l11_opy_ as e:
                print(bstack1ll1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࡻࡾࠢ࠰ࡂࠥࢁࡽ࠻ࠢࡾࢁࠧᵕ").format(func.__name__, bstack111l11l1l11_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack1111l1l1lll_opy_(bstack1111ll1l11l_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack1111ll1l11l_opy_(cls, *args, **kwargs)
            except bstack111l11l1l11_opy_ as e:
                print(bstack1ll1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡼࡿࠣ࠱ࡃࠦࡻࡾ࠼ࠣࡿࢂࠨᵖ").format(bstack1111ll1l11l_opy_.__name__, bstack111l11l1l11_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack1111l1l1lll_opy_
    else:
        return decorator
def bstack11l11ll11_opy_(bstack111l1111_opy_):
    if os.getenv(bstack1ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪᵗ")) is not None:
        return bstack1lll1ll111_opy_(os.getenv(bstack1ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫᵘ")))
    if bstack1ll1l_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᵙ") in bstack111l1111_opy_ and bstack111l1ll1lll_opy_(bstack111l1111_opy_[bstack1ll1l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᵚ")]):
        return False
    if bstack1ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᵛ") in bstack111l1111_opy_ and bstack111l1ll1lll_opy_(bstack111l1111_opy_[bstack1ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᵜ")]):
        return False
    return True
def bstack111ll1llll_opy_():
    try:
        from pytest_bdd import reporting
        bstack111l1l11lll_opy_ = os.environ.get(bstack1ll1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡛ࡓࡆࡔࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࠨᵝ"), None)
        return bstack111l1l11lll_opy_ is None or bstack111l1l11lll_opy_ == bstack1ll1l_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠦᵞ")
    except Exception as e:
        return False
def bstack1l1l1llll_opy_(hub_url, CONFIG):
    if bstack111lllll1_opy_() <= version.parse(bstack1ll1l_opy_ (u"ࠨ࠵࠱࠵࠸࠴࠰ࠨᵟ")):
        if hub_url:
            return bstack1ll1l_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥᵠ") + hub_url + bstack1ll1l_opy_ (u"ࠥ࠾࠽࠶࠯ࡸࡦ࠲࡬ࡺࡨࠢᵡ")
        return bstack1llll1l1ll_opy_
    if hub_url:
        return bstack1ll1l_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨᵢ") + hub_url + bstack1ll1l_opy_ (u"ࠧ࠵ࡷࡥ࠱࡫ࡹࡧࠨᵣ")
    return bstack111l1llll1_opy_
def bstack1111ll11111_opy_():
    return isinstance(os.getenv(bstack1ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖ࡙ࡕࡇࡖࡘࡤࡖࡌࡖࡉࡌࡒࠬᵤ")), str)
def bstack1l111l11l1_opy_(url):
    return urlparse(url).hostname
def bstack11llllll11_opy_(hostname):
    for bstack1lll11111_opy_ in bstack1ll1ll11l1_opy_:
        regex = re.compile(bstack1lll11111_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11ll111lll1_opy_(bstack111l111l11l_opy_, file_name, logger):
    bstack1l1l1lllll_opy_ = os.path.join(os.path.expanduser(bstack1ll1l_opy_ (u"ࠧࡿࠩᵥ")), bstack111l111l11l_opy_)
    try:
        if not os.path.exists(bstack1l1l1lllll_opy_):
            os.makedirs(bstack1l1l1lllll_opy_)
        file_path = os.path.join(os.path.expanduser(bstack1ll1l_opy_ (u"ࠨࢀࠪᵦ")), bstack111l111l11l_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack1ll1l_opy_ (u"ࠩࡺࠫᵧ")):
                pass
            with open(file_path, bstack1ll1l_opy_ (u"ࠥࡻ࠰ࠨᵨ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack11ll11llll_opy_.format(str(e)))
def bstack11ll111ll11_opy_(file_name, key, value, logger):
    file_path = bstack11ll111lll1_opy_(bstack1ll1l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᵩ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack11111llll_opy_ = json.load(open(file_path, bstack1ll1l_opy_ (u"ࠬࡸࡢࠨᵪ")))
        else:
            bstack11111llll_opy_ = {}
        bstack11111llll_opy_[key] = value
        with open(file_path, bstack1ll1l_opy_ (u"ࠨࡷࠬࠤᵫ")) as outfile:
            json.dump(bstack11111llll_opy_, outfile)
def bstack11l1l11l11_opy_(file_name, logger):
    file_path = bstack11ll111lll1_opy_(bstack1ll1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᵬ"), file_name, logger)
    bstack11111llll_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack1ll1l_opy_ (u"ࠨࡴࠪᵭ")) as bstack1lll11l11_opy_:
            bstack11111llll_opy_ = json.load(bstack1lll11l11_opy_)
    return bstack11111llll_opy_
def bstack1ll11lll1_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack1ll1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡩ࡫࡬ࡦࡶ࡬ࡲ࡬ࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ᵮ") + file_path + bstack1ll1l_opy_ (u"ࠪࠤࠬᵯ") + str(e))
def bstack111lllll1_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack1ll1l_opy_ (u"ࠦࡁࡔࡏࡕࡕࡈࡘࡃࠨᵰ")
def bstack1l1ll1ll1l_opy_(config):
    if bstack1ll1l_opy_ (u"ࠬ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫᵱ") in config:
        del (config[bstack1ll1l_opy_ (u"࠭ࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬᵲ")])
        return False
    if bstack111lllll1_opy_() < version.parse(bstack1ll1l_opy_ (u"ࠧ࠴࠰࠷࠲࠵࠭ᵳ")):
        return False
    if bstack111lllll1_opy_() >= version.parse(bstack1ll1l_opy_ (u"ࠨ࠶࠱࠵࠳࠻ࠧᵴ")):
        return True
    if bstack1ll1l_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩᵵ") in config and config[bstack1ll1l_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪᵶ")] is False:
        return False
    else:
        return True
def bstack1l111lll11_opy_(args_list, bstack111l1l111l1_opy_):
    index = -1
    for value in bstack111l1l111l1_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
def bstack111l1111l11_opy_(a, b):
  for k, v in b.items():
    if isinstance(v, dict) and k in a and isinstance(a[k], dict):
        bstack111l1111l11_opy_(a[k], v)
    else:
        a[k] = v
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1llll1l1_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1llll1l1_opy_ = bstack1llll1l1_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack1ll1l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᵷ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack1ll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᵸ"), exception=exception)
    def bstack11111l11l1_opy_(self):
        if self.result != bstack1ll1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᵹ"):
            return None
        if isinstance(self.exception_type, str) and bstack1ll1l_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥᵺ") in self.exception_type:
            return bstack1ll1l_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠤᵻ")
        return bstack1ll1l_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥᵼ")
    def bstack111l11lllll_opy_(self):
        if self.result != bstack1ll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᵽ"):
            return None
        if self.bstack1llll1l1_opy_:
            return self.bstack1llll1l1_opy_
        return bstack111l1lll111_opy_(self.exception)
def bstack111l1lll111_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack111l11l111l_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1l1l1l1l_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1lll1ll11l_opy_(config, logger):
    try:
        import playwright
        bstack1111ll11l1l_opy_ = playwright.__file__
        bstack111l1ll1ll1_opy_ = os.path.split(bstack1111ll11l1l_opy_)
        bstack111ll1111l1_opy_ = bstack111l1ll1ll1_opy_[0] + bstack1ll1l_opy_ (u"ࠫ࠴ࡪࡲࡪࡸࡨࡶ࠴ࡶࡡࡤ࡭ࡤ࡫ࡪ࠵࡬ࡪࡤ࠲ࡧࡱ࡯࠯ࡤ࡮࡬࠲࡯ࡹࠧᵾ")
        os.environ[bstack1ll1l_opy_ (u"ࠬࡍࡌࡐࡄࡄࡐࡤࡇࡇࡆࡐࡗࡣࡍ࡚ࡔࡑࡡࡓࡖࡔ࡞࡙ࠨᵿ")] = bstack1l111l11l_opy_(config)
        with open(bstack111ll1111l1_opy_, bstack1ll1l_opy_ (u"࠭ࡲࠨᶀ")) as f:
            file_content = f.read()
            bstack111l1lll1l1_opy_ = bstack1ll1l_opy_ (u"ࠧࡨ࡮ࡲࡦࡦࡲ࠭ࡢࡩࡨࡲࡹ࠭ᶁ")
            bstack111l1l1l1l1_opy_ = file_content.find(bstack111l1lll1l1_opy_)
            if bstack111l1l1l1l1_opy_ == -1:
              process = subprocess.Popen(bstack1ll1l_opy_ (u"ࠣࡰࡳࡱࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡧ࡭ࡱࡥࡥࡱ࠳ࡡࡨࡧࡱࡸࠧᶂ"), shell=True, cwd=bstack111l1ll1ll1_opy_[0])
              process.wait()
              bstack111l11l11ll_opy_ = bstack1ll1l_opy_ (u"ࠩࠥࡹࡸ࡫ࠠࡴࡶࡵ࡭ࡨࡺࠢ࠼ࠩᶃ")
              bstack1111lllll11_opy_ = bstack1ll1l_opy_ (u"ࠥࠦࠧࠦ࡜ࠣࡷࡶࡩࠥࡹࡴࡳ࡫ࡦࡸࡡࠨ࠻ࠡࡥࡲࡲࡸࡺࠠࡼࠢࡥࡳࡴࡺࡳࡵࡴࡤࡴࠥࢃࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࠫ࡬ࡲ࡯ࡣࡣ࡯࠱ࡦ࡭ࡥ࡯ࡶࠪ࠭ࡀࠦࡩࡧࠢࠫࡴࡷࡵࡣࡦࡵࡶ࠲ࡪࡴࡶ࠯ࡉࡏࡓࡇࡇࡌࡠࡃࡊࡉࡓ࡚࡟ࡉࡖࡗࡔࡤࡖࡒࡐ࡚࡜࠭ࠥࡨ࡯ࡰࡶࡶࡸࡷࡧࡰࠩࠫ࠾ࠤࠧࠨࠢᶄ")
              bstack1111lll1lll_opy_ = file_content.replace(bstack111l11l11ll_opy_, bstack1111lllll11_opy_)
              with open(bstack111ll1111l1_opy_, bstack1ll1l_opy_ (u"ࠫࡼ࠭ᶅ")) as f:
                f.write(bstack1111lll1lll_opy_)
    except Exception as e:
        logger.error(bstack11ll11l1l1_opy_.format(str(e)))
def bstack11ll1l1ll1_opy_():
  try:
    bstack111l1l1ll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll1l_opy_ (u"ࠬࡵࡰࡵ࡫ࡰࡥࡱࡥࡨࡶࡤࡢࡹࡷࡲ࠮࡫ࡵࡲࡲࠬᶆ"))
    bstack1111llllll1_opy_ = []
    if os.path.exists(bstack111l1l1ll1l_opy_):
      with open(bstack111l1l1ll1l_opy_) as f:
        bstack1111llllll1_opy_ = json.load(f)
      os.remove(bstack111l1l1ll1l_opy_)
    return bstack1111llllll1_opy_
  except:
    pass
  return []
def bstack11111lllll_opy_(bstack1l11ll1l1_opy_):
  try:
    bstack1111llllll1_opy_ = []
    bstack111l1l1ll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll1l_opy_ (u"࠭࡯ࡱࡶ࡬ࡱࡦࡲ࡟ࡩࡷࡥࡣࡺࡸ࡬࠯࡬ࡶࡳࡳ࠭ᶇ"))
    if os.path.exists(bstack111l1l1ll1l_opy_):
      with open(bstack111l1l1ll1l_opy_) as f:
        bstack1111llllll1_opy_ = json.load(f)
    bstack1111llllll1_opy_.append(bstack1l11ll1l1_opy_)
    with open(bstack111l1l1ll1l_opy_, bstack1ll1l_opy_ (u"ࠧࡸࠩᶈ")) as f:
        json.dump(bstack1111llllll1_opy_, f)
  except:
    pass
def bstack111llll1l_opy_(logger, bstack1111l1lllll_opy_ = False):
  try:
    test_name = os.environ.get(bstack1ll1l_opy_ (u"ࠨࡒ࡜ࡘࡊ࡙ࡔࡠࡖࡈࡗ࡙ࡥࡎࡂࡏࡈࠫᶉ"), bstack1ll1l_opy_ (u"ࠩࠪᶊ"))
    if test_name == bstack1ll1l_opy_ (u"ࠪࠫᶋ"):
        test_name = threading.current_thread().__dict__.get(bstack1ll1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡆࡩࡪ࡟ࡵࡧࡶࡸࡤࡴࡡ࡮ࡧࠪᶌ"), bstack1ll1l_opy_ (u"ࠬ࠭ᶍ"))
    bstack1111ll1ll11_opy_ = bstack1ll1l_opy_ (u"࠭ࠬࠡࠩᶎ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack1111l1lllll_opy_:
        bstack111l1lll1_opy_ = os.environ.get(bstack1ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧᶏ"), bstack1ll1l_opy_ (u"ࠨ࠲ࠪᶐ"))
        bstack1111ll1lll_opy_ = {bstack1ll1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᶑ"): test_name, bstack1ll1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᶒ"): bstack1111ll1ll11_opy_, bstack1ll1l_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪᶓ"): bstack111l1lll1_opy_}
        bstack1111l1ll1l1_opy_ = []
        bstack111l11llll1_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡶࡰࡱࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫᶔ"))
        if os.path.exists(bstack111l11llll1_opy_):
            with open(bstack111l11llll1_opy_) as f:
                bstack1111l1ll1l1_opy_ = json.load(f)
        bstack1111l1ll1l1_opy_.append(bstack1111ll1lll_opy_)
        with open(bstack111l11llll1_opy_, bstack1ll1l_opy_ (u"࠭ࡷࠨᶕ")) as f:
            json.dump(bstack1111l1ll1l1_opy_, f)
    else:
        bstack1111ll1lll_opy_ = {bstack1ll1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᶖ"): test_name, bstack1ll1l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᶗ"): bstack1111ll1ll11_opy_, bstack1ll1l_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨᶘ"): str(multiprocessing.current_process().name)}
        if bstack1ll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺࠧᶙ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack1111ll1lll_opy_)
  except Exception as e:
      logger.warn(bstack1ll1l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡲࡶࡪࠦࡰࡺࡶࡨࡷࡹࠦࡦࡶࡰࡱࡩࡱࠦࡤࡢࡶࡤ࠾ࠥࢁࡽࠣᶚ").format(e))
def bstack1lll11l1l_opy_(error_message, test_name, index, logger):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1ll1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧ࡯ࡳࡨࡱࠠ࡯ࡱࡷࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠬࠡࡷࡶ࡭ࡳ࡭ࠠࡣࡣࡶ࡭ࡨࠦࡦࡪ࡮ࡨࠤࡴࡶࡥࡳࡣࡷ࡭ࡴࡴࡳࠨᶛ"))
    try:
      bstack111l11111l1_opy_ = []
      bstack1111ll1lll_opy_ = {bstack1ll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᶜ"): test_name, bstack1ll1l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᶝ"): error_message, bstack1ll1l_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧᶞ"): index}
      bstack111l111lll1_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪᶟ"))
      if os.path.exists(bstack111l111lll1_opy_):
          with open(bstack111l111lll1_opy_) as f:
              bstack111l11111l1_opy_ = json.load(f)
      bstack111l11111l1_opy_.append(bstack1111ll1lll_opy_)
      with open(bstack111l111lll1_opy_, bstack1ll1l_opy_ (u"ࠪࡻࠬᶠ")) as f:
          json.dump(bstack111l11111l1_opy_, f)
    except Exception as e:
      logger.warn(bstack1ll1l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡲࡶࡪࠦࡲࡰࡤࡲࡸࠥ࡬ࡵ࡯ࡰࡨࡰࠥࡪࡡࡵࡣ࠽ࠤࢀࢃࠢᶡ").format(e))
    return
  bstack111l11111l1_opy_ = []
  bstack1111ll1lll_opy_ = {bstack1ll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᶢ"): test_name, bstack1ll1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬᶣ"): error_message, bstack1ll1l_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭ᶤ"): index}
  bstack111l111lll1_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll1l_opy_ (u"ࠨࡴࡲࡦࡴࡺ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩᶥ"))
  lock_file = bstack111l111lll1_opy_ + bstack1ll1l_opy_ (u"ࠩ࠱ࡰࡴࡩ࡫ࠨᶦ")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack111l111lll1_opy_):
          with open(bstack111l111lll1_opy_, bstack1ll1l_opy_ (u"ࠪࡶࠬᶧ")) as f:
              content = f.read().strip()
              if content:
                  bstack111l11111l1_opy_ = json.load(open(bstack111l111lll1_opy_))
      bstack111l11111l1_opy_.append(bstack1111ll1lll_opy_)
      with open(bstack111l111lll1_opy_, bstack1ll1l_opy_ (u"ࠫࡼ࠭ᶨ")) as f:
          json.dump(bstack111l11111l1_opy_, f)
  except Exception as e:
    logger.warn(bstack1ll1l_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡳࡷ࡫ࠠࡳࡱࡥࡳࡹࠦࡦࡶࡰࡱࡩࡱࠦࡤࡢࡶࡤࠤࡼ࡯ࡴࡩࠢࡩ࡭ࡱ࡫ࠠ࡭ࡱࡦ࡯࡮ࡴࡧ࠻ࠢࡾࢁࠧᶩ").format(e))
def bstack11l1ll11ll_opy_(bstack1lll1l1111_opy_, name, logger):
  try:
    bstack1111ll1lll_opy_ = {bstack1ll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᶪ"): name, bstack1ll1l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᶫ"): bstack1lll1l1111_opy_, bstack1ll1l_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧᶬ"): str(threading.current_thread()._name)}
    return bstack1111ll1lll_opy_
  except Exception as e:
    logger.warn(bstack1ll1l_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡧ࡫ࡨࡢࡸࡨࠤ࡫ࡻ࡮࡯ࡧ࡯ࠤࡩࡧࡴࡢ࠼ࠣࡿࢂࠨᶭ").format(e))
  return
def bstack1111l1l111l_opy_():
    return platform.system() == bstack1ll1l_opy_ (u"࡛ࠪ࡮ࡴࡤࡰࡹࡶࠫᶮ")
def bstack1l1lll1ll_opy_(bstack111l1l1111l_opy_, config, logger):
    bstack1111ll1llll_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack111l1l1111l_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack1ll1l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫࡯ࡸࡪࡸࠠࡤࡱࡱࡪ࡮࡭ࠠ࡬ࡧࡼࡷࠥࡨࡹࠡࡴࡨ࡫ࡪࡾࠠ࡮ࡣࡷࡧ࡭ࡀࠠࡼࡿࠥᶯ").format(e))
    return bstack1111ll1llll_opy_
def bstack11l1ll1l111_opy_(bstack111l1111l1l_opy_, bstack111l1ll1l1l_opy_):
    bstack1111ll11l11_opy_ = version.parse(bstack111l1111l1l_opy_)
    bstack111l1l1lll1_opy_ = version.parse(bstack111l1ll1l1l_opy_)
    if bstack1111ll11l11_opy_ > bstack111l1l1lll1_opy_:
        return 1
    elif bstack1111ll11l11_opy_ < bstack111l1l1lll1_opy_:
        return -1
    else:
        return 0
def bstack1ll1111l_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack111l11lll1l_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack1111lll1111_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack1l1lll1l1l_opy_(options, framework, config, bstack11ll1ll11l_opy_={}):
    if options is None:
        return
    if getattr(options, bstack1ll1l_opy_ (u"ࠬ࡭ࡥࡵࠩᶰ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack1llll1ll11_opy_ = caps.get(bstack1ll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᶱ"))
    bstack1111ll11lll_opy_ = True
    bstack1ll11l11ll_opy_ = os.environ[bstack1ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬᶲ")]
    bstack1l1111l1ll1_opy_ = config.get(bstack1ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᶳ"), False)
    if bstack1l1111l1ll1_opy_:
        bstack1l1l1l11111_opy_ = config.get(bstack1ll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩᶴ"), {})
        bstack1l1l1l11111_opy_[bstack1ll1l_opy_ (u"ࠪࡥࡺࡺࡨࡕࡱ࡮ࡩࡳ࠭ᶵ")] = os.getenv(bstack1ll1l_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩᶶ"))
        bstack1111lll11ll_opy_ = json.loads(os.getenv(bstack1ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭ᶷ"), bstack1ll1l_opy_ (u"࠭ࡻࡾࠩᶸ"))).get(bstack1ll1l_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᶹ"))
    if bstack111l1ll1lll_opy_(caps.get(bstack1ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡶࡵࡨ࡛࠸ࡉࠧᶺ"))) or bstack111l1ll1lll_opy_(caps.get(bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡷࡶࡩࡤࡽ࠳ࡤࠩᶻ"))):
        bstack1111ll11lll_opy_ = False
    if bstack1l1ll1ll1l_opy_({bstack1ll1l_opy_ (u"ࠥࡹࡸ࡫ࡗ࠴ࡅࠥᶼ"): bstack1111ll11lll_opy_}):
        bstack1llll1ll11_opy_ = bstack1llll1ll11_opy_ or {}
        bstack1llll1ll11_opy_[bstack1ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ᶽ")] = bstack1111lll1111_opy_(framework)
        bstack1llll1ll11_opy_[bstack1ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᶾ")] = bstack1lll1llll1l_opy_()
        bstack1llll1ll11_opy_[bstack1ll1l_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩᶿ")] = bstack1ll11l11ll_opy_
        bstack1llll1ll11_opy_[bstack1ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩ᷀")] = bstack11ll1ll11l_opy_
        if bstack1l1111l1ll1_opy_:
            bstack1llll1ll11_opy_[bstack1ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ᷁")] = bstack1l1111l1ll1_opy_
            bstack1llll1ll11_opy_[bstack1ll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴ᷂ࠩ")] = bstack1l1l1l11111_opy_
            bstack1llll1ll11_opy_[bstack1ll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ᷃")][bstack1ll1l_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ᷄")] = bstack1111lll11ll_opy_
        if getattr(options, bstack1ll1l_opy_ (u"ࠬࡹࡥࡵࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸࡾ࠭᷅"), None):
            options.set_capability(bstack1ll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ᷆"), bstack1llll1ll11_opy_)
        else:
            options[bstack1ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ᷇")] = bstack1llll1ll11_opy_
    else:
        if getattr(options, bstack1ll1l_opy_ (u"ࠨࡵࡨࡸࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡺࠩ᷈"), None):
            options.set_capability(bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪ᷉"), bstack1111lll1111_opy_(framework))
            options.set_capability(bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱ᷊ࠫ"), bstack1lll1llll1l_opy_())
            options.set_capability(bstack1ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭᷋"), bstack1ll11l11ll_opy_)
            options.set_capability(bstack1ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭᷌"), bstack11ll1ll11l_opy_)
            if bstack1l1111l1ll1_opy_:
                options.set_capability(bstack1ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ᷍"), bstack1l1111l1ll1_opy_)
                options.set_capability(bstack1ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ᷎࠭"), bstack1l1l1l11111_opy_)
                options.set_capability(bstack1ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹ࠮ࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ᷏"), bstack1111lll11ll_opy_)
        else:
            options[bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍ᷐ࠪ")] = bstack1111lll1111_opy_(framework)
            options[bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ᷑")] = bstack1lll1llll1l_opy_()
            options[bstack1ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭᷒")] = bstack1ll11l11ll_opy_
            options[bstack1ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ᷓ")] = bstack11ll1ll11l_opy_
            if bstack1l1111l1ll1_opy_:
                options[bstack1ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᷔ")] = bstack1l1111l1ll1_opy_
                options[bstack1ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ᷕ")] = bstack1l1l1l11111_opy_
                options[bstack1ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᷖ")][bstack1ll1l_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᷗ")] = bstack1111lll11ll_opy_
    return options
def bstack111l1l11ll1_opy_(ws_endpoint, framework):
    bstack11ll1ll11l_opy_ = bstack111111ll_opy_.get_property(bstack1ll1l_opy_ (u"ࠥࡔࡑࡇ࡙ࡘࡔࡌࡋࡍ࡚࡟ࡑࡔࡒࡈ࡚ࡉࡔࡠࡏࡄࡔࠧᷘ"))
    if ws_endpoint and len(ws_endpoint.split(bstack1ll1l_opy_ (u"ࠫࡨࡧࡰࡴ࠿ࠪᷙ"))) > 1:
        ws_url = ws_endpoint.split(bstack1ll1l_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫᷚ"))[0]
        if bstack1ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩᷛ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack1111l1ll11l_opy_ = json.loads(urllib.parse.unquote(ws_endpoint.split(bstack1ll1l_opy_ (u"ࠧࡤࡣࡳࡷࡂ࠭ᷜ"))[1]))
            bstack1111l1ll11l_opy_ = bstack1111l1ll11l_opy_ or {}
            bstack1ll11l11ll_opy_ = os.environ[bstack1ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ᷝ")]
            bstack1111l1ll11l_opy_[bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪᷞ")] = str(framework) + str(__version__)
            bstack1111l1ll11l_opy_[bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᷟ")] = bstack1lll1llll1l_opy_()
            bstack1111l1ll11l_opy_[bstack1ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ᷠ")] = bstack1ll11l11ll_opy_
            bstack1111l1ll11l_opy_[bstack1ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ᷡ")] = bstack11ll1ll11l_opy_
            ws_endpoint = ws_endpoint.split(bstack1ll1l_opy_ (u"࠭ࡣࡢࡲࡶࡁࠬᷢ"))[0] + bstack1ll1l_opy_ (u"ࠧࡤࡣࡳࡷࡂ࠭ᷣ") + urllib.parse.quote(json.dumps(bstack1111l1ll11l_opy_))
    return ws_endpoint
def bstack111lll111l_opy_():
    global bstack111lll11l_opy_
    from playwright._impl._browser_type import BrowserType
    bstack111lll11l_opy_ = BrowserType.connect
    return bstack111lll11l_opy_
def bstack11ll11l11l_opy_(framework_name):
    global bstack1l1llllll_opy_
    bstack1l1llllll_opy_ = framework_name
    return framework_name
def bstack1l1llll1l_opy_(self, *args, **kwargs):
    global bstack111lll11l_opy_
    try:
        global bstack1l1llllll_opy_
        if bstack1ll1l_opy_ (u"ࠨࡹࡶࡉࡳࡪࡰࡰ࡫ࡱࡸࠬᷤ") in kwargs:
            kwargs[bstack1ll1l_opy_ (u"ࠩࡺࡷࡊࡴࡤࡱࡱ࡬ࡲࡹ࠭ᷥ")] = bstack111l1l11ll1_opy_(
                kwargs.get(bstack1ll1l_opy_ (u"ࠪࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺࠧᷦ"), None),
                bstack1l1llllll_opy_
            )
    except Exception as e:
        logger.error(bstack1ll1l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡫࡮ࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫࡙ࠥࡄࡌࠢࡦࡥࡵࡹ࠺ࠡࡽࢀࠦᷧ").format(str(e)))
    return bstack111lll11l_opy_(self, *args, **kwargs)
def bstack111l1111ll1_opy_(bstack1111l1l11ll_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack111l1l1ll_opy_(bstack1111l1l11ll_opy_, bstack1ll1l_opy_ (u"ࠧࠨᷨ"))
        if proxies and proxies.get(bstack1ll1l_opy_ (u"ࠨࡨࡵࡶࡳࡷࠧᷩ")):
            parsed_url = urlparse(proxies.get(bstack1ll1l_opy_ (u"ࠢࡩࡶࡷࡴࡸࠨᷪ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack1ll1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡈࡰࡵࡷࠫᷫ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack1ll1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡱࡵࡸࠬᷬ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack1ll1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡗࡶࡩࡷ࠭ᷭ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack1ll1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡥࡸࡹࠧᷮ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack1l1l1ll111_opy_(bstack1111l1l11ll_opy_):
    bstack111l11ll111_opy_ = {
        bstack11l1l1111l1_opy_[bstack111l1lll11l_opy_]: bstack1111l1l11ll_opy_[bstack111l1lll11l_opy_]
        for bstack111l1lll11l_opy_ in bstack1111l1l11ll_opy_
        if bstack111l1lll11l_opy_ in bstack11l1l1111l1_opy_
    }
    bstack111l11ll111_opy_[bstack1ll1l_opy_ (u"ࠧࡶࡲࡰࡺࡼࡗࡪࡺࡴࡪࡰࡪࡷࠧᷯ")] = bstack111l1111ll1_opy_(bstack1111l1l11ll_opy_, bstack111111ll_opy_.get_property(bstack1ll1l_opy_ (u"ࠨࡰࡳࡱࡻࡽࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸࠨᷰ")))
    bstack1111llll1ll_opy_ = [element.lower() for element in bstack11l1l111111_opy_]
    bstack1111l1l1l1l_opy_(bstack111l11ll111_opy_, bstack1111llll1ll_opy_)
    return bstack111l11ll111_opy_
def bstack1111l1l1l1l_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack1ll1l_opy_ (u"ࠢࠫࠬ࠭࠮ࠧᷱ")
    for value in d.values():
        if isinstance(value, dict):
            bstack1111l1l1l1l_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack1111l1l1l1l_opy_(item, keys)
def bstack1ll1l11ll11_opy_():
    bstack111l111ll1l_opy_ = [os.environ.get(bstack1ll1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡋࡏࡉࡘࡥࡄࡊࡔࠥᷲ")), os.path.join(os.path.expanduser(bstack1ll1l_opy_ (u"ࠤࢁࠦᷳ")), bstack1ll1l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᷴ")), os.path.join(bstack1ll1l_opy_ (u"ࠫ࠴ࡺ࡭ࡱࠩ᷵"), bstack1ll1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬ᷶"))]
    for path in bstack111l111ll1l_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack1ll1l_opy_ (u"ࠨࡆࡪ࡮ࡨࠤࠬࠨ᷷") + str(path) + bstack1ll1l_opy_ (u"ࠢࠨࠢࡨࡼ࡮ࡹࡴࡴ࠰᷸ࠥ"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack1ll1l_opy_ (u"ࠣࡉ࡬ࡺ࡮ࡴࡧࠡࡲࡨࡶࡲ࡯ࡳࡴ࡫ࡲࡲࡸࠦࡦࡰࡴ᷹ࠣࠫࠧ") + str(path) + bstack1ll1l_opy_ (u"ࠤ᷺ࠪࠦ"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack1ll1l_opy_ (u"ࠥࡊ࡮ࡲࡥࠡࠩࠥ᷻") + str(path) + bstack1ll1l_opy_ (u"ࠦࠬࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡩࡣࡶࠤࡹ࡮ࡥࠡࡴࡨࡵࡺ࡯ࡲࡦࡦࠣࡴࡪࡸ࡭ࡪࡵࡶ࡭ࡴࡴࡳ࠯ࠤ᷼"))
            else:
                logger.debug(bstack1ll1l_opy_ (u"ࠧࡉࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡧ࡫࡯ࡩ᷽ࠥ࠭ࠢ") + str(path) + bstack1ll1l_opy_ (u"ࠨࠧࠡࡹ࡬ࡸ࡭ࠦࡷࡳ࡫ࡷࡩࠥࡶࡥࡳ࡯࡬ࡷࡸ࡯࡯࡯࠰ࠥ᷾"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack1ll1l_opy_ (u"ࠢࡐࡲࡨࡶࡦࡺࡩࡰࡰࠣࡷࡺࡩࡣࡦࡧࡧࡩࡩࠦࡦࡰࡴ᷿ࠣࠫࠧ") + str(path) + bstack1ll1l_opy_ (u"ࠣࠩ࠱ࠦḀ"))
            return path
        except Exception as e:
            logger.debug(bstack1ll1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࠢࡸࡴࠥ࡬ࡩ࡭ࡧࠣࠫࢀࡶࡡࡵࡪࢀࠫ࠿ࠦࠢḁ") + str(e) + bstack1ll1l_opy_ (u"ࠥࠦḂ"))
    logger.debug(bstack1ll1l_opy_ (u"ࠦࡆࡲ࡬ࠡࡲࡤࡸ࡭ࡹࠠࡧࡣ࡬ࡰࡪࡪ࠮ࠣḃ"))
    return None
@measure(event_name=EVENTS.bstack11l1l11ll11_opy_, stage=STAGE.bstack11lll11ll_opy_)
def bstack1l1ll1111l1_opy_(binary_path, bstack1l11llll111_opy_, bs_config):
    logger.debug(bstack1ll1l_opy_ (u"ࠧࡉࡵࡳࡴࡨࡲࡹࠦࡃࡍࡋࠣࡔࡦࡺࡨࠡࡨࡲࡹࡳࡪ࠺ࠡࡽࢀࠦḄ").format(binary_path))
    bstack111l1l1ll11_opy_ = bstack1ll1l_opy_ (u"࠭ࠧḅ")
    bstack1111lll1ll1_opy_ = {
        bstack1ll1l_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬḆ"): __version__,
        bstack1ll1l_opy_ (u"ࠣࡱࡶࠦḇ"): platform.system(),
        bstack1ll1l_opy_ (u"ࠤࡲࡷࡤࡧࡲࡤࡪࠥḈ"): platform.machine(),
        bstack1ll1l_opy_ (u"ࠥࡧࡱ࡯࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣḉ"): bstack1ll1l_opy_ (u"ࠫ࠵࠭Ḋ"),
        bstack1ll1l_opy_ (u"ࠧࡹࡤ࡬ࡡ࡯ࡥࡳ࡭ࡵࡢࡩࡨࠦḋ"): bstack1ll1l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭Ḍ")
    }
    bstack111l1l1l11l_opy_(bstack1111lll1ll1_opy_)
    try:
        if binary_path:
            bstack1111lll1ll1_opy_[bstack1ll1l_opy_ (u"ࠧࡤ࡮࡬ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬḍ")] = subprocess.check_output([binary_path, bstack1ll1l_opy_ (u"ࠣࡸࡨࡶࡸ࡯࡯࡯ࠤḎ")]).strip().decode(bstack1ll1l_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨḏ"))
        response = requests.request(
            bstack1ll1l_opy_ (u"ࠪࡋࡊ࡚ࠧḐ"),
            url=bstack1ll1ll11ll_opy_(bstack11l1l1l111l_opy_),
            headers=None,
            auth=(bs_config[bstack1ll1l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ḑ")], bs_config[bstack1ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨḒ")]),
            json=None,
            params=bstack1111lll1ll1_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack1ll1l_opy_ (u"࠭ࡵࡳ࡮ࠪḓ") in data.keys() and bstack1ll1l_opy_ (u"ࠧࡶࡲࡧࡥࡹ࡫ࡤࡠࡥ࡯࡭ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭Ḕ") in data.keys():
            logger.debug(bstack1ll1l_opy_ (u"ࠣࡐࡨࡩࡩࠦࡴࡰࠢࡸࡴࡩࡧࡴࡦࠢࡥ࡭ࡳࡧࡲࡺ࠮ࠣࡧࡺࡸࡲࡦࡰࡷࠤࡧ࡯࡮ࡢࡴࡼࠤࡻ࡫ࡲࡴ࡫ࡲࡲ࠿ࠦࡻࡾࠤḕ").format(bstack1111lll1ll1_opy_[bstack1ll1l_opy_ (u"ࠩࡦࡰ࡮ࡥࡶࡦࡴࡶ࡭ࡴࡴࠧḖ")]))
            if bstack1ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡘࡖࡑ࠭ḗ") in os.environ:
                logger.debug(bstack1ll1l_opy_ (u"ࠦࡘࡱࡩࡱࡲ࡬ࡲ࡬ࠦࡢࡪࡰࡤࡶࡾࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡣࡶࠤࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆࡎࡔࡁࡓ࡛ࡢ࡙ࡗࡒࠠࡪࡵࠣࡷࡪࡺࠢḘ"))
                data[bstack1ll1l_opy_ (u"ࠬࡻࡲ࡭ࠩḙ")] = os.environ[bstack1ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡉࡏࡃࡕ࡝ࡤ࡛ࡒࡍࠩḚ")]
            bstack111l11l1l1l_opy_ = bstack111ll111111_opy_(data[bstack1ll1l_opy_ (u"ࠧࡶࡴ࡯ࠫḛ")], bstack1l11llll111_opy_)
            bstack111l1l1ll11_opy_ = os.path.join(bstack1l11llll111_opy_, bstack111l11l1l1l_opy_)
            os.chmod(bstack111l1l1ll11_opy_, 0o777) # bstack111l111ll11_opy_ permission
            return bstack111l1l1ll11_opy_
    except Exception as e:
        logger.debug(bstack1ll1l_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡤࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡳ࡫ࡷࠡࡕࡇࡏࠥࢁࡽࠣḜ").format(e))
    return binary_path
def bstack111l1l1l11l_opy_(bstack1111lll1ll1_opy_):
    try:
        if bstack1ll1l_opy_ (u"ࠩ࡯࡭ࡳࡻࡸࠨḝ") not in bstack1111lll1ll1_opy_[bstack1ll1l_opy_ (u"ࠪࡳࡸ࠭Ḟ")].lower():
            return
        if os.path.exists(bstack1ll1l_opy_ (u"ࠦ࠴࡫ࡴࡤ࠱ࡲࡷ࠲ࡸࡥ࡭ࡧࡤࡷࡪࠨḟ")):
            with open(bstack1ll1l_opy_ (u"ࠧ࠵ࡥࡵࡥ࠲ࡳࡸ࠳ࡲࡦ࡮ࡨࡥࡸ࡫ࠢḠ"), bstack1ll1l_opy_ (u"ࠨࡲࠣḡ")) as f:
                bstack111l1llll1l_opy_ = {}
                for line in f:
                    if bstack1ll1l_opy_ (u"ࠢ࠾ࠤḢ") in line:
                        key, value = line.rstrip().split(bstack1ll1l_opy_ (u"ࠣ࠿ࠥḣ"), 1)
                        bstack111l1llll1l_opy_[key] = value.strip(bstack1ll1l_opy_ (u"ࠩࠥࡠࠬ࠭Ḥ"))
                bstack1111lll1ll1_opy_[bstack1ll1l_opy_ (u"ࠪࡨ࡮ࡹࡴࡳࡱࠪḥ")] = bstack111l1llll1l_opy_.get(bstack1ll1l_opy_ (u"ࠦࡎࡊࠢḦ"), bstack1ll1l_opy_ (u"ࠧࠨḧ"))
        elif os.path.exists(bstack1ll1l_opy_ (u"ࠨ࠯ࡦࡶࡦ࠳ࡦࡲࡰࡪࡰࡨ࠱ࡷ࡫࡬ࡦࡣࡶࡩࠧḨ")):
            bstack1111lll1ll1_opy_[bstack1ll1l_opy_ (u"ࠧࡥ࡫ࡶࡸࡷࡵࠧḩ")] = bstack1ll1l_opy_ (u"ࠨࡣ࡯ࡴ࡮ࡴࡥࠨḪ")
    except Exception as e:
        logger.debug(bstack1ll1l_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡭ࡥࡵࠢࡧ࡭ࡸࡺࡲࡰࠢࡲࡪࠥࡲࡩ࡯ࡷࡻࠦḫ") + e)
@measure(event_name=EVENTS.bstack11l1l11ll1l_opy_, stage=STAGE.bstack11lll11ll_opy_)
def bstack111ll111111_opy_(bstack111l1l11l1l_opy_, bstack1111lll1l11_opy_):
    logger.debug(bstack1ll1l_opy_ (u"ࠥࡈࡴࡽ࡮࡭ࡱࡤࡨ࡮ࡴࡧࠡࡕࡇࡏࠥࡨࡩ࡯ࡣࡵࡽࠥ࡬ࡲࡰ࡯࠽ࠤࠧḬ") + str(bstack111l1l11l1l_opy_) + bstack1ll1l_opy_ (u"ࠦࠧḭ"))
    zip_path = os.path.join(bstack1111lll1l11_opy_, bstack1ll1l_opy_ (u"ࠧࡪ࡯ࡸࡰ࡯ࡳࡦࡪࡥࡥࡡࡩ࡭ࡱ࡫࠮ࡻ࡫ࡳࠦḮ"))
    bstack111l11l1l1l_opy_ = bstack1ll1l_opy_ (u"࠭ࠧḯ")
    with requests.get(bstack111l1l11l1l_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack1ll1l_opy_ (u"ࠢࡸࡤࠥḰ")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack1ll1l_opy_ (u"ࠣࡈ࡬ࡰࡪࠦࡤࡰࡹࡱࡰࡴࡧࡤࡦࡦࠣࡷࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺ࠰ࠥḱ"))
    with zipfile.ZipFile(zip_path, bstack1ll1l_opy_ (u"ࠩࡵࠫḲ")) as zip_ref:
        bstack111l11l1111_opy_ = zip_ref.namelist()
        if len(bstack111l11l1111_opy_) > 0:
            bstack111l11l1l1l_opy_ = bstack111l11l1111_opy_[0] # bstack111l11111ll_opy_ bstack11l1l1l1l11_opy_ will be bstack11l111l1_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack1111lll1l11_opy_)
        logger.debug(bstack1ll1l_opy_ (u"ࠥࡊ࡮ࡲࡥࡴࠢࡶࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹࠡࡧࡻࡸࡷࡧࡣࡵࡧࡧࠤࡹࡵࠠࠨࠤḳ") + str(bstack1111lll1l11_opy_) + bstack1ll1l_opy_ (u"ࠦࠬࠨḴ"))
    os.remove(zip_path)
    return bstack111l11l1l1l_opy_
def get_cli_dir():
    bstack1111ll111ll_opy_ = bstack1ll1l11ll11_opy_()
    if bstack1111ll111ll_opy_:
        bstack1l11llll111_opy_ = os.path.join(bstack1111ll111ll_opy_, bstack1ll1l_opy_ (u"ࠧࡩ࡬ࡪࠤḵ"))
        if not os.path.exists(bstack1l11llll111_opy_):
            os.makedirs(bstack1l11llll111_opy_, mode=0o777, exist_ok=True)
        return bstack1l11llll111_opy_
    else:
        raise FileNotFoundError(bstack1ll1l_opy_ (u"ࠨࡎࡰࠢࡺࡶ࡮ࡺࡡࡣ࡮ࡨࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧࠣࡪࡴࡸࠠࡵࡪࡨࠤࡘࡊࡋࠡࡤ࡬ࡲࡦࡸࡹ࠯ࠤḶ"))
def bstack1l1l1ll11l1_opy_(bstack1l11llll111_opy_):
    bstack1ll1l_opy_ (u"ࠢࠣࠤࡊࡩࡹࠦࡴࡩࡧࠣࡴࡦࡺࡨࠡࡨࡲࡶࠥࡺࡨࡦࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡕࡇࡏࠥࡨࡩ࡯ࡣࡵࡽࠥ࡯࡮ࠡࡣࠣࡻࡷ࡯ࡴࡢࡤ࡯ࡩࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹ࠯ࠤࠥࠦḷ")
    bstack1111l1l1ll1_opy_ = [
        os.path.join(bstack1l11llll111_opy_, f)
        for f in os.listdir(bstack1l11llll111_opy_)
        if os.path.isfile(os.path.join(bstack1l11llll111_opy_, f)) and f.startswith(bstack1ll1l_opy_ (u"ࠣࡤ࡬ࡲࡦࡸࡹ࠮ࠤḸ"))
    ]
    if len(bstack1111l1l1ll1_opy_) > 0:
        return max(bstack1111l1l1ll1_opy_, key=os.path.getmtime) # get bstack1111l1l11l1_opy_ binary
    return bstack1ll1l_opy_ (u"ࠤࠥḹ")
def bstack1111llll11l_opy_():
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
def bstack1ll11l1l1_opy_(data, keys, default=None):
    bstack1ll1l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡗࡦ࡬ࡥ࡭ࡻࠣ࡫ࡪࡺࠠࡢࠢࡱࡩࡸࡺࡥࡥࠢࡹࡥࡱࡻࡥࠡࡨࡵࡳࡲࠦࡡࠡࡦ࡬ࡧࡹ࡯࡯࡯ࡣࡵࡽࠥࡵࡲࠡ࡮࡬ࡷࡹ࠴ࠊࠡࠢࠣࠤ࠿ࡶࡡࡳࡣࡰࠤࡩࡧࡴࡢ࠼ࠣࡘ࡭࡫ࠠࡥ࡫ࡦࡸ࡮ࡵ࡮ࡢࡴࡼࠤࡴࡸࠠ࡭࡫ࡶࡸࠥࡺ࡯ࠡࡶࡵࡥࡻ࡫ࡲࡴࡧ࠱ࠎࠥࠦࠠࠡ࠼ࡳࡥࡷࡧ࡭ࠡ࡭ࡨࡽࡸࡀࠠࡂࠢ࡯࡭ࡸࡺࠠࡰࡨࠣ࡯ࡪࡿࡳ࠰࡫ࡱࡨ࡮ࡩࡥࡴࠢࡵࡩࡵࡸࡥࡴࡧࡱࡸ࡮ࡴࡧࠡࡶ࡫ࡩࠥࡶࡡࡵࡪ࠱ࠎࠥࠦࠠࠡ࠼ࡳࡥࡷࡧ࡭ࠡࡦࡨࡪࡦࡻ࡬ࡵ࠼࡚ࠣࡦࡲࡵࡦࠢࡷࡳࠥࡸࡥࡵࡷࡵࡲࠥ࡯ࡦࠡࡶ࡫ࡩࠥࡶࡡࡵࡪࠣࡨࡴ࡫ࡳࠡࡰࡲࡸࠥ࡫ࡸࡪࡵࡷ࠲ࠏࠦࠠࠡࠢ࠽ࡶࡪࡺࡵࡳࡰ࠽ࠤ࡙࡮ࡥࠡࡸࡤࡰࡺ࡫ࠠࡢࡶࠣࡸ࡭࡫ࠠ࡯ࡧࡶࡸࡪࡪࠠࡱࡣࡷ࡬࠱ࠦ࡯ࡳࠢࡧࡩ࡫ࡧࡵ࡭ࡶࠣ࡭࡫ࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥ࠰ࠍࠤࠥࠦࠠࠣࠤࠥḺ")
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