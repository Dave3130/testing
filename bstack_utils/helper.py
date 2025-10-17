# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
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
from bstack_utils.constants import (bstack1ll1l1ll1_opy_, bstack1l111lll1_opy_, bstack1l1l1l1l1_opy_,
                                    bstack11l1l1l11ll_opy_, bstack11l1l1ll11l_opy_, bstack11l1l1ll111_opy_, bstack11l1l111lll_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack111l11lll_opy_, bstack111111ll1_opy_
from bstack_utils.proxy import bstack1llllll11l_opy_, bstack11111ll11l_opy_
from bstack_utils.constants import *
from bstack_utils import bstack1lll11ll11_opy_
from bstack_utils.bstack11l111l11l_opy_ import bstack11ll1l1l1_opy_
from browserstack_sdk._version import __version__
bstack111ll111_opy_ = Config.bstack111ll1ll_opy_()
logger = bstack1lll11ll11_opy_.get_logger(__name__, bstack1lll11ll11_opy_.bstack1l1l1ll11ll_opy_())
def bstack111l1ll1ll1_opy_(config):
    return config[bstack11l111_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩᮺ")]
def bstack111l1111l11_opy_(config):
    return config[bstack11l111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫᮻ")]
def bstack1l1111l1ll_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack1111ll1l1ll_opy_(obj):
    values = []
    bstack111l11111ll_opy_ = re.compile(bstack11l111_opy_ (u"ࡴࠥࡢࡈ࡛ࡓࡕࡑࡐࡣ࡙ࡇࡇࡠ࡞ࡧ࠯ࠩࠨᮼ"), re.I)
    for key in obj.keys():
        if bstack111l11111ll_opy_.match(key):
            values.append(obj[key])
    return values
def bstack111l1l1lll1_opy_(config):
    tags = []
    tags.extend(bstack1111ll1l1ll_opy_(os.environ))
    tags.extend(bstack1111ll1l1ll_opy_(config))
    return tags
def bstack1111l1l1ll1_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack111l1l1ll11_opy_(bstack111l1llll1l_opy_):
    if not bstack111l1llll1l_opy_:
        return bstack11l111_opy_ (u"ࠪࠫᮽ")
    return bstack11l111_opy_ (u"ࠦࢀࢃࠠࠩࡽࢀ࠭ࠧᮾ").format(bstack111l1llll1l_opy_.name, bstack111l1llll1l_opy_.email)
def bstack111l1ll1l1l_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack111l11lllll_opy_ = repo.common_dir
        info = {
            bstack11l111_opy_ (u"ࠧࡹࡨࡢࠤᮿ"): repo.head.commit.hexsha,
            bstack11l111_opy_ (u"ࠨࡳࡩࡱࡵࡸࡤࡹࡨࡢࠤᯀ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack11l111_opy_ (u"ࠢࡣࡴࡤࡲࡨ࡮ࠢᯁ"): repo.active_branch.name,
            bstack11l111_opy_ (u"ࠣࡶࡤ࡫ࠧᯂ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack11l111_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡶࡨࡶࠧᯃ"): bstack111l1l1ll11_opy_(repo.head.commit.committer),
            bstack11l111_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡷࡩࡷࡥࡤࡢࡶࡨࠦᯄ"): repo.head.commit.committed_datetime.isoformat(),
            bstack11l111_opy_ (u"ࠦࡦࡻࡴࡩࡱࡵࠦᯅ"): bstack111l1l1ll11_opy_(repo.head.commit.author),
            bstack11l111_opy_ (u"ࠧࡧࡵࡵࡪࡲࡶࡤࡪࡡࡵࡧࠥᯆ"): repo.head.commit.authored_datetime.isoformat(),
            bstack11l111_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡥ࡭ࡦࡵࡶࡥ࡬࡫ࠢᯇ"): repo.head.commit.message,
            bstack11l111_opy_ (u"ࠢࡳࡱࡲࡸࠧᯈ"): repo.git.rev_parse(bstack11l111_opy_ (u"ࠣ࠯࠰ࡷ࡭ࡵࡷ࠮ࡶࡲࡴࡱ࡫ࡶࡦ࡮ࠥᯉ")),
            bstack11l111_opy_ (u"ࠤࡦࡳࡲࡳ࡯࡯ࡡࡪ࡭ࡹࡥࡤࡪࡴࠥᯊ"): bstack111l11lllll_opy_,
            bstack11l111_opy_ (u"ࠥࡻࡴࡸ࡫ࡵࡴࡨࡩࡤ࡭ࡩࡵࡡࡧ࡭ࡷࠨᯋ"): subprocess.check_output([bstack11l111_opy_ (u"ࠦ࡬࡯ࡴࠣᯌ"), bstack11l111_opy_ (u"ࠧࡸࡥࡷ࠯ࡳࡥࡷࡹࡥࠣᯍ"), bstack11l111_opy_ (u"ࠨ࠭࠮ࡩ࡬ࡸ࠲ࡩ࡯࡮࡯ࡲࡲ࠲ࡪࡩࡳࠤᯎ")]).strip().decode(
                bstack11l111_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ᯏ")),
            bstack11l111_opy_ (u"ࠣ࡮ࡤࡷࡹࡥࡴࡢࡩࠥᯐ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack11l111_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡵࡢࡷ࡮ࡴࡣࡦࡡ࡯ࡥࡸࡺ࡟ࡵࡣࡪࠦᯑ"): repo.git.rev_list(
                bstack11l111_opy_ (u"ࠥࡿࢂ࠴࠮ࡼࡿࠥᯒ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack1111lll1111_opy_ = []
        for remote in remotes:
            bstack111l11l1ll1_opy_ = {
                bstack11l111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᯓ"): remote.name,
                bstack11l111_opy_ (u"ࠧࡻࡲ࡭ࠤᯔ"): remote.url,
            }
            bstack1111lll1111_opy_.append(bstack111l11l1ll1_opy_)
        bstack1111ll1ll11_opy_ = {
            bstack11l111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᯕ"): bstack11l111_opy_ (u"ࠢࡨ࡫ࡷࠦᯖ"),
            **info,
            bstack11l111_opy_ (u"ࠣࡴࡨࡱࡴࡺࡥࡴࠤᯗ"): bstack1111lll1111_opy_
        }
        bstack1111ll1ll11_opy_ = bstack111l1l111ll_opy_(bstack1111ll1ll11_opy_)
        return bstack1111ll1ll11_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack11l111_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡲࡴࡺࡲࡡࡵ࡫ࡱ࡫ࠥࡍࡩࡵࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠧᯘ").format(err))
        return {}
def bstack11ll1ll11ll_opy_(bstack1111l1l11ll_opy_=None):
    bstack11l111_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡋࡪࡺࠠࡨ࡫ࡷࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡳࡱࡧࡦ࡭࡫࡯ࡣࡢ࡮࡯ࡽࠥ࡬࡯ࡳ࡯ࡤࡸࡹ࡫ࡤࠡࡨࡲࡶࠥࡇࡉࠡࡵࡨࡰࡪࡩࡴࡪࡱࡱࠤࡺࡹࡥࠡࡥࡤࡷࡪࡹࠠࡧࡱࡵࠤࡪࡧࡣࡩࠢࡩࡳࡱࡪࡥࡳࠢ࡬ࡲࠥࡺࡨࡦࠢ࡯࡭ࡸࡺ࠮ࠋࠢࠣࠤࠥࡇࡲࡨࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥ࡬࡯࡭ࡦࡨࡶࡸࠦࠨ࡭࡫ࡶࡸ࠱ࠦ࡯ࡱࡶ࡬ࡳࡳࡧ࡬ࠪ࠼ࠣࡐ࡮ࡹࡴࠡࡱࡩࠤ࡫ࡵ࡬ࡥࡧࡵࠤࡵࡧࡴࡩࡵࠣࡸࡴࠦࡥࡹࡶࡵࡥࡨࡺࠠࡨ࡫ࡷࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡦࡳࡱࡰ࠲ࠥࡊࡥࡧࡣࡸࡰࡹࡹࠠࡵࡱࠣ࡟ࡴࡹ࠮ࡨࡧࡷࡧࡼࡪࠨࠪ࡟࠱ࠎࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡱ࡯ࡳࡵ࠼ࠣࡐ࡮ࡹࡴࠡࡱࡩࠤࡩ࡯ࡣࡵࡵ࠯ࠤࡪࡧࡣࡩࠢࡦࡳࡳࡺࡡࡪࡰ࡬ࡲ࡬ࠦࡧࡪࡶࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡤࠤ࡫ࡵ࡬ࡥࡧࡵ࠲ࠏࠦࠠࠡࠢࠥࠦࠧᯙ")
    if bstack1111l1l11ll_opy_ == None: # bstack1111l1l1111_opy_ for bstack11ll1ll111l_opy_-repo
        bstack1111l1l11ll_opy_ = [os.getcwd()]
    results = []
    for folder in bstack1111l1l11ll_opy_:
        try:
            repo = git.Repo(folder, search_parent_directories=True)
            result = {
                bstack11l111_opy_ (u"ࠦࡵࡸࡉࡥࠤᯚ"): bstack11l111_opy_ (u"ࠧࠨᯛ"),
                bstack11l111_opy_ (u"ࠨࡦࡪ࡮ࡨࡷࡈ࡮ࡡ࡯ࡩࡨࡨࠧᯜ"): [],
                bstack11l111_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸࡳࠣᯝ"): [],
                bstack11l111_opy_ (u"ࠣࡲࡵࡈࡦࡺࡥࠣᯞ"): bstack11l111_opy_ (u"ࠤࠥᯟ"),
                bstack11l111_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡐࡩࡸࡹࡡࡨࡧࡶࠦᯠ"): [],
                bstack11l111_opy_ (u"ࠦࡵࡸࡔࡪࡶ࡯ࡩࠧᯡ"): bstack11l111_opy_ (u"ࠧࠨᯢ"),
                bstack11l111_opy_ (u"ࠨࡰࡳࡆࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳࠨᯣ"): bstack11l111_opy_ (u"ࠢࠣᯤ"),
                bstack11l111_opy_ (u"ࠣࡲࡵࡖࡦࡽࡄࡪࡨࡩࠦᯥ"): bstack11l111_opy_ (u"ࠤ᯦ࠥ")
            }
            bstack1111ll11l11_opy_ = repo.active_branch.name
            bstack1111l11llll_opy_ = repo.head.commit
            result[bstack11l111_opy_ (u"ࠥࡴࡷࡏࡤࠣᯧ")] = bstack1111l11llll_opy_.hexsha
            bstack111l1l111l1_opy_ = _1111llllll1_opy_(repo)
            logger.debug(bstack11l111_opy_ (u"ࠦࡇࡧࡳࡦࠢࡥࡶࡦࡴࡣࡩࠢࡩࡳࡷࠦࡣࡰ࡯ࡳࡥࡷ࡯ࡳࡰࡰ࠽ࠤࠧᯨ") + str(bstack111l1l111l1_opy_) + bstack11l111_opy_ (u"ࠧࠨᯩ"))
            if bstack111l1l111l1_opy_:
                try:
                    bstack1111l11lll1_opy_ = repo.git.diff(bstack11l111_opy_ (u"ࠨ࠭࠮ࡰࡤࡱࡪ࠳࡯࡯࡮ࡼࠦᯪ"), bstack1lll1lll1ll_opy_ (u"ࠢࡼࡤࡤࡷࡪࡥࡢࡳࡣࡱࡧ࡭ࢃ࠮࠯࠰ࡾࡧࡺࡸࡲࡦࡰࡷࡣࡧࡸࡡ࡯ࡥ࡫ࢁࠧᯫ")).split(bstack11l111_opy_ (u"ࠨ࡞ࡱࠫᯬ"))
                    logger.debug(bstack11l111_opy_ (u"ࠤࡆ࡬ࡦࡴࡧࡦࡦࠣࡪ࡮ࡲࡥࡴࠢࡥࡩࡹࡽࡥࡦࡰࠣࡿࡧࡧࡳࡦࡡࡥࡶࡦࡴࡣࡩࡿࠣࡥࡳࡪࠠࡼࡥࡸࡶࡷ࡫࡮ࡵࡡࡥࡶࡦࡴࡣࡩࡿ࠽ࠤࠧᯭ") + str(bstack1111l11lll1_opy_) + bstack11l111_opy_ (u"ࠥࠦᯮ"))
                    result[bstack11l111_opy_ (u"ࠦ࡫࡯࡬ࡦࡵࡆ࡬ࡦࡴࡧࡦࡦࠥᯯ")] = [f.strip() for f in bstack1111l11lll1_opy_ if f.strip()]
                    commits = list(repo.iter_commits(bstack1lll1lll1ll_opy_ (u"ࠧࢁࡢࡢࡵࡨࡣࡧࡸࡡ࡯ࡥ࡫ࢁ࠳࠴ࡻࡤࡷࡵࡶࡪࡴࡴࡠࡤࡵࡥࡳࡩࡨࡾࠤᯰ")))
                except Exception:
                    logger.debug(bstack11l111_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡪࡩࡹࠦࡣࡩࡣࡱ࡫ࡪࡪࠠࡧ࡫࡯ࡩࡸࠦࡦࡳࡱࡰࠤࡧࡸࡡ࡯ࡥ࡫ࠤࡨࡵ࡭ࡱࡣࡵ࡭ࡸࡵ࡮࠯ࠢࡉࡥࡱࡲࡩ࡯ࡩࠣࡦࡦࡩ࡫ࠡࡶࡲࠤࡷ࡫ࡣࡦࡰࡷࠤࡨࡵ࡭࡮࡫ࡷࡷ࠳ࠨᯱ"))
                    commits = list(repo.iter_commits(max_count=10))
                    if commits:
                        result[bstack11l111_opy_ (u"ࠢࡧ࡫࡯ࡩࡸࡉࡨࡢࡰࡪࡩࡩࠨ᯲")] = _1111l1lllll_opy_(commits[:5])
            else:
                commits = list(repo.iter_commits(max_count=10))
                if commits:
                    result[bstack11l111_opy_ (u"ࠣࡨ࡬ࡰࡪࡹࡃࡩࡣࡱ࡫ࡪࡪ᯳ࠢ")] = _1111l1lllll_opy_(commits[:5])
            bstack1111l1lll11_opy_ = set()
            bstack111ll1111l1_opy_ = []
            for commit in commits:
                logger.debug(bstack11l111_opy_ (u"ࠤࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡣࡰ࡯ࡰ࡭ࡹࡀࠠࠣ᯴") + str(commit.message) + bstack11l111_opy_ (u"ࠥࠦ᯵"))
                bstack111l1lll1l1_opy_ = commit.author.name if commit.author else bstack11l111_opy_ (u"࡚ࠦࡴ࡫࡯ࡱࡺࡲࠧ᯶")
                bstack1111l1lll11_opy_.add(bstack111l1lll1l1_opy_)
                bstack111ll1111l1_opy_.append({
                    bstack11l111_opy_ (u"ࠧࡳࡥࡴࡵࡤ࡫ࡪࠨ᯷"): commit.message.strip(),
                    bstack11l111_opy_ (u"ࠨࡵࡴࡧࡵࠦ᯸"): bstack111l1lll1l1_opy_
                })
            result[bstack11l111_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸࡳࠣ᯹")] = list(bstack1111l1lll11_opy_)
            result[bstack11l111_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡎࡧࡶࡷࡦ࡭ࡥࡴࠤ᯺")] = bstack111ll1111l1_opy_
            result[bstack11l111_opy_ (u"ࠤࡳࡶࡉࡧࡴࡦࠤ᯻")] = bstack1111l11llll_opy_.committed_datetime.strftime(bstack11l111_opy_ (u"ࠥࠩ࡞࠳ࠥ࡮࠯ࠨࡨࠧ᯼"))
            if (not result[bstack11l111_opy_ (u"ࠦࡵࡸࡔࡪࡶ࡯ࡩࠧ᯽")] or result[bstack11l111_opy_ (u"ࠧࡶࡲࡕ࡫ࡷࡰࡪࠨ᯾")].strip() == bstack11l111_opy_ (u"ࠨࠢ᯿")) and bstack1111l11llll_opy_.message:
                bstack111l1lll11l_opy_ = bstack1111l11llll_opy_.message.strip().splitlines()
                result[bstack11l111_opy_ (u"ࠢࡱࡴࡗ࡭ࡹࡲࡥࠣᰀ")] = bstack111l1lll11l_opy_[0] if bstack111l1lll11l_opy_ else bstack11l111_opy_ (u"ࠣࠤᰁ")
                if len(bstack111l1lll11l_opy_) > 2:
                    result[bstack11l111_opy_ (u"ࠤࡳࡶࡉ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠤᰂ")] = bstack11l111_opy_ (u"ࠪࡠࡳ࠭ᰃ").join(bstack111l1lll11l_opy_[2:]).strip()
            results.append(result)
        except Exception as err:
            logger.info(bstack11l111_opy_ (u"ࠦࡠࡐࡄ࡞ࠢࡆࡹࡷࡸࡥ࡯ࡶࠣࡔ࡜ࡊࠠࡑࡣࡷ࡬࠿ࠦࡻࡾࠤᰄ").format(os.getcwd()))
            logger.error(bstack11l111_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡵࡰࡶ࡮ࡤࡸ࡮ࡴࡧࠡࡉ࡬ࡸࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡧࡱࡵࠤࡆࡏࠠࡴࡧ࡯ࡩࡨࡺࡩࡰࡰࠣࠬ࡫ࡵ࡬ࡥࡧࡵ࠾ࠥࢁࡦࡰ࡮ࡧࡩࡷࢃࠩ࠻ࠢࠥᰅ") + str(str(err)) + bstack11l111_opy_ (u"ࠨࠢᰆ"))
    filtered_results = [
        result
        for result in results
        if _1111lll1ll1_opy_(result)
    ]
    return filtered_results
def _1111lll1ll1_opy_(result):
    bstack11l111_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡉࡧ࡯ࡴࡪࡸࠠࡵࡱࠣࡧ࡭࡫ࡣ࡬ࠢ࡬ࡪࠥࡧࠠࡨ࡫ࡷࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡲࡦࡵࡸࡰࡹࠦࡩࡴࠢࡹࡥࡱ࡯ࡤࠡࠪࡱࡳࡳ࠳ࡥ࡮ࡲࡷࡽࠥ࡬ࡩ࡭ࡧࡶࡇ࡭ࡧ࡮ࡨࡧࡧࠤࡦࡴࡤࠡࡣࡸࡸ࡭ࡵࡲࡴࠫ࠱ࠎࠥࠦࠠࠡࠤࠥࠦᰇ")
    return (
        isinstance(result.get(bstack11l111_opy_ (u"ࠣࡨ࡬ࡰࡪࡹࡃࡩࡣࡱ࡫ࡪࡪࠢᰈ"), None), list)
        and len(result[bstack11l111_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡳࡄࡪࡤࡲ࡬࡫ࡤࠣᰉ")]) > 0
        and isinstance(result.get(bstack11l111_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࡶࠦᰊ"), None), list)
        and len(result[bstack11l111_opy_ (u"ࠦࡦࡻࡴࡩࡱࡵࡷࠧᰋ")]) > 0
    )
def _1111llllll1_opy_(repo):
    bstack11l111_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤ࡚ࠥࡲࡺࠢࡷࡳࠥࡪࡥࡵࡧࡵࡱ࡮ࡴࡥࠡࡶ࡫ࡩࠥࡨࡡࡴࡧࠣࡦࡷࡧ࡮ࡤࡪࠣࡪࡴࡸࠠࡵࡪࡨࠤ࡬࡯ࡶࡦࡰࠣࡶࡪࡶ࡯ࠡࡹ࡬ࡸ࡭ࡵࡵࡵࠢ࡫ࡥࡷࡪࡣࡰࡦࡨࡨࠥࡴࡡ࡮ࡧࡶࠤࡦࡴࡤࠡࡹࡲࡶࡰࠦࡷࡪࡶ࡫ࠤࡦࡲ࡬ࠡࡘࡆࡗࠥࡶࡲࡰࡸ࡬ࡨࡪࡸࡳ࠯ࠌࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹࠠࡵࡪࡨࠤࡩ࡫ࡦࡢࡷ࡯ࡸࠥࡨࡲࡢࡰࡦ࡬ࠥ࡯ࡦࠡࡲࡲࡷࡸ࡯ࡢ࡭ࡧ࠯ࠤࡪࡲࡳࡦࠢࡑࡳࡳ࡫࠮ࠋࠢࠣࠤࠥࠨࠢࠣᰌ")
    try:
        try:
            origin = repo.remotes.origin
            bstack1111ll11l1l_opy_ = origin.refs[bstack11l111_opy_ (u"࠭ࡈࡆࡃࡇࠫᰍ")]
            target = bstack1111ll11l1l_opy_.reference.name
            if target.startswith(bstack11l111_opy_ (u"ࠧࡰࡴ࡬࡫࡮ࡴ࠯ࠨᰎ")):
                return target
        except Exception:
            pass
        if repo.remotes and repo.remotes.origin.refs:
            for ref in repo.remotes.origin.refs:
                if ref.name.startswith(bstack11l111_opy_ (u"ࠨࡱࡵ࡭࡬࡯࡮࠰ࠩᰏ")):
                    return ref.name
        if repo.heads:
            return repo.heads[0].name
    except Exception:
        pass
    return None
def _1111l1lllll_opy_(commits):
    bstack11l111_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡊࡩࡹࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡤࡪࡤࡲ࡬࡫ࡤࠡࡨ࡬ࡰࡪࡹࠠࡧࡴࡲࡱࠥࡧࠠ࡭࡫ࡶࡸࠥࡵࡦࠡࡥࡲࡱࡲ࡯ࡴࡴ࠰ࠍࠤࠥࠦࠠࠣࠤࠥᰐ")
    bstack1111l11lll1_opy_ = set()
    try:
        for commit in commits:
            if commit.parents:
                for parent in commit.parents:
                    diff = commit.diff(parent)
                    for bstack1111l1l1l11_opy_ in diff:
                        if bstack1111l1l1l11_opy_.a_path:
                            bstack1111l11lll1_opy_.add(bstack1111l1l1l11_opy_.a_path)
                        if bstack1111l1l1l11_opy_.b_path:
                            bstack1111l11lll1_opy_.add(bstack1111l1l1l11_opy_.b_path)
    except Exception:
        pass
    return list(bstack1111l11lll1_opy_)
def bstack111l1l111ll_opy_(bstack1111ll1ll11_opy_):
    bstack111l111llll_opy_ = bstack111l11l111l_opy_(bstack1111ll1ll11_opy_)
    if bstack111l111llll_opy_ and bstack111l111llll_opy_ > bstack11l1l1l11ll_opy_:
        bstack1111ll1111l_opy_ = bstack111l111llll_opy_ - bstack11l1l1l11ll_opy_
        bstack111l1lll111_opy_ = bstack111l1llll11_opy_(bstack1111ll1ll11_opy_[bstack11l111_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡢࡱࡪࡹࡳࡢࡩࡨࠦᰑ")], bstack1111ll1111l_opy_)
        bstack1111ll1ll11_opy_[bstack11l111_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡣࡲ࡫ࡳࡴࡣࡪࡩࠧᰒ")] = bstack111l1lll111_opy_
        logger.info(bstack11l111_opy_ (u"࡚ࠧࡨࡦࠢࡦࡳࡲࡳࡩࡵࠢ࡫ࡥࡸࠦࡢࡦࡧࡱࠤࡹࡸࡵ࡯ࡥࡤࡸࡪࡪ࠮ࠡࡕ࡬ࡾࡪࠦ࡯ࡧࠢࡦࡳࡲࡳࡩࡵࠢࡤࡪࡹ࡫ࡲࠡࡶࡵࡹࡳࡩࡡࡵ࡫ࡲࡲࠥ࡯ࡳࠡࡽࢀࠤࡐࡈࠢᰓ")
                    .format(bstack111l11l111l_opy_(bstack1111ll1ll11_opy_) / 1024))
    return bstack1111ll1ll11_opy_
def bstack111l11l111l_opy_(json_data):
    try:
        if json_data:
            bstack111l11l11l1_opy_ = json.dumps(json_data)
            bstack1111lll1lll_opy_ = sys.getsizeof(bstack111l11l11l1_opy_)
            return bstack1111lll1lll_opy_
    except Exception as e:
        logger.debug(bstack11l111_opy_ (u"ࠨࡓࡰ࡯ࡨࡸ࡭࡯࡮ࡨࠢࡺࡩࡳࡺࠠࡸࡴࡲࡲ࡬ࠦࡷࡩ࡫࡯ࡩࠥࡩࡡ࡭ࡥࡸࡰࡦࡺࡩ࡯ࡩࠣࡷ࡮ࢀࡥࠡࡱࡩࠤࡏ࡙ࡏࡏࠢࡲࡦ࡯࡫ࡣࡵ࠼ࠣࡿࢂࠨᰔ").format(e))
    return -1
def bstack111l1llll11_opy_(field, bstack111l111ll11_opy_):
    try:
        bstack1111l1l1l1l_opy_ = len(bytes(bstack11l1l1ll11l_opy_, bstack11l111_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ᰕ")))
        bstack111l11l1l1l_opy_ = bytes(field, bstack11l111_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧᰖ"))
        bstack111l1111lll_opy_ = len(bstack111l11l1l1l_opy_)
        bstack111l1ll1111_opy_ = ceil(bstack111l1111lll_opy_ - bstack111l111ll11_opy_ - bstack1111l1l1l1l_opy_)
        if bstack111l1ll1111_opy_ > 0:
            bstack1111l1llll1_opy_ = bstack111l11l1l1l_opy_[:bstack111l1ll1111_opy_].decode(bstack11l111_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᰗ"), errors=bstack11l111_opy_ (u"ࠪ࡭࡬ࡴ࡯ࡳࡧࠪᰘ")) + bstack11l1l1ll11l_opy_
            return bstack1111l1llll1_opy_
    except Exception as e:
        logger.debug(bstack11l111_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡷࡶࡺࡴࡣࡢࡶ࡬ࡲ࡬ࠦࡦࡪࡧ࡯ࡨ࠱ࠦ࡮ࡰࡶ࡫࡭ࡳ࡭ࠠࡸࡣࡶࠤࡹࡸࡵ࡯ࡥࡤࡸࡪࡪࠠࡩࡧࡵࡩ࠿ࠦࡻࡾࠤᰙ").format(e))
    return field
def bstack1l11l111l_opy_():
    env = os.environ
    if (bstack11l111_opy_ (u"ࠧࡐࡅࡏࡍࡌࡒࡘࡥࡕࡓࡎࠥᰚ") in env and len(env[bstack11l111_opy_ (u"ࠨࡊࡆࡐࡎࡍࡓ࡙࡟ࡖࡔࡏࠦᰛ")]) > 0) or (
            bstack11l111_opy_ (u"ࠢࡋࡇࡑࡏࡎࡔࡓࡠࡊࡒࡑࡊࠨᰜ") in env and len(env[bstack11l111_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡋࡓࡒࡋࠢᰝ")]) > 0):
        return {
            bstack11l111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᰞ"): bstack11l111_opy_ (u"ࠥࡎࡪࡴ࡫ࡪࡰࡶࠦᰟ"),
            bstack11l111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᰠ"): env.get(bstack11l111_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᰡ")),
            bstack11l111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᰢ"): env.get(bstack11l111_opy_ (u"ࠢࡋࡑࡅࡣࡓࡇࡍࡆࠤᰣ")),
            bstack11l111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᰤ"): env.get(bstack11l111_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣᰥ"))
        }
    if env.get(bstack11l111_opy_ (u"ࠥࡇࡎࠨᰦ")) == bstack11l111_opy_ (u"ࠦࡹࡸࡵࡦࠤᰧ") and bstack11lll1lll_opy_(env.get(bstack11l111_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡈࡏࠢᰨ"))):
        return {
            bstack11l111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᰩ"): bstack11l111_opy_ (u"ࠢࡄ࡫ࡵࡧࡱ࡫ࡃࡊࠤᰪ"),
            bstack11l111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᰫ"): env.get(bstack11l111_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧᰬ")),
            bstack11l111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᰭ"): env.get(bstack11l111_opy_ (u"ࠦࡈࡏࡒࡄࡎࡈࡣࡏࡕࡂࠣᰮ")),
            bstack11l111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᰯ"): env.get(bstack11l111_opy_ (u"ࠨࡃࡊࡔࡆࡐࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࠤᰰ"))
        }
    if env.get(bstack11l111_opy_ (u"ࠢࡄࡋࠥᰱ")) == bstack11l111_opy_ (u"ࠣࡶࡵࡹࡪࠨᰲ") and bstack11lll1lll_opy_(env.get(bstack11l111_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࠤᰳ"))):
        return {
            bstack11l111_opy_ (u"ࠥࡲࡦࡳࡥࠣᰴ"): bstack11l111_opy_ (u"࡙ࠦࡸࡡࡷ࡫ࡶࠤࡈࡏࠢᰵ"),
            bstack11l111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᰶ"): env.get(bstack11l111_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࡥࡂࡖࡋࡏࡈࡤ࡝ࡅࡃࡡࡘࡖࡑࠨ᰷")),
            bstack11l111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᰸"): env.get(bstack11l111_opy_ (u"ࠣࡖࡕࡅ࡛ࡏࡓࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥ᰹")),
            bstack11l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᰺"): env.get(bstack11l111_opy_ (u"ࠥࡘࡗࡇࡖࡊࡕࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤ᰻"))
        }
    if env.get(bstack11l111_opy_ (u"ࠦࡈࡏࠢ᰼")) == bstack11l111_opy_ (u"ࠧࡺࡲࡶࡧࠥ᰽") and env.get(bstack11l111_opy_ (u"ࠨࡃࡊࡡࡑࡅࡒࡋࠢ᰾")) == bstack11l111_opy_ (u"ࠢࡤࡱࡧࡩࡸ࡮ࡩࡱࠤ᰿"):
        return {
            bstack11l111_opy_ (u"ࠣࡰࡤࡱࡪࠨ᱀"): bstack11l111_opy_ (u"ࠤࡆࡳࡩ࡫ࡳࡩ࡫ࡳࠦ᱁"),
            bstack11l111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᱂"): None,
            bstack11l111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᱃"): None,
            bstack11l111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ᱄"): None
        }
    if env.get(bstack11l111_opy_ (u"ࠨࡂࡊࡖࡅ࡙ࡈࡑࡅࡕࡡࡅࡖࡆࡔࡃࡉࠤ᱅")) and env.get(bstack11l111_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡇࡔࡓࡍࡊࡖࠥ᱆")):
        return {
            bstack11l111_opy_ (u"ࠣࡰࡤࡱࡪࠨ᱇"): bstack11l111_opy_ (u"ࠤࡅ࡭ࡹࡨࡵࡤ࡭ࡨࡸࠧ᱈"),
            bstack11l111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᱉"): env.get(bstack11l111_opy_ (u"ࠦࡇࡏࡔࡃࡗࡆࡏࡊ࡚࡟ࡈࡋࡗࡣࡍ࡚ࡔࡑࡡࡒࡖࡎࡍࡉࡏࠤ᱊")),
            bstack11l111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ᱋"): None,
            bstack11l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ᱌"): env.get(bstack11l111_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᱍ"))
        }
    if env.get(bstack11l111_opy_ (u"ࠣࡅࡌࠦᱎ")) == bstack11l111_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᱏ") and bstack11lll1lll_opy_(env.get(bstack11l111_opy_ (u"ࠥࡈࡗࡕࡎࡆࠤ᱐"))):
        return {
            bstack11l111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᱑"): bstack11l111_opy_ (u"ࠧࡊࡲࡰࡰࡨࠦ᱒"),
            bstack11l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᱓"): env.get(bstack11l111_opy_ (u"ࠢࡅࡔࡒࡒࡊࡥࡂࡖࡋࡏࡈࡤࡒࡉࡏࡍࠥ᱔")),
            bstack11l111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᱕"): None,
            bstack11l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᱖"): env.get(bstack11l111_opy_ (u"ࠥࡈࡗࡕࡎࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣ᱗"))
        }
    if env.get(bstack11l111_opy_ (u"ࠦࡈࡏࠢ᱘")) == bstack11l111_opy_ (u"ࠧࡺࡲࡶࡧࠥ᱙") and bstack11lll1lll_opy_(env.get(bstack11l111_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࠤᱚ"))):
        return {
            bstack11l111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᱛ"): bstack11l111_opy_ (u"ࠣࡕࡨࡱࡦࡶࡨࡰࡴࡨࠦᱜ"),
            bstack11l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᱝ"): env.get(bstack11l111_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࡥࡏࡓࡉࡄࡒࡎࡠࡁࡕࡋࡒࡒࡤ࡛ࡒࡍࠤᱞ")),
            bstack11l111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᱟ"): env.get(bstack11l111_opy_ (u"࡙ࠧࡅࡎࡃࡓࡌࡔࡘࡅࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᱠ")),
            bstack11l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᱡ"): env.get(bstack11l111_opy_ (u"ࠢࡔࡇࡐࡅࡕࡎࡏࡓࡇࡢࡎࡔࡈ࡟ࡊࡆࠥᱢ"))
        }
    if env.get(bstack11l111_opy_ (u"ࠣࡅࡌࠦᱣ")) == bstack11l111_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᱤ") and bstack11lll1lll_opy_(env.get(bstack11l111_opy_ (u"ࠥࡋࡎ࡚ࡌࡂࡄࡢࡇࡎࠨᱥ"))):
        return {
            bstack11l111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᱦ"): bstack11l111_opy_ (u"ࠧࡍࡩࡵࡎࡤࡦࠧᱧ"),
            bstack11l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᱨ"): env.get(bstack11l111_opy_ (u"ࠢࡄࡋࡢࡎࡔࡈ࡟ࡖࡔࡏࠦᱩ")),
            bstack11l111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᱪ"): env.get(bstack11l111_opy_ (u"ࠤࡆࡍࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢᱫ")),
            bstack11l111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᱬ"): env.get(bstack11l111_opy_ (u"ࠦࡈࡏ࡟ࡋࡑࡅࡣࡎࡊࠢᱭ"))
        }
    if env.get(bstack11l111_opy_ (u"ࠧࡉࡉࠣᱮ")) == bstack11l111_opy_ (u"ࠨࡴࡳࡷࡨࠦᱯ") and bstack11lll1lll_opy_(env.get(bstack11l111_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࠥᱰ"))):
        return {
            bstack11l111_opy_ (u"ࠣࡰࡤࡱࡪࠨᱱ"): bstack11l111_opy_ (u"ࠤࡅࡹ࡮ࡲࡤ࡬࡫ࡷࡩࠧᱲ"),
            bstack11l111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᱳ"): env.get(bstack11l111_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᱴ")),
            bstack11l111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᱵ"): env.get(bstack11l111_opy_ (u"ࠨࡂࡖࡋࡏࡈࡐࡏࡔࡆࡡࡏࡅࡇࡋࡌࠣᱶ")) or env.get(bstack11l111_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡔࡎࡖࡅࡍࡋࡑࡉࡤࡔࡁࡎࡇࠥᱷ")),
            bstack11l111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᱸ"): env.get(bstack11l111_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᱹ"))
        }
    if bstack11lll1lll_opy_(env.get(bstack11l111_opy_ (u"ࠥࡘࡋࡥࡂࡖࡋࡏࡈࠧᱺ"))):
        return {
            bstack11l111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᱻ"): bstack11l111_opy_ (u"ࠧ࡜ࡩࡴࡷࡤࡰ࡙ࠥࡴࡶࡦ࡬ࡳ࡚ࠥࡥࡢ࡯ࠣࡗࡪࡸࡶࡪࡥࡨࡷࠧᱼ"),
            bstack11l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᱽ"): bstack11l111_opy_ (u"ࠢࡼࡿࡾࢁࠧ᱾").format(env.get(bstack11l111_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡌࡏࡖࡐࡇࡅ࡙ࡏࡏࡏࡕࡈࡖ࡛ࡋࡒࡖࡔࡌࠫ᱿")), env.get(bstack11l111_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡐࡓࡑࡍࡉࡈ࡚ࡉࡅࠩᲀ"))),
            bstack11l111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᲁ"): env.get(bstack11l111_opy_ (u"ࠦࡘ࡟ࡓࡕࡇࡐࡣࡉࡋࡆࡊࡐࡌࡘࡎࡕࡎࡊࡆࠥᲂ")),
            bstack11l111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᲃ"): env.get(bstack11l111_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡍࡉࠨᲄ"))
        }
    if bstack11lll1lll_opy_(env.get(bstack11l111_opy_ (u"ࠢࡂࡒࡓ࡚ࡊ࡟ࡏࡓࠤᲅ"))):
        return {
            bstack11l111_opy_ (u"ࠣࡰࡤࡱࡪࠨᲆ"): bstack11l111_opy_ (u"ࠤࡄࡴࡵࡼࡥࡺࡱࡵࠦᲇ"),
            bstack11l111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᲈ"): bstack11l111_opy_ (u"ࠦࢀࢃ࠯ࡱࡴࡲ࡮ࡪࡩࡴ࠰ࡽࢀ࠳ࢀࢃ࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿࠥᲉ").format(env.get(bstack11l111_opy_ (u"ࠬࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡖࡔࡏࠫᲊ")), env.get(bstack11l111_opy_ (u"࠭ࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡃࡆࡇࡔ࡛ࡎࡕࡡࡑࡅࡒࡋࠧ᲋")), env.get(bstack11l111_opy_ (u"ࠧࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡓࡖࡔࡐࡅࡄࡖࡢࡗࡑ࡛ࡇࠨ᲌")), env.get(bstack11l111_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬ᲍"))),
            bstack11l111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ᲎"): env.get(bstack11l111_opy_ (u"ࠥࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢ᲏")),
            bstack11l111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᲐ"): env.get(bstack11l111_opy_ (u"ࠧࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨᲑ"))
        }
    if env.get(bstack11l111_opy_ (u"ࠨࡁ࡛ࡗࡕࡉࡤࡎࡔࡕࡒࡢ࡙ࡘࡋࡒࡠࡃࡊࡉࡓ࡚ࠢᲒ")) and env.get(bstack11l111_opy_ (u"ࠢࡕࡈࡢࡆ࡚ࡏࡌࡅࠤᲓ")):
        return {
            bstack11l111_opy_ (u"ࠣࡰࡤࡱࡪࠨᲔ"): bstack11l111_opy_ (u"ࠤࡄࡾࡺࡸࡥࠡࡅࡌࠦᲕ"),
            bstack11l111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᲖ"): bstack11l111_opy_ (u"ࠦࢀࢃࡻࡾ࠱ࡢࡦࡺ࡯࡬ࡥ࠱ࡵࡩࡸࡻ࡬ࡵࡵࡂࡦࡺ࡯࡬ࡥࡋࡧࡁࢀࢃࠢᲗ").format(env.get(bstack11l111_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡉࡓ࡚ࡔࡄࡂࡖࡌࡓࡓ࡙ࡅࡓࡘࡈࡖ࡚ࡘࡉࠨᲘ")), env.get(bstack11l111_opy_ (u"࠭ࡓ࡚ࡕࡗࡉࡒࡥࡔࡆࡃࡐࡔࡗࡕࡊࡆࡅࡗࠫᲙ")), env.get(bstack11l111_opy_ (u"ࠧࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠧᲚ"))),
            bstack11l111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᲛ"): env.get(bstack11l111_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠤᲜ")),
            bstack11l111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᲝ"): env.get(bstack11l111_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡋࡇࠦᲞ"))
        }
    if any([env.get(bstack11l111_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᲟ")), env.get(bstack11l111_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡕࡉࡘࡕࡌࡗࡇࡇࡣࡘࡕࡕࡓࡅࡈࡣ࡛ࡋࡒࡔࡋࡒࡒࠧᲠ")), env.get(bstack11l111_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡗࡔ࡛ࡒࡄࡇࡢ࡚ࡊࡘࡓࡊࡑࡑࠦᲡ"))]):
        return {
            bstack11l111_opy_ (u"ࠣࡰࡤࡱࡪࠨᲢ"): bstack11l111_opy_ (u"ࠤࡄ࡛ࡘࠦࡃࡰࡦࡨࡆࡺ࡯࡬ࡥࠤᲣ"),
            bstack11l111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᲤ"): env.get(bstack11l111_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡑࡗࡅࡐࡎࡉ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᲥ")),
            bstack11l111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᲦ"): env.get(bstack11l111_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦᲧ")),
            bstack11l111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᲨ"): env.get(bstack11l111_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᲩ"))
        }
    if env.get(bstack11l111_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡥࡹ࡮ࡲࡤࡏࡷࡰࡦࡪࡸࠢᲪ")):
        return {
            bstack11l111_opy_ (u"ࠥࡲࡦࡳࡥࠣᲫ"): bstack11l111_opy_ (u"ࠦࡇࡧ࡭ࡣࡱࡲࠦᲬ"),
            bstack11l111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᲭ"): env.get(bstack11l111_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡢࡶ࡫࡯ࡨࡗ࡫ࡳࡶ࡮ࡷࡷ࡚ࡸ࡬ࠣᲮ")),
            bstack11l111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᲯ"): env.get(bstack11l111_opy_ (u"ࠣࡤࡤࡱࡧࡵ࡯ࡠࡵ࡫ࡳࡷࡺࡊࡰࡤࡑࡥࡲ࡫ࠢᲰ")),
            bstack11l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᲱ"): env.get(bstack11l111_opy_ (u"ࠥࡦࡦࡳࡢࡰࡱࡢࡦࡺ࡯࡬ࡥࡐࡸࡱࡧ࡫ࡲࠣᲲ"))
        }
    if env.get(bstack11l111_opy_ (u"ࠦ࡜ࡋࡒࡄࡍࡈࡖࠧᲳ")) or env.get(bstack11l111_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡍࡂࡋࡑࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡓࡕࡃࡕࡘࡊࡊࠢᲴ")):
        return {
            bstack11l111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᲵ"): bstack11l111_opy_ (u"ࠢࡘࡧࡵࡧࡰ࡫ࡲࠣᲶ"),
            bstack11l111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᲷ"): env.get(bstack11l111_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᲸ")),
            bstack11l111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᲹ"): bstack11l111_opy_ (u"ࠦࡒࡧࡩ࡯ࠢࡓ࡭ࡵ࡫࡬ࡪࡰࡨࠦᲺ") if env.get(bstack11l111_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡍࡂࡋࡑࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡓࡕࡃࡕࡘࡊࡊࠢ᲻")) else None,
            bstack11l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ᲼"): env.get(bstack11l111_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࡠࡉࡌࡘࡤࡉࡏࡎࡏࡌࡘࠧᲽ"))
        }
    if any([env.get(bstack11l111_opy_ (u"ࠣࡉࡆࡔࡤࡖࡒࡐࡌࡈࡇ࡙ࠨᲾ")), env.get(bstack11l111_opy_ (u"ࠤࡊࡇࡑࡕࡕࡅࡡࡓࡖࡔࡐࡅࡄࡖࠥᲿ")), env.get(bstack11l111_opy_ (u"ࠥࡋࡔࡕࡇࡍࡇࡢࡇࡑࡕࡕࡅࡡࡓࡖࡔࡐࡅࡄࡖࠥ᳀"))]):
        return {
            bstack11l111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᳁"): bstack11l111_opy_ (u"ࠧࡍ࡯ࡰࡩ࡯ࡩࠥࡉ࡬ࡰࡷࡧࠦ᳂"),
            bstack11l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᳃"): None,
            bstack11l111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᳄"): env.get(bstack11l111_opy_ (u"ࠣࡒࡕࡓࡏࡋࡃࡕࡡࡌࡈࠧ᳅")),
            bstack11l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᳆"): env.get(bstack11l111_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡌࡈࠧ᳇"))
        }
    if env.get(bstack11l111_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋࠢ᳈")):
        return {
            bstack11l111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᳉"): bstack11l111_opy_ (u"ࠨࡓࡩ࡫ࡳࡴࡦࡨ࡬ࡦࠤ᳊"),
            bstack11l111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ᳋"): env.get(bstack11l111_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢ᳌")),
            bstack11l111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ᳍"): bstack11l111_opy_ (u"ࠥࡎࡴࡨࠠࠤࡽࢀࠦ᳎").format(env.get(bstack11l111_opy_ (u"ࠫࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡋࡑࡅࡣࡎࡊࠧ᳏"))) if env.get(bstack11l111_opy_ (u"࡙ࠧࡈࡊࡒࡓࡅࡇࡒࡅࡠࡌࡒࡆࡤࡏࡄࠣ᳐")) else None,
            bstack11l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ᳑"): env.get(bstack11l111_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤ᳒"))
        }
    if bstack11lll1lll_opy_(env.get(bstack11l111_opy_ (u"ࠣࡐࡈࡘࡑࡏࡆ࡚ࠤ᳓"))):
        return {
            bstack11l111_opy_ (u"ࠤࡱࡥࡲ࡫᳔ࠢ"): bstack11l111_opy_ (u"ࠥࡒࡪࡺ࡬ࡪࡨࡼ᳕ࠦ"),
            bstack11l111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲ᳖ࠢ"): env.get(bstack11l111_opy_ (u"ࠧࡊࡅࡑࡎࡒ࡝ࡤ࡛ࡒࡍࠤ᳗")),
            bstack11l111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥ᳘ࠣ"): env.get(bstack11l111_opy_ (u"ࠢࡔࡋࡗࡉࡤࡔࡁࡎࡇ᳙ࠥ")),
            bstack11l111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ᳚"): env.get(bstack11l111_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡋࡇࠦ᳛"))
        }
    if bstack11lll1lll_opy_(env.get(bstack11l111_opy_ (u"ࠥࡋࡎ࡚ࡈࡖࡄࡢࡅࡈ࡚ࡉࡐࡐࡖ᳜ࠦ"))):
        return {
            bstack11l111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᳝"): bstack11l111_opy_ (u"ࠧࡍࡩࡵࡊࡸࡦࠥࡇࡣࡵ࡫ࡲࡲࡸࠨ᳞"),
            bstack11l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᳟"): bstack11l111_opy_ (u"ࠢࡼࡿ࠲ࡿࢂ࠵ࡡࡤࡶ࡬ࡳࡳࡹ࠯ࡳࡷࡱࡷ࠴ࢁࡽࠣ᳠").format(env.get(bstack11l111_opy_ (u"ࠨࡉࡌࡘࡍ࡛ࡂࡠࡕࡈࡖ࡛ࡋࡒࡠࡗࡕࡐࠬ᳡")), env.get(bstack11l111_opy_ (u"ࠩࡊࡍ࡙ࡎࡕࡃࡡࡕࡉࡕࡕࡓࡊࡖࡒࡖ࡞᳢࠭")), env.get(bstack11l111_opy_ (u"ࠪࡋࡎ࡚ࡈࡖࡄࡢࡖ࡚ࡔ࡟ࡊࡆ᳣ࠪ"))),
            bstack11l111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᳤"): env.get(bstack11l111_opy_ (u"ࠧࡍࡉࡕࡊࡘࡆࡤ࡝ࡏࡓࡍࡉࡐࡔ࡝᳥ࠢ")),
            bstack11l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶ᳦ࠧ"): env.get(bstack11l111_opy_ (u"ࠢࡈࡋࡗࡌ࡚ࡈ࡟ࡓࡗࡑࡣࡎࡊ᳧ࠢ"))
        }
    if env.get(bstack11l111_opy_ (u"ࠣࡅࡌ᳨ࠦ")) == bstack11l111_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᳩ") and env.get(bstack11l111_opy_ (u"࡚ࠥࡊࡘࡃࡆࡎࠥᳪ")) == bstack11l111_opy_ (u"ࠦ࠶ࠨᳫ"):
        return {
            bstack11l111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᳬ"): bstack11l111_opy_ (u"ࠨࡖࡦࡴࡦࡩࡱࠨ᳭"),
            bstack11l111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᳮ"): bstack11l111_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࡽࢀࠦᳯ").format(env.get(bstack11l111_opy_ (u"࡙ࠩࡉࡗࡉࡅࡍࡡࡘࡖࡑ࠭ᳰ"))),
            bstack11l111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᳱ"): None,
            bstack11l111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᳲ"): None,
        }
    if env.get(bstack11l111_opy_ (u"࡚ࠧࡅࡂࡏࡆࡍ࡙࡟࡟ࡗࡇࡕࡗࡎࡕࡎࠣᳳ")):
        return {
            bstack11l111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ᳴"): bstack11l111_opy_ (u"ࠢࡕࡧࡤࡱࡨ࡯ࡴࡺࠤᳵ"),
            bstack11l111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᳶ"): None,
            bstack11l111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ᳷"): env.get(bstack11l111_opy_ (u"ࠥࡘࡊࡇࡍࡄࡋࡗ࡝ࡤࡖࡒࡐࡌࡈࡇ࡙ࡥࡎࡂࡏࡈࠦ᳸")),
            bstack11l111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ᳹"): env.get(bstack11l111_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᳺ"))
        }
    if any([env.get(bstack11l111_opy_ (u"ࠨࡃࡐࡐࡆࡓ࡚ࡘࡓࡆࠤ᳻")), env.get(bstack11l111_opy_ (u"ࠢࡄࡑࡑࡇࡔ࡛ࡒࡔࡇࡢ࡙ࡗࡒࠢ᳼")), env.get(bstack11l111_opy_ (u"ࠣࡅࡒࡒࡈࡕࡕࡓࡕࡈࡣ࡚࡙ࡅࡓࡐࡄࡑࡊࠨ᳽")), env.get(bstack11l111_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࡤ࡚ࡅࡂࡏࠥ᳾"))]):
        return {
            bstack11l111_opy_ (u"ࠥࡲࡦࡳࡥࠣ᳿"): bstack11l111_opy_ (u"ࠦࡈࡵ࡮ࡤࡱࡸࡶࡸ࡫ࠢᴀ"),
            bstack11l111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᴁ"): None,
            bstack11l111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᴂ"): env.get(bstack11l111_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣᴃ")) or None,
            bstack11l111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᴄ"): env.get(bstack11l111_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡋࡇࠦᴅ"), 0)
        }
    if env.get(bstack11l111_opy_ (u"ࠥࡋࡔࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣᴆ")):
        return {
            bstack11l111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᴇ"): bstack11l111_opy_ (u"ࠧࡍ࡯ࡄࡆࠥᴈ"),
            bstack11l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᴉ"): None,
            bstack11l111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᴊ"): env.get(bstack11l111_opy_ (u"ࠣࡉࡒࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᴋ")),
            bstack11l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᴌ"): env.get(bstack11l111_opy_ (u"ࠥࡋࡔࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡅࡒ࡙ࡓ࡚ࡅࡓࠤᴍ"))
        }
    if env.get(bstack11l111_opy_ (u"ࠦࡈࡌ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤᴎ")):
        return {
            bstack11l111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᴏ"): bstack11l111_opy_ (u"ࠨࡃࡰࡦࡨࡊࡷ࡫ࡳࡩࠤᴐ"),
            bstack11l111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᴑ"): env.get(bstack11l111_opy_ (u"ࠣࡅࡉࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢᴒ")),
            bstack11l111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᴓ"): env.get(bstack11l111_opy_ (u"ࠥࡇࡋࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡐࡄࡑࡊࠨᴔ")),
            bstack11l111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᴕ"): env.get(bstack11l111_opy_ (u"ࠧࡉࡆࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᴖ"))
        }
    return {bstack11l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᴗ"): None}
def get_host_info():
    return {
        bstack11l111_opy_ (u"ࠢࡩࡱࡶࡸࡳࡧ࡭ࡦࠤᴘ"): platform.node(),
        bstack11l111_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠥᴙ"): platform.system(),
        bstack11l111_opy_ (u"ࠤࡷࡽࡵ࡫ࠢᴚ"): platform.machine(),
        bstack11l111_opy_ (u"ࠥࡺࡪࡸࡳࡪࡱࡱࠦᴛ"): platform.version(),
        bstack11l111_opy_ (u"ࠦࡦࡸࡣࡩࠤᴜ"): platform.architecture()[0]
    }
def bstack1llll11l11_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack111l1ll1lll_opy_():
    if bstack111ll111_opy_.get_property(bstack11l111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭ᴝ")):
        return bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᴞ")
    return bstack11l111_opy_ (u"ࠧࡶࡰ࡮ࡲࡴࡽ࡮ࡠࡩࡵ࡭ࡩ࠭ᴟ")
def bstack111l11lll1l_opy_(driver):
    info = {
        bstack11l111_opy_ (u"ࠨࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧᴠ"): driver.capabilities,
        bstack11l111_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩ࠭ᴡ"): driver.session_id,
        bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫᴢ"): driver.capabilities.get(bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩᴣ"), None),
        bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᴤ"): driver.capabilities.get(bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᴥ"), None),
        bstack11l111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩᴦ"): driver.capabilities.get(bstack11l111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠧᴧ"), None),
        bstack11l111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬᴨ"):driver.capabilities.get(bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬᴩ"), None),
    }
    if bstack111l1ll1lll_opy_() == bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᴪ"):
        if bstack11l1l1l11l_opy_():
            info[bstack11l111_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭ᴫ")] = bstack11l111_opy_ (u"࠭ࡡࡱࡲ࠰ࡥࡺࡺ࡯࡮ࡣࡷࡩࠬᴬ")
        elif driver.capabilities.get(bstack11l111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᴭ"), {}).get(bstack11l111_opy_ (u"ࠨࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩࠬᴮ"), False):
            info[bstack11l111_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࠪᴯ")] = bstack11l111_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧᴰ")
        else:
            info[bstack11l111_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࠬᴱ")] = bstack11l111_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧᴲ")
    return info
def bstack11l1l1l11l_opy_():
    if bstack111ll111_opy_.get_property(bstack11l111_opy_ (u"࠭ࡡࡱࡲࡢࡥࡺࡺ࡯࡮ࡣࡷࡩࠬᴳ")):
        return True
    if bstack11lll1lll_opy_(os.environ.get(bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨᴴ"), None)):
        return True
    return False
def bstack11ll11ll1l_opy_(bstack111ll111111_opy_, url, data, config):
    headers = config.get(bstack11l111_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩᴵ"), None)
    proxies = bstack1llllll11l_opy_(config, url)
    auth = config.get(bstack11l111_opy_ (u"ࠩࡤࡹࡹ࡮ࠧᴶ"), None)
    response = requests.request(
            bstack111ll111111_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack111ll1l11l_opy_(bstack1ll1ll111_opy_, size):
    bstack111ll1l111_opy_ = []
    while len(bstack1ll1ll111_opy_) > size:
        bstack1ll1ll111l_opy_ = bstack1ll1ll111_opy_[:size]
        bstack111ll1l111_opy_.append(bstack1ll1ll111l_opy_)
        bstack1ll1ll111_opy_ = bstack1ll1ll111_opy_[size:]
    bstack111ll1l111_opy_.append(bstack1ll1ll111_opy_)
    return bstack111ll1l111_opy_
def bstack1111l1l11l1_opy_(message, bstack1111l1l1lll_opy_=False):
    os.write(1, bytes(message, bstack11l111_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᴷ")))
    os.write(1, bytes(bstack11l111_opy_ (u"ࠫࡡࡴࠧᴸ"), bstack11l111_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫᴹ")))
    if bstack1111l1l1lll_opy_:
        with open(bstack11l111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࠳࡯࠲࠳ࡼ࠱ࠬᴺ") + os.environ[bstack11l111_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡌࡆ࡙ࡈࡆࡆࡢࡍࡉ࠭ᴻ")] + bstack11l111_opy_ (u"ࠨ࠰࡯ࡳ࡬࠭ᴼ"), bstack11l111_opy_ (u"ࠩࡤࠫᴽ")) as f:
            f.write(message + bstack11l111_opy_ (u"ࠪࡠࡳ࠭ᴾ"))
def bstack1lll11llll1_opy_():
    return os.environ[bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧᴿ")].lower() == bstack11l111_opy_ (u"ࠬࡺࡲࡶࡧࠪᵀ")
def bstack1llll111_opy_():
    return bstack1l11l111_opy_().replace(tzinfo=None).isoformat() + bstack11l111_opy_ (u"࡚࠭ࠨᵁ")
def bstack1111l1ll111_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack11l111_opy_ (u"࡛ࠧࠩᵂ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack11l111_opy_ (u"ࠨ࡜ࠪᵃ")))).total_seconds() * 1000
def bstack111l11l1l11_opy_(timestamp):
    return bstack111l1lllll1_opy_(timestamp).isoformat() + bstack11l111_opy_ (u"ࠩ࡝ࠫᵄ")
def bstack1111l1ll11l_opy_(bstack1111l1ll1l1_opy_):
    date_format = bstack11l111_opy_ (u"ࠪࠩ࡞ࠫ࡭ࠦࡦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗ࠳ࠫࡦࠨᵅ")
    bstack1111llll1ll_opy_ = datetime.datetime.strptime(bstack1111l1ll1l1_opy_, date_format)
    return bstack1111llll1ll_opy_.isoformat() + bstack11l111_opy_ (u"ࠫ࡟࠭ᵆ")
def bstack111l111l111_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack11l111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᵇ")
    else:
        return bstack11l111_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᵈ")
def bstack11lll1lll_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack11l111_opy_ (u"ࠧࡵࡴࡸࡩࠬᵉ")
def bstack111l111l1ll_opy_(val):
    return val.__str__().lower() == bstack11l111_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧᵊ")
def error_handler(bstack111l1l11lll_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack111l1l11lll_opy_ as e:
                print(bstack11l111_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࡿࢂࠦ࠭࠿ࠢࡾࢁ࠿ࠦࡻࡾࠤᵋ").format(func.__name__, bstack111l1l11lll_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack1111ll1l111_opy_(bstack111l1ll111l_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack111l1ll111l_opy_(cls, *args, **kwargs)
            except bstack111l1l11lll_opy_ as e:
                print(bstack11l111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࢀࢃࠠ࠮ࡀࠣࡿࢂࡀࠠࡼࡿࠥᵌ").format(bstack111l1ll111l_opy_.__name__, bstack111l1l11lll_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack1111ll1l111_opy_
    else:
        return decorator
def bstack1ll1l1l1ll_opy_(bstack1lllll11l_opy_):
    if os.getenv(bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧᵍ")) is not None:
        return bstack11lll1lll_opy_(os.getenv(bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨᵎ")))
    if bstack11l111_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᵏ") in bstack1lllll11l_opy_ and bstack111l111l1ll_opy_(bstack1lllll11l_opy_[bstack11l111_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᵐ")]):
        return False
    if bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᵑ") in bstack1lllll11l_opy_ and bstack111l111l1ll_opy_(bstack1lllll11l_opy_[bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᵒ")]):
        return False
    return True
def bstack11llll1l11_opy_():
    try:
        from pytest_bdd import reporting
        bstack111l1llllll_opy_ = os.environ.get(bstack11l111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡘࡗࡊࡘ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠥᵓ"), None)
        return bstack111l1llllll_opy_ is None or bstack111l1llllll_opy_ == bstack11l111_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠣᵔ")
    except Exception as e:
        return False
def bstack111l1111l1_opy_(hub_url, CONFIG):
    if bstack1l11l1l11l_opy_() <= version.parse(bstack11l111_opy_ (u"ࠬ࠹࠮࠲࠵࠱࠴ࠬᵕ")):
        if hub_url:
            return bstack11l111_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢᵖ") + hub_url + bstack11l111_opy_ (u"ࠢ࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠦᵗ")
        return bstack1l111lll1_opy_
    if hub_url:
        return bstack11l111_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥᵘ") + hub_url + bstack11l111_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥᵙ")
    return bstack1l1l1l1l1_opy_
def bstack1111lllll11_opy_():
    return isinstance(os.getenv(bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓ࡝࡙ࡋࡓࡕࡡࡓࡐ࡚ࡍࡉࡏࠩᵚ")), str)
def bstack1lllll1l1l_opy_(url):
    return urlparse(url).hostname
def bstack1111ll1l11_opy_(hostname):
    for bstack11l11111l_opy_ in bstack1ll1l1ll1_opy_:
        regex = re.compile(bstack11l11111l_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11ll111l1l1_opy_(bstack111l11ll1l1_opy_, file_name, logger):
    bstack11lllll11_opy_ = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠫࢃ࠭ᵛ")), bstack111l11ll1l1_opy_)
    try:
        if not os.path.exists(bstack11lllll11_opy_):
            os.makedirs(bstack11lllll11_opy_)
        file_path = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠬࢄࠧᵜ")), bstack111l11ll1l1_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack11l111_opy_ (u"࠭ࡷࠨᵝ")):
                pass
            with open(file_path, bstack11l111_opy_ (u"ࠢࡸ࠭ࠥᵞ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack111l11lll_opy_.format(str(e)))
def bstack11ll111llll_opy_(file_name, key, value, logger):
    file_path = bstack11ll111l1l1_opy_(bstack11l111_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᵟ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1ll11llll_opy_ = json.load(open(file_path, bstack11l111_opy_ (u"ࠩࡵࡦࠬᵠ")))
        else:
            bstack1ll11llll_opy_ = {}
        bstack1ll11llll_opy_[key] = value
        with open(file_path, bstack11l111_opy_ (u"ࠥࡻ࠰ࠨᵡ")) as outfile:
            json.dump(bstack1ll11llll_opy_, outfile)
def bstack11l11ll11_opy_(file_name, logger):
    file_path = bstack11ll111l1l1_opy_(bstack11l111_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᵢ"), file_name, logger)
    bstack1ll11llll_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack11l111_opy_ (u"ࠬࡸࠧᵣ")) as bstack11l1l111l_opy_:
            bstack1ll11llll_opy_ = json.load(bstack11l1l111l_opy_)
    return bstack1ll11llll_opy_
def bstack1l11ll111_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack11l111_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡦࡨࡰࡪࡺࡩ࡯ࡩࠣࡪ࡮ࡲࡥ࠻ࠢࠪᵤ") + file_path + bstack11l111_opy_ (u"ࠧࠡࠩᵥ") + str(e))
def bstack1l11l1l11l_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack11l111_opy_ (u"ࠣ࠾ࡑࡓ࡙࡙ࡅࡕࡀࠥᵦ")
def bstack1l11ll1ll1_opy_(config):
    if bstack11l111_opy_ (u"ࠩ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᵧ") in config:
        del (config[bstack11l111_opy_ (u"ࠪ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᵨ")])
        return False
    if bstack1l11l1l11l_opy_() < version.parse(bstack11l111_opy_ (u"ࠫ࠸࠴࠴࠯࠲ࠪᵩ")):
        return False
    if bstack1l11l1l11l_opy_() >= version.parse(bstack11l111_opy_ (u"ࠬ࠺࠮࠲࠰࠸ࠫᵪ")):
        return True
    if bstack11l111_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ᵫ") in config and config[bstack11l111_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧᵬ")] is False:
        return False
    else:
        return True
def bstack11l111lll_opy_(args_list, bstack1111ll111l1_opy_):
    index = -1
    for value in bstack1111ll111l1_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
def bstack1111lll1l1l_opy_(a, b):
  for k, v in b.items():
    if isinstance(v, dict) and k in a and isinstance(a[k], dict):
        bstack1111lll1l1l_opy_(a[k], v)
    else:
        a[k] = v
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1ll1l1l1_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1ll1l1l1_opy_ = bstack1ll1l1l1_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack11l111_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᵭ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack11l111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᵮ"), exception=exception)
    def bstack11111l1111_opy_(self):
        if self.result != bstack11l111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᵯ"):
            return None
        if isinstance(self.exception_type, str) and bstack11l111_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࠢᵰ") in self.exception_type:
            return bstack11l111_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࡆࡴࡵࡳࡷࠨᵱ")
        return bstack11l111_opy_ (u"ࠨࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠢᵲ")
    def bstack111l1ll11ll_opy_(self):
        if self.result != bstack11l111_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᵳ"):
            return None
        if self.bstack1ll1l1l1_opy_:
            return self.bstack1ll1l1l1_opy_
        return bstack1111llll111_opy_(self.exception)
def bstack1111llll111_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack111l1l11111_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1l11lll1_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack11llllll11_opy_(config, logger):
    try:
        import playwright
        bstack111l1l1llll_opy_ = playwright.__file__
        bstack1111ll111ll_opy_ = os.path.split(bstack111l1l1llll_opy_)
        bstack111l11ll111_opy_ = bstack1111ll111ll_opy_[0] + bstack11l111_opy_ (u"ࠨ࠱ࡧࡶ࡮ࡼࡥࡳ࠱ࡳࡥࡨࡱࡡࡨࡧ࠲ࡰ࡮ࡨ࠯ࡤ࡮࡬࠳ࡨࡲࡩ࠯࡬ࡶࠫᵴ")
        os.environ[bstack11l111_opy_ (u"ࠩࡊࡐࡔࡈࡁࡍࡡࡄࡋࡊࡔࡔࡠࡊࡗࡘࡕࡥࡐࡓࡑ࡛࡝ࠬᵵ")] = bstack11111ll11l_opy_(config)
        with open(bstack111l11ll111_opy_, bstack11l111_opy_ (u"ࠪࡶࠬᵶ")) as f:
            file_content = f.read()
            bstack1111ll11lll_opy_ = bstack11l111_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯࠱ࡦ࡭ࡥ࡯ࡶࠪᵷ")
            bstack1111ll1ll1l_opy_ = file_content.find(bstack1111ll11lll_opy_)
            if bstack1111ll1ll1l_opy_ == -1:
              process = subprocess.Popen(bstack11l111_opy_ (u"ࠧࡴࡰ࡮ࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣ࡫ࡱࡵࡢࡢ࡮࠰ࡥ࡬࡫࡮ࡵࠤᵸ"), shell=True, cwd=bstack1111ll111ll_opy_[0])
              process.wait()
              bstack111l11111l1_opy_ = bstack11l111_opy_ (u"࠭ࠢࡶࡵࡨࠤࡸࡺࡲࡪࡥࡷࠦࡀ࠭ᵹ")
              bstack111l1l1l1ll_opy_ = bstack11l111_opy_ (u"ࠢࠣࠤࠣࡠࠧࡻࡳࡦࠢࡶࡸࡷ࡯ࡣࡵ࡞ࠥ࠿ࠥࡩ࡯࡯ࡵࡷࠤࢀࠦࡢࡰࡱࡷࡷࡹࡸࡡࡱࠢࢀࠤࡂࠦࡲࡦࡳࡸ࡭ࡷ࡫ࠨࠨࡩ࡯ࡳࡧࡧ࡬࠮ࡣࡪࡩࡳࡺࠧࠪ࠽ࠣ࡭࡫ࠦࠨࡱࡴࡲࡧࡪࡹࡳ࠯ࡧࡱࡺ࠳ࡍࡌࡐࡄࡄࡐࡤࡇࡇࡆࡐࡗࡣࡍ࡚ࡔࡑࡡࡓࡖࡔ࡞࡙ࠪࠢࡥࡳࡴࡺࡳࡵࡴࡤࡴ࠭࠯࠻ࠡࠤࠥࠦᵺ")
              bstack111l11ll1ll_opy_ = file_content.replace(bstack111l11111l1_opy_, bstack111l1l1l1ll_opy_)
              with open(bstack111l11ll111_opy_, bstack11l111_opy_ (u"ࠨࡹࠪᵻ")) as f:
                f.write(bstack111l11ll1ll_opy_)
    except Exception as e:
        logger.error(bstack111111ll1_opy_.format(str(e)))
def bstack1l1l1llll1_opy_():
  try:
    bstack111l1l1l111_opy_ = os.path.join(tempfile.gettempdir(), bstack11l111_opy_ (u"ࠩࡲࡴࡹ࡯࡭ࡢ࡮ࡢ࡬ࡺࡨ࡟ࡶࡴ࡯࠲࡯ࡹ࡯࡯ࠩᵼ"))
    bstack111l1l1ll1l_opy_ = []
    if os.path.exists(bstack111l1l1l111_opy_):
      with open(bstack111l1l1l111_opy_) as f:
        bstack111l1l1ll1l_opy_ = json.load(f)
      os.remove(bstack111l1l1l111_opy_)
    return bstack111l1l1ll1l_opy_
  except:
    pass
  return []
def bstack11ll11lll1_opy_(bstack1l1lllll11_opy_):
  try:
    bstack111l1l1ll1l_opy_ = []
    bstack111l1l1l111_opy_ = os.path.join(tempfile.gettempdir(), bstack11l111_opy_ (u"ࠪࡳࡵࡺࡩ࡮ࡣ࡯ࡣ࡭ࡻࡢࡠࡷࡵࡰ࠳ࡰࡳࡰࡰࠪᵽ"))
    if os.path.exists(bstack111l1l1l111_opy_):
      with open(bstack111l1l1l111_opy_) as f:
        bstack111l1l1ll1l_opy_ = json.load(f)
    bstack111l1l1ll1l_opy_.append(bstack1l1lllll11_opy_)
    with open(bstack111l1l1l111_opy_, bstack11l111_opy_ (u"ࠫࡼ࠭ᵾ")) as f:
        json.dump(bstack111l1l1ll1l_opy_, f)
  except:
    pass
def bstack11l11l1l1_opy_(logger, bstack111l1l1111l_opy_ = False):
  try:
    test_name = os.environ.get(bstack11l111_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘࡤ࡚ࡅࡔࡖࡢࡒࡆࡓࡅࠨᵿ"), bstack11l111_opy_ (u"࠭ࠧᶀ"))
    if test_name == bstack11l111_opy_ (u"ࠧࠨᶁ"):
        test_name = threading.current_thread().__dict__.get(bstack11l111_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡃࡦࡧࡣࡹ࡫ࡳࡵࡡࡱࡥࡲ࡫ࠧᶂ"), bstack11l111_opy_ (u"ࠩࠪᶃ"))
    bstack1111lllllll_opy_ = bstack11l111_opy_ (u"ࠪ࠰ࠥ࠭ᶄ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack111l1l1111l_opy_:
        bstack1l1lll1l1l_opy_ = os.environ.get(bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫᶅ"), bstack11l111_opy_ (u"ࠬ࠶ࠧᶆ"))
        bstack11lll1llll_opy_ = {bstack11l111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᶇ"): test_name, bstack11l111_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᶈ"): bstack1111lllllll_opy_, bstack11l111_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧᶉ"): bstack1l1lll1l1l_opy_}
        bstack111l11llll1_opy_ = []
        bstack111l111lll1_opy_ = os.path.join(tempfile.gettempdir(), bstack11l111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡳࡴࡵࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨᶊ"))
        if os.path.exists(bstack111l111lll1_opy_):
            with open(bstack111l111lll1_opy_) as f:
                bstack111l11llll1_opy_ = json.load(f)
        bstack111l11llll1_opy_.append(bstack11lll1llll_opy_)
        with open(bstack111l111lll1_opy_, bstack11l111_opy_ (u"ࠪࡻࠬᶋ")) as f:
            json.dump(bstack111l11llll1_opy_, f)
    else:
        bstack11lll1llll_opy_ = {bstack11l111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᶌ"): test_name, bstack11l111_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᶍ"): bstack1111lllllll_opy_, bstack11l111_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬᶎ"): str(multiprocessing.current_process().name)}
        if bstack11l111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷࠫᶏ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack11lll1llll_opy_)
  except Exception as e:
      logger.warn(bstack11l111_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺ࡯ࡳࡧࠣࡴࡾࡺࡥࡴࡶࠣࡪࡺࡴ࡮ࡦ࡮ࠣࡨࡦࡺࡡ࠻ࠢࡾࢁࠧᶐ").format(e))
def bstack1ll1l1llll_opy_(error_message, test_name, index, logger):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l111_opy_ (u"ࠩࡩ࡭ࡱ࡫࡬ࡰࡥ࡮ࠤࡳࡵࡴࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨ࠰ࠥࡻࡳࡪࡰࡪࠤࡧࡧࡳࡪࡥࠣࡪ࡮ࡲࡥࠡࡱࡳࡩࡷࡧࡴࡪࡱࡱࡷࠬᶑ"))
    try:
      bstack1111llll11l_opy_ = []
      bstack11lll1llll_opy_ = {bstack11l111_opy_ (u"ࠪࡲࡦࡳࡥࠨᶒ"): test_name, bstack11l111_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᶓ"): error_message, bstack11l111_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫᶔ"): index}
      bstack111l11l11ll_opy_ = os.path.join(tempfile.gettempdir(), bstack11l111_opy_ (u"࠭ࡲࡰࡤࡲࡸࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧᶕ"))
      if os.path.exists(bstack111l11l11ll_opy_):
          with open(bstack111l11l11ll_opy_) as f:
              bstack1111llll11l_opy_ = json.load(f)
      bstack1111llll11l_opy_.append(bstack11lll1llll_opy_)
      with open(bstack111l11l11ll_opy_, bstack11l111_opy_ (u"ࠧࡸࠩᶖ")) as f:
          json.dump(bstack1111llll11l_opy_, f)
    except Exception as e:
      logger.warn(bstack11l111_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺ࡯ࡳࡧࠣࡶࡴࡨ࡯ࡵࠢࡩࡹࡳࡴࡥ࡭ࠢࡧࡥࡹࡧ࠺ࠡࡽࢀࠦᶗ").format(e))
    return
  bstack1111llll11l_opy_ = []
  bstack11lll1llll_opy_ = {bstack11l111_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᶘ"): test_name, bstack11l111_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᶙ"): error_message, bstack11l111_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪᶚ"): index}
  bstack111l11l11ll_opy_ = os.path.join(tempfile.gettempdir(), bstack11l111_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭ᶛ"))
  lock_file = bstack111l11l11ll_opy_ + bstack11l111_opy_ (u"࠭࠮࡭ࡱࡦ࡯ࠬᶜ")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack111l11l11ll_opy_):
          with open(bstack111l11l11ll_opy_, bstack11l111_opy_ (u"ࠧࡳࠩᶝ")) as f:
              content = f.read().strip()
              if content:
                  bstack1111llll11l_opy_ = json.load(open(bstack111l11l11ll_opy_))
      bstack1111llll11l_opy_.append(bstack11lll1llll_opy_)
      with open(bstack111l11l11ll_opy_, bstack11l111_opy_ (u"ࠨࡹࠪᶞ")) as f:
          json.dump(bstack1111llll11l_opy_, f)
  except Exception as e:
    logger.warn(bstack11l111_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡷࡵࡢࡰࡶࠣࡪࡺࡴ࡮ࡦ࡮ࠣࡨࡦࡺࡡࠡࡹ࡬ࡸ࡭ࠦࡦࡪ࡮ࡨࠤࡱࡵࡣ࡬࡫ࡱ࡫࠿ࠦࡻࡾࠤᶟ").format(e))
def bstack111lll1l1l_opy_(bstack11lll11111_opy_, name, logger):
  try:
    bstack11lll1llll_opy_ = {bstack11l111_opy_ (u"ࠪࡲࡦࡳࡥࠨᶠ"): name, bstack11l111_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᶡ"): bstack11lll11111_opy_, bstack11l111_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫᶢ"): str(threading.current_thread()._name)}
    return bstack11lll1llll_opy_
  except Exception as e:
    logger.warn(bstack11l111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡴࡸࡥࠡࡤࡨ࡬ࡦࡼࡥࠡࡨࡸࡲࡳ࡫࡬ࠡࡦࡤࡸࡦࡀࠠࡼࡿࠥᶣ").format(e))
  return
def bstack111l1ll1l11_opy_():
    return platform.system() == bstack11l111_opy_ (u"ࠧࡘ࡫ࡱࡨࡴࡽࡳࠨᶤ")
def bstack1l1l11l1l1_opy_(bstack111l1ll11l1_opy_, config, logger):
    bstack1111lll11ll_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack111l1ll11l1_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack11l111_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡬ࡵࡧࡵࠤࡨࡵ࡮ࡧ࡫ࡪࠤࡰ࡫ࡹࡴࠢࡥࡽࠥࡸࡥࡨࡧࡻࠤࡲࡧࡴࡤࡪ࠽ࠤࢀࢃࠢᶥ").format(e))
    return bstack1111lll11ll_opy_
def bstack11l1ll1ll11_opy_(bstack1111ll11111_opy_, bstack1111lllll1l_opy_):
    bstack111l1l11l1l_opy_ = version.parse(bstack1111ll11111_opy_)
    bstack1111lll111l_opy_ = version.parse(bstack1111lllll1l_opy_)
    if bstack111l1l11l1l_opy_ > bstack1111lll111l_opy_:
        return 1
    elif bstack111l1l11l1l_opy_ < bstack1111lll111l_opy_:
        return -1
    else:
        return 0
def bstack1l11l111_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack111l1lllll1_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack1111lll1l11_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack111llll1ll_opy_(options, framework, config, bstack11l1ll1l1_opy_={}):
    if options is None:
        return
    if getattr(options, bstack11l111_opy_ (u"ࠩࡪࡩࡹ࠭ᶦ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack1ll1l1lll1_opy_ = caps.get(bstack11l111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᶧ"))
    bstack111l1111ll1_opy_ = True
    bstack1ll11111l_opy_ = os.environ[bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᶨ")]
    bstack1l1111lll1l_opy_ = config.get(bstack11l111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᶩ"), False)
    if bstack1l1111lll1l_opy_:
        bstack1l1l1l1llll_opy_ = config.get(bstack11l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ᶪ"), {})
        bstack1l1l1l1llll_opy_[bstack11l111_opy_ (u"ࠧࡢࡷࡷ࡬࡙ࡵ࡫ࡦࡰࠪᶫ")] = os.getenv(bstack11l111_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ᶬ"))
        bstack1111l1l111l_opy_ = json.loads(os.getenv(bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪᶭ"), bstack11l111_opy_ (u"ࠪࡿࢂ࠭ᶮ"))).get(bstack11l111_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᶯ"))
    if bstack111l111l1ll_opy_(caps.get(bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡺࡹࡥࡘ࠵ࡆࠫᶰ"))) or bstack111l111l1ll_opy_(caps.get(bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡻࡳࡦࡡࡺ࠷ࡨ࠭ᶱ"))):
        bstack111l1111ll1_opy_ = False
    if bstack1l11ll1ll1_opy_({bstack11l111_opy_ (u"ࠢࡶࡵࡨ࡛࠸ࡉࠢᶲ"): bstack111l1111ll1_opy_}):
        bstack1ll1l1lll1_opy_ = bstack1ll1l1lll1_opy_ or {}
        bstack1ll1l1lll1_opy_[bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪᶳ")] = bstack1111lll1l11_opy_(framework)
        bstack1ll1l1lll1_opy_[bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᶴ")] = bstack1lll11llll1_opy_()
        bstack1ll1l1lll1_opy_[bstack11l111_opy_ (u"ࠪࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ᶵ")] = bstack1ll11111l_opy_
        bstack1ll1l1lll1_opy_[bstack11l111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ᶶ")] = bstack11l1ll1l1_opy_
        if bstack1l1111lll1l_opy_:
            bstack1ll1l1lll1_opy_[bstack11l111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᶷ")] = bstack1l1111lll1l_opy_
            bstack1ll1l1lll1_opy_[bstack11l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ᶸ")] = bstack1l1l1l1llll_opy_
            bstack1ll1l1lll1_opy_[bstack11l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᶹ")][bstack11l111_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᶺ")] = bstack1111l1l111l_opy_
        if getattr(options, bstack11l111_opy_ (u"ࠩࡶࡩࡹࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵࡻࠪᶻ"), None):
            options.set_capability(bstack11l111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᶼ"), bstack1ll1l1lll1_opy_)
        else:
            options[bstack11l111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᶽ")] = bstack1ll1l1lll1_opy_
    else:
        if getattr(options, bstack11l111_opy_ (u"ࠬࡹࡥࡵࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸࡾ࠭ᶾ"), None):
            options.set_capability(bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧᶿ"), bstack1111lll1l11_opy_(framework))
            options.set_capability(bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨ᷀"), bstack1lll11llll1_opy_())
            options.set_capability(bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪ᷁"), bstack1ll11111l_opy_)
            options.set_capability(bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲ᷂ࠪ"), bstack11l1ll1l1_opy_)
            if bstack1l1111lll1l_opy_:
                options.set_capability(bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ᷃"), bstack1l1111lll1l_opy_)
                options.set_capability(bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ᷄"), bstack1l1l1l1llll_opy_)
                options.set_capability(bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶ࠲ࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ᷅"), bstack1111l1l111l_opy_)
        else:
            options[bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧ᷆")] = bstack1111lll1l11_opy_(framework)
            options[bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨ᷇")] = bstack1lll11llll1_opy_()
            options[bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪ᷈")] = bstack1ll11111l_opy_
            options[bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪ᷉")] = bstack11l1ll1l1_opy_
            if bstack1l1111lll1l_opy_:
                options[bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺ᷊ࠩ")] = bstack1l1111lll1l_opy_
                options[bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ᷋")] = bstack1l1l1l1llll_opy_
                options[bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ᷌")][bstack11l111_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ᷍")] = bstack1111l1l111l_opy_
    return options
def bstack111l11l1lll_opy_(ws_endpoint, framework):
    bstack11l1ll1l1_opy_ = bstack111ll111_opy_.get_property(bstack11l111_opy_ (u"ࠢࡑࡎࡄ࡝࡜ࡘࡉࡈࡊࡗࡣࡕࡘࡏࡅࡗࡆࡘࡤࡓࡁࡑࠤ᷎"))
    if ws_endpoint and len(ws_endpoint.split(bstack11l111_opy_ (u"ࠨࡥࡤࡴࡸࡃ᷏ࠧ"))) > 1:
        ws_url = ws_endpoint.split(bstack11l111_opy_ (u"ࠩࡦࡥࡵࡹ࠽ࠨ᷐"))[0]
        if bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭᷑") in ws_url:
            from browserstack_sdk._version import __version__
            bstack111l111111l_opy_ = json.loads(urllib.parse.unquote(ws_endpoint.split(bstack11l111_opy_ (u"ࠫࡨࡧࡰࡴ࠿ࠪ᷒"))[1]))
            bstack111l111111l_opy_ = bstack111l111111l_opy_ or {}
            bstack1ll11111l_opy_ = os.environ[bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪᷓ")]
            bstack111l111111l_opy_[bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧᷔ")] = str(framework) + str(__version__)
            bstack111l111111l_opy_[bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᷕ")] = bstack1lll11llll1_opy_()
            bstack111l111111l_opy_[bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪᷖ")] = bstack1ll11111l_opy_
            bstack111l111111l_opy_[bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪᷗ")] = bstack11l1ll1l1_opy_
            ws_endpoint = ws_endpoint.split(bstack11l111_opy_ (u"ࠪࡧࡦࡶࡳ࠾ࠩᷘ"))[0] + bstack11l111_opy_ (u"ࠫࡨࡧࡰࡴ࠿ࠪᷙ") + urllib.parse.quote(json.dumps(bstack111l111111l_opy_))
    return ws_endpoint
def bstack11ll1l11ll_opy_():
    global bstack1111l1l1l1_opy_
    from playwright._impl._browser_type import BrowserType
    bstack1111l1l1l1_opy_ = BrowserType.connect
    return bstack1111l1l1l1_opy_
def bstack1111l11l11_opy_(framework_name):
    global bstack1ll1ll1l1l_opy_
    bstack1ll1ll1l1l_opy_ = framework_name
    return framework_name
def bstack1llllll1l1_opy_(self, *args, **kwargs):
    global bstack1111l1l1l1_opy_
    try:
        global bstack1ll1ll1l1l_opy_
        if bstack11l111_opy_ (u"ࠬࡽࡳࡆࡰࡧࡴࡴ࡯࡮ࡵࠩᷚ") in kwargs:
            kwargs[bstack11l111_opy_ (u"࠭ࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶࠪᷛ")] = bstack111l11l1lll_opy_(
                kwargs.get(bstack11l111_opy_ (u"ࠧࡸࡵࡈࡲࡩࡶ࡯ࡪࡰࡷࠫᷜ"), None),
                bstack1ll1ll1l1l_opy_
            )
    except Exception as e:
        logger.error(bstack11l111_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪࡨࡲࠥࡶࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡖࡈࡐࠦࡣࡢࡲࡶ࠾ࠥࢁࡽࠣᷝ").format(str(e)))
    return bstack1111l1l1l1_opy_(self, *args, **kwargs)
def bstack1111ll1lll1_opy_(bstack111l11lll11_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack1llllll11l_opy_(bstack111l11lll11_opy_, bstack11l111_opy_ (u"ࠤࠥᷞ"))
        if proxies and proxies.get(bstack11l111_opy_ (u"ࠥ࡬ࡹࡺࡰࡴࠤᷟ")):
            parsed_url = urlparse(proxies.get(bstack11l111_opy_ (u"ࠦ࡭ࡺࡴࡱࡵࠥᷠ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack11l111_opy_ (u"ࠬࡶࡲࡰࡺࡼࡌࡴࡹࡴࠨᷡ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack11l111_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡵࡲࡵࠩᷢ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack11l111_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡛ࡳࡦࡴࠪᷣ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack11l111_opy_ (u"ࠨࡲࡵࡳࡽࡿࡐࡢࡵࡶࠫᷤ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack111lll1111_opy_(bstack111l11lll11_opy_):
    bstack111l111l1l1_opy_ = {
        bstack11l1l111lll_opy_[bstack111l1l1l11l_opy_]: bstack111l11lll11_opy_[bstack111l1l1l11l_opy_]
        for bstack111l1l1l11l_opy_ in bstack111l11lll11_opy_
        if bstack111l1l1l11l_opy_ in bstack11l1l111lll_opy_
    }
    bstack111l111l1l1_opy_[bstack11l111_opy_ (u"ࠤࡳࡶࡴࡾࡹࡔࡧࡷࡸ࡮ࡴࡧࡴࠤᷥ")] = bstack1111ll1lll1_opy_(bstack111l11lll11_opy_, bstack111ll111_opy_.get_property(bstack11l111_opy_ (u"ࠥࡴࡷࡵࡸࡺࡕࡨࡸࡹ࡯࡮ࡨࡵࠥᷦ")))
    bstack1111lll11l1_opy_ = [element.lower() for element in bstack11l1l1ll111_opy_]
    bstack1111ll1llll_opy_(bstack111l111l1l1_opy_, bstack1111lll11l1_opy_)
    return bstack111l111l1l1_opy_
def bstack1111ll1llll_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack11l111_opy_ (u"ࠦ࠯࠰ࠪࠫࠤᷧ")
    for value in d.values():
        if isinstance(value, dict):
            bstack1111ll1llll_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack1111ll1llll_opy_(item, keys)
def bstack1ll11l1l111_opy_():
    bstack111l11ll11l_opy_ = [os.environ.get(bstack11l111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡏࡌࡆࡕࡢࡈࡎࡘࠢᷨ")), os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠨࡾࠣᷩ")), bstack11l111_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᷪ")), os.path.join(bstack11l111_opy_ (u"ࠨ࠱ࡷࡱࡵ࠭ᷫ"), bstack11l111_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩᷬ"))]
    for path in bstack111l11ll11l_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack11l111_opy_ (u"ࠥࡊ࡮ࡲࡥࠡࠩࠥᷭ") + str(path) + bstack11l111_opy_ (u"ࠦࠬࠦࡥࡹ࡫ࡶࡸࡸ࠴ࠢᷮ"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack11l111_opy_ (u"ࠧࡍࡩࡷ࡫ࡱ࡫ࠥࡶࡥࡳ࡯࡬ࡷࡸ࡯࡯࡯ࡵࠣࡪࡴࡸࠠࠨࠤᷯ") + str(path) + bstack11l111_opy_ (u"ࠨࠧࠣᷰ"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack11l111_opy_ (u"ࠢࡇ࡫࡯ࡩࠥ࠭ࠢᷱ") + str(path) + bstack11l111_opy_ (u"ࠣࠩࠣࡥࡱࡸࡥࡢࡦࡼࠤ࡭ࡧࡳࠡࡶ࡫ࡩࠥࡸࡥࡲࡷ࡬ࡶࡪࡪࠠࡱࡧࡵࡱ࡮ࡹࡳࡪࡱࡱࡷ࠳ࠨᷲ"))
            else:
                logger.debug(bstack11l111_opy_ (u"ࠤࡆࡶࡪࡧࡴࡪࡰࡪࠤ࡫࡯࡬ࡦࠢࠪࠦᷳ") + str(path) + bstack11l111_opy_ (u"ࠥࠫࠥࡽࡩࡵࡪࠣࡻࡷ࡯ࡴࡦࠢࡳࡩࡷࡳࡩࡴࡵ࡬ࡳࡳ࠴ࠢᷴ"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack11l111_opy_ (u"ࠦࡔࡶࡥࡳࡣࡷ࡭ࡴࡴࠠࡴࡷࡦࡧࡪ࡫ࡤࡦࡦࠣࡪࡴࡸࠠࠨࠤ᷵") + str(path) + bstack11l111_opy_ (u"ࠧ࠭࠮ࠣ᷶"))
            return path
        except Exception as e:
            logger.debug(bstack11l111_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡵࡱࠢࡩ࡭ࡱ࡫ࠠࠨࡽࡳࡥࡹ࡮ࡽࠨ࠼᷷ࠣࠦ") + str(e) + bstack11l111_opy_ (u"᷸ࠢࠣ"))
    logger.debug(bstack11l111_opy_ (u"ࠣࡃ࡯ࡰࠥࡶࡡࡵࡪࡶࠤ࡫ࡧࡩ࡭ࡧࡧ࠲᷹ࠧ"))
    return None
@measure(event_name=EVENTS.bstack11l1l1l111l_opy_, stage=STAGE.bstack1l111l11l_opy_)
def bstack1l11lllll11_opy_(binary_path, bstack1l1l1llll11_opy_, bs_config):
    logger.debug(bstack11l111_opy_ (u"ࠤࡆࡹࡷࡸࡥ࡯ࡶࠣࡇࡑࡏࠠࡑࡣࡷ࡬ࠥ࡬࡯ࡶࡰࡧ࠾ࠥࢁࡽ᷺ࠣ").format(binary_path))
    bstack1111ll1l1l1_opy_ = bstack11l111_opy_ (u"ࠪࠫ᷻")
    bstack111ll11111l_opy_ = {
        bstack11l111_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ᷼"): __version__,
        bstack11l111_opy_ (u"ࠧࡵࡳ᷽ࠣ"): platform.system(),
        bstack11l111_opy_ (u"ࠨ࡯ࡴࡡࡤࡶࡨ࡮ࠢ᷾"): platform.machine(),
        bstack11l111_opy_ (u"ࠢࡤ࡮࡬ࡣࡻ࡫ࡲࡴ࡫ࡲࡲ᷿ࠧ"): bstack11l111_opy_ (u"ࠨ࠲ࠪḀ"),
        bstack11l111_opy_ (u"ࠤࡶࡨࡰࡥ࡬ࡢࡰࡪࡹࡦ࡭ࡥࠣḁ"): bstack11l111_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪḂ")
    }
    bstack1111llll1l1_opy_(bstack111ll11111l_opy_)
    try:
        if binary_path:
            bstack111ll11111l_opy_[bstack11l111_opy_ (u"ࠫࡨࡲࡩࡠࡸࡨࡶࡸ࡯࡯࡯ࠩḃ")] = subprocess.check_output([binary_path, bstack11l111_opy_ (u"ࠧࡼࡥࡳࡵ࡬ࡳࡳࠨḄ")]).strip().decode(bstack11l111_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬḅ"))
        response = requests.request(
            bstack11l111_opy_ (u"ࠧࡈࡇࡗࠫḆ"),
            url=bstack11ll1l1l1_opy_(bstack11l1l1111ll_opy_),
            headers=None,
            auth=(bs_config[bstack11l111_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪḇ")], bs_config[bstack11l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬḈ")]),
            json=None,
            params=bstack111ll11111l_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack11l111_opy_ (u"ࠪࡹࡷࡲࠧḉ") in data.keys() and bstack11l111_opy_ (u"ࠫࡺࡶࡤࡢࡶࡨࡨࡤࡩ࡬ࡪࡡࡹࡩࡷࡹࡩࡰࡰࠪḊ") in data.keys():
            logger.debug(bstack11l111_opy_ (u"ࠧࡔࡥࡦࡦࠣࡸࡴࠦࡵࡱࡦࡤࡸࡪࠦࡢࡪࡰࡤࡶࡾ࠲ࠠࡤࡷࡵࡶࡪࡴࡴࠡࡤ࡬ࡲࡦࡸࡹࠡࡸࡨࡶࡸ࡯࡯࡯࠼ࠣࡿࢂࠨḋ").format(bstack111ll11111l_opy_[bstack11l111_opy_ (u"࠭ࡣ࡭࡫ࡢࡺࡪࡸࡳࡪࡱࡱࠫḌ")]))
            if bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡊࡐࡄࡖ࡞ࡥࡕࡓࡎࠪḍ") in os.environ:
                logger.debug(bstack11l111_opy_ (u"ࠣࡕ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡦ࡮ࡴࡡࡳࡻࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠥࡧࡳࠡࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡋࡑࡅࡗ࡟࡟ࡖࡔࡏࠤ࡮ࡹࠠࡴࡧࡷࠦḎ"))
                data[bstack11l111_opy_ (u"ࠩࡸࡶࡱ࠭ḏ")] = os.environ[bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡘࡖࡑ࠭Ḑ")]
            bstack111l1l11l11_opy_ = bstack111l1lll1ll_opy_(data[bstack11l111_opy_ (u"ࠫࡺࡸ࡬ࠨḑ")], bstack1l1l1llll11_opy_)
            bstack1111ll1l1l1_opy_ = os.path.join(bstack1l1l1llll11_opy_, bstack111l1l11l11_opy_)
            os.chmod(bstack1111ll1l1l1_opy_, 0o777) # bstack111l1111l1l_opy_ permission
            return bstack1111ll1l1l1_opy_
    except Exception as e:
        logger.debug(bstack11l111_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡨࡴࡽ࡮࡭ࡱࡤࡨ࡮ࡴࡧࠡࡰࡨࡻ࡙ࠥࡄࡌࠢࡾࢁࠧḒ").format(e))
    return binary_path
def bstack1111llll1l1_opy_(bstack111ll11111l_opy_):
    try:
        if bstack11l111_opy_ (u"࠭࡬ࡪࡰࡸࡼࠬḓ") not in bstack111ll11111l_opy_[bstack11l111_opy_ (u"ࠧࡰࡵࠪḔ")].lower():
            return
        if os.path.exists(bstack11l111_opy_ (u"ࠣ࠱ࡨࡸࡨ࠵࡯ࡴ࠯ࡵࡩࡱ࡫ࡡࡴࡧࠥḕ")):
            with open(bstack11l111_opy_ (u"ࠤ࠲ࡩࡹࡩ࠯ࡰࡵ࠰ࡶࡪࡲࡥࡢࡵࡨࠦḖ"), bstack11l111_opy_ (u"ࠥࡶࠧḗ")) as f:
                bstack111l1l1l1l1_opy_ = {}
                for line in f:
                    if bstack11l111_opy_ (u"ࠦࡂࠨḘ") in line:
                        key, value = line.rstrip().split(bstack11l111_opy_ (u"ࠧࡃࠢḙ"), 1)
                        bstack111l1l1l1l1_opy_[key] = value.strip(bstack11l111_opy_ (u"࠭ࠢ࡝ࠩࠪḚ"))
                bstack111ll11111l_opy_[bstack11l111_opy_ (u"ࠧࡥ࡫ࡶࡸࡷࡵࠧḛ")] = bstack111l1l1l1l1_opy_.get(bstack11l111_opy_ (u"ࠣࡋࡇࠦḜ"), bstack11l111_opy_ (u"ࠤࠥḝ"))
        elif os.path.exists(bstack11l111_opy_ (u"ࠥ࠳ࡪࡺࡣ࠰ࡣ࡯ࡴ࡮ࡴࡥ࠮ࡴࡨࡰࡪࡧࡳࡦࠤḞ")):
            bstack111ll11111l_opy_[bstack11l111_opy_ (u"ࠫࡩ࡯ࡳࡵࡴࡲࠫḟ")] = bstack11l111_opy_ (u"ࠬࡧ࡬ࡱ࡫ࡱࡩࠬḠ")
    except Exception as e:
        logger.debug(bstack11l111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡪࡩࡹࠦࡤࡪࡵࡷࡶࡴࠦ࡯ࡧࠢ࡯࡭ࡳࡻࡸࠣḡ") + e)
@measure(event_name=EVENTS.bstack11l1l111l1l_opy_, stage=STAGE.bstack1l111l11l_opy_)
def bstack111l1lll1ll_opy_(bstack111l1l11ll1_opy_, bstack1111ll1l11l_opy_):
    logger.debug(bstack11l111_opy_ (u"ࠢࡅࡱࡺࡲࡱࡵࡡࡥ࡫ࡱ࡫࡙ࠥࡄࡌࠢࡥ࡭ࡳࡧࡲࡺࠢࡩࡶࡴࡳ࠺ࠡࠤḢ") + str(bstack111l1l11ll1_opy_) + bstack11l111_opy_ (u"ࠣࠤḣ"))
    zip_path = os.path.join(bstack1111ll1l11l_opy_, bstack11l111_opy_ (u"ࠤࡧࡳࡼࡴ࡬ࡰࡣࡧࡩࡩࡥࡦࡪ࡮ࡨ࠲ࡿ࡯ࡰࠣḤ"))
    bstack111l1l11l11_opy_ = bstack11l111_opy_ (u"ࠪࠫḥ")
    with requests.get(bstack111l1l11ll1_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack11l111_opy_ (u"ࠦࡼࡨࠢḦ")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack11l111_opy_ (u"ࠧࡌࡩ࡭ࡧࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࡪࡪࠠࡴࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࡰࡾ࠴ࠢḧ"))
    with zipfile.ZipFile(zip_path, bstack11l111_opy_ (u"࠭ࡲࠨḨ")) as zip_ref:
        bstack111l1111111_opy_ = zip_ref.namelist()
        if len(bstack111l1111111_opy_) > 0:
            bstack111l1l11l11_opy_ = bstack111l1111111_opy_[0] # bstack111l11l1111_opy_ bstack11l11llll1l_opy_ will be bstack1111l1lll1l_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack1111ll1l11l_opy_)
        logger.debug(bstack11l111_opy_ (u"ࠢࡇ࡫࡯ࡩࡸࠦࡳࡶࡥࡦࡩࡸࡹࡦࡶ࡮࡯ࡽࠥ࡫ࡸࡵࡴࡤࡧࡹ࡫ࡤࠡࡶࡲࠤࠬࠨḩ") + str(bstack1111ll1l11l_opy_) + bstack11l111_opy_ (u"ࠣࠩࠥḪ"))
    os.remove(zip_path)
    return bstack111l1l11l11_opy_
def get_cli_dir():
    bstack1111l1ll1ll_opy_ = bstack1ll11l1l111_opy_()
    if bstack1111l1ll1ll_opy_:
        bstack1l1l1llll11_opy_ = os.path.join(bstack1111l1ll1ll_opy_, bstack11l111_opy_ (u"ࠤࡦࡰ࡮ࠨḫ"))
        if not os.path.exists(bstack1l1l1llll11_opy_):
            os.makedirs(bstack1l1l1llll11_opy_, mode=0o777, exist_ok=True)
        return bstack1l1l1llll11_opy_
    else:
        raise FileNotFoundError(bstack11l111_opy_ (u"ࠥࡒࡴࠦࡷࡳ࡫ࡷࡥࡧࡲࡥࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡕࡇࡏࠥࡨࡩ࡯ࡣࡵࡽ࠳ࠨḬ"))
def bstack1l1l111lll1_opy_(bstack1l1l1llll11_opy_):
    bstack11l111_opy_ (u"ࠦࠧࠨࡇࡦࡶࠣࡸ࡭࡫ࠠࡱࡣࡷ࡬ࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯࡙ࠥࡄࡌࠢࡥ࡭ࡳࡧࡲࡺࠢ࡬ࡲࠥࡧࠠࡸࡴ࡬ࡸࡦࡨ࡬ࡦࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽ࠳ࠨࠢࠣḭ")
    bstack111l111l11l_opy_ = [
        os.path.join(bstack1l1l1llll11_opy_, f)
        for f in os.listdir(bstack1l1l1llll11_opy_)
        if os.path.isfile(os.path.join(bstack1l1l1llll11_opy_, f)) and f.startswith(bstack11l111_opy_ (u"ࠧࡨࡩ࡯ࡣࡵࡽ࠲ࠨḮ"))
    ]
    if len(bstack111l111l11l_opy_) > 0:
        return max(bstack111l111l11l_opy_, key=os.path.getmtime) # get bstack111l111ll1l_opy_ binary
    return bstack11l111_opy_ (u"ࠨࠢḯ")
def bstack1111ll11ll1_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l1111l1l11_opy_(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = bstack1l1111l1l11_opy_(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack111l11l1l_opy_(data, keys, default=None):
    bstack11l111_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡔࡣࡩࡩࡱࡿࠠࡨࡧࡷࠤࡦࠦ࡮ࡦࡵࡷࡩࡩࠦࡶࡢ࡮ࡸࡩࠥ࡬ࡲࡰ࡯ࠣࡥࠥࡪࡩࡤࡶ࡬ࡳࡳࡧࡲࡺࠢࡲࡶࠥࡲࡩࡴࡶ࠱ࠎࠥࠦࠠࠡ࠼ࡳࡥࡷࡧ࡭ࠡࡦࡤࡸࡦࡀࠠࡕࡪࡨࠤࡩ࡯ࡣࡵ࡫ࡲࡲࡦࡸࡹࠡࡱࡵࠤࡱ࡯ࡳࡵࠢࡷࡳࠥࡺࡲࡢࡸࡨࡶࡸ࡫࠮ࠋࠢࠣࠤࠥࡀࡰࡢࡴࡤࡱࠥࡱࡥࡺࡵ࠽ࠤࡆࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠ࡬ࡧࡼࡷ࠴࡯࡮ࡥ࡫ࡦࡩࡸࠦࡲࡦࡲࡵࡩࡸ࡫࡮ࡵ࡫ࡱ࡫ࠥࡺࡨࡦࠢࡳࡥࡹ࡮࠮ࠋࠢࠣࠤࠥࡀࡰࡢࡴࡤࡱࠥࡪࡥࡧࡣࡸࡰࡹࡀࠠࡗࡣ࡯ࡹࡪࠦࡴࡰࠢࡵࡩࡹࡻࡲ࡯ࠢ࡬ࡪࠥࡺࡨࡦࠢࡳࡥࡹ࡮ࠠࡥࡱࡨࡷࠥࡴ࡯ࡵࠢࡨࡼ࡮ࡹࡴ࠯ࠌࠣࠤࠥࠦ࠺ࡳࡧࡷࡹࡷࡴ࠺ࠡࡖ࡫ࡩࠥࡼࡡ࡭ࡷࡨࠤࡦࡺࠠࡵࡪࡨࠤࡳ࡫ࡳࡵࡧࡧࠤࡵࡧࡴࡩ࠮ࠣࡳࡷࠦࡤࡦࡨࡤࡹࡱࡺࠠࡪࡨࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩ࠴ࠊࠡࠢࠣࠤࠧࠨࠢḰ")
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