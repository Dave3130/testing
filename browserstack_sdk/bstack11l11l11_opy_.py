# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
import multiprocessing
import os
import json
from time import sleep
import time
import bstack_utils.accessibility as bstack11111ll1_opy_
import subprocess
import re
from browserstack_sdk.bstack111l1111_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack111ll1ll_opy_
from bstack_utils.bstack111l1lll_opy_ import bstack1llll111l_opy_
from bstack_utils.constants import bstack1llll1l1l_opy_
from bstack_utils.bstack1111111l_opy_ import bstack1lll1lll1_opy_
class bstack1llll1l11_opy_:
    def __init__(self, args, logger, bstack1111l1ll_opy_, bstack111l11ll_opy_):
        self.args = args
        self.logger = logger
        self.bstack1111l1ll_opy_ = bstack1111l1ll_opy_
        self.bstack111l11ll_opy_ = bstack111l11ll_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack1111l111_opy_ = []
        self.bstack1llll1ll1_opy_ = []
        self.bstack11l1l111_opy_ = []
        self.bstack1llllll1l_opy_ = self.bstack1111llll_opy_()
        self.bstack111l1l11_opy_ = -1
    def bstack1111lll1_opy_(self, bstack11111l1l_opy_):
        self.parse_args()
        self.bstack111lllll_opy_()
        self.bstack111l1l1l_opy_(bstack11111l1l_opy_)
        self.bstack1llll1111_opy_()
    def bstack1lllll11l_opy_(self):
        bstack1111111l_opy_ = bstack1lll1lll1_opy_.bstack1llllllll_opy_(self.bstack1111l1ll_opy_, self.logger)
        if bstack1111111l_opy_ is None:
            self.logger.warn(bstack1ll1ll1_opy_ (u"ࠢࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡩࡣࡱࡨࡱ࡫ࡲࠡ࡫ࡶࠤࡳࡵࡴࠡ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡩࡩ࠴ࠠࡔ࡭࡬ࡴࡵ࡯࡮ࡨࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥ঒"))
            return
        bstack1111l1l1_opy_ = False
        bstack1111111l_opy_.bstack111ll111_opy_(bstack1ll1ll1_opy_ (u"ࠣࡧࡱࡥࡧࡲࡥࡥࠤও"), bstack1111111l_opy_.bstack1lllll1ll_opy_())
        start_time = time.time()
        if bstack1111111l_opy_.bstack1lllll1ll_opy_():
            test_files = self.bstack1lllll1l1_opy_()
            bstack1111l1l1_opy_ = True
            bstack1111l11l_opy_ = bstack1111111l_opy_.bstack111l1ll1_opy_(test_files)
            if bstack1111l11l_opy_:
                self.bstack1111l111_opy_ = [os.path.normpath(item).replace(bstack1ll1ll1_opy_ (u"ࠩ࡟ࡠࠬঔ"), bstack1ll1ll1_opy_ (u"ࠪ࠳ࠬক")) for item in bstack1111l11l_opy_]
                self.__1lll1llll_opy_()
                bstack1111111l_opy_.bstack11l11lll_opy_(bstack1111l1l1_opy_)
                self.logger.info(bstack1ll1ll1_opy_ (u"࡙ࠦ࡫ࡳࡵࡵࠣࡶࡪࡵࡲࡥࡧࡵࡩࡩࠦࡵࡴ࡫ࡱ࡫ࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠤখ").format(self.bstack1111l111_opy_))
            else:
                self.logger.info(bstack1ll1ll1_opy_ (u"ࠧࡔ࡯ࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡽࡥࡳࡧࠣࡶࡪࡵࡲࡥࡧࡵࡩࡩࠦࡢࡺࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥগ"))
        bstack1111111l_opy_.bstack111ll111_opy_(bstack1ll1ll1_opy_ (u"ࠨࡴࡪ࡯ࡨࡘࡦࡱࡥ࡯ࡖࡲࡅࡵࡶ࡬ࡺࠤঘ"), int((time.time() - start_time) * 1000)) # bstack11l11111_opy_ to bstack111lll1l_opy_
    def __1lll1llll_opy_(self):
        bstack1ll1ll1_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡋࡵࡲࠡࡧࡤࡧ࡭ࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࠢ࡬ࡲࠥࡹࡥ࡭ࡨ࠱ࡷࡵ࡫ࡣࡠࡨ࡬ࡰࡪࡹࠬࠡࡥࡲࡰࡱ࡫ࡣࡵࠢࡤࡰࡱࠦ࡮ࡰࡦࡨ࡭ࡩࡹࠠࡶࡵ࡬ࡲ࡬ࠦࡰࡺࡶࡨࡷࡹࠦ࠭࠮ࡥࡲࡰࡱ࡫ࡣࡵ࠯ࡲࡲࡱࡿࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦঙ")
        bstack1111ll1l_opy_ = []
        for bstack11111lll_opy_ in self.bstack1111l111_opy_:
            try:
                bstack1111ll11_opy_ = [bstack1ll1ll1_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࠣচ"), bstack11111lll_opy_, bstack1ll1ll1_opy_ (u"ࠤ࠰࠱ࡨࡵ࡬࡭ࡧࡦࡸ࠲ࡵ࡮࡭ࡻࠥছ"), bstack1ll1ll1_opy_ (u"ࠥ࠱ࡶࠨজ")]
                result = subprocess.run(bstack1111ll11_opy_, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if result.returncode != 0 and result.stdout:
                    self.logger.error(bstack1ll1ll1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡧࡴࡲ࡬ࡦࡥࡷ࡭ࡳ࡭ࠠ࡯ࡱࡧࡩࠥ࡯ࡤࠡࡨࡲࡶࠥࢁࡽ࠻ࠢࡾࢁࠧঝ").format(bstack11111lll_opy_, result.stderr))
                    continue
                for line in result.stdout.splitlines():
                    line = line.strip()
                    if line and not line.startswith(bstack1ll1ll1_opy_ (u"ࠧࡂࠢঞ")) and bstack1ll1ll1_opy_ (u"ࠨ࠺࠻ࠤট") in line:
                        bstack1111ll1l_opy_.append(line)
            except Exception as e:
                self.logger.error(bstack1ll1ll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡲࡴࡪࡥࠡ࡫ࡧࠤ࡫ࡵࡲࠡࡨ࡬ࡰࡪࡀࠠࡼࡿࠥঠ").format(bstack11111lll_opy_))
                return 0
        os.environ[bstack1ll1ll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡐࡔࡆࡌࡊ࡙ࡔࡓࡃࡗࡉࡉࡥࡓࡆࡎࡈࡇ࡙ࡕࡒࡔࠩড")] = json.dumps(bstack1111ll1l_opy_)
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack111111ll_opy_():
        import importlib
        if getattr(importlib, bstack1ll1ll1_opy_ (u"ࠩࡩ࡭ࡳࡪ࡟࡭ࡱࡤࡨࡪࡸࠧঢ"), False):
            bstack1lllllll1_opy_ = importlib.find_loader(bstack1ll1ll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࠬণ"))
        else:
            bstack1lllllll1_opy_ = importlib.util.find_spec(bstack1ll1ll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭ত"))
    def bstack11l111l1_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack111l1l11_opy_ = -1
        if self.bstack111l11ll_opy_ and bstack1ll1ll1_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬথ") in self.bstack1111l1ll_opy_:
            self.bstack111l1l11_opy_ = int(self.bstack1111l1ll_opy_[bstack1ll1ll1_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭দ")])
        try:
            bstack1llll1lll_opy_ = [bstack1ll1ll1_opy_ (u"ࠧ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠩধ"), bstack1ll1ll1_opy_ (u"ࠨ࠯࠰ࡴࡱࡻࡧࡪࡰࡶࠫন"), bstack1ll1ll1_opy_ (u"ࠩ࠰ࡴࠬ঩")]
            if self.bstack111l1l11_opy_ >= 0:
                bstack1llll1lll_opy_.extend([bstack1ll1ll1_opy_ (u"ࠪ࠱࠲ࡴࡵ࡮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫপ"), bstack1ll1ll1_opy_ (u"ࠫ࠲ࡴࠧফ")])
            for arg in bstack1llll1lll_opy_:
                self.bstack11l111l1_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack111lllll_opy_(self):
        bstack1llll1ll1_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack1llll1ll1_opy_ = bstack1llll1ll1_opy_
        return self.bstack1llll1ll1_opy_
    def bstack11111111_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack111111ll_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack111ll1ll_opy_)
    def bstack111l1l1l_opy_(self, bstack11111l1l_opy_):
        bstack11111l11_opy_ = Config.bstack1llllllll_opy_()
        if bstack11111l1l_opy_:
            self.bstack1llll1ll1_opy_.append(bstack1ll1ll1_opy_ (u"ࠬ࠳࠭ࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩব"))
            self.bstack1llll1ll1_opy_.append(bstack1ll1ll1_opy_ (u"࠭ࡔࡳࡷࡨࠫভ"))
        if bstack11111l11_opy_.bstack11l1111l_opy_():
            self.bstack1llll1ll1_opy_.append(bstack1ll1ll1_opy_ (u"ࠧ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭ম"))
            self.bstack1llll1ll1_opy_.append(bstack1ll1ll1_opy_ (u"ࠨࡖࡵࡹࡪ࠭য"))
        self.bstack1llll1ll1_opy_.append(bstack1ll1ll1_opy_ (u"ࠩ࠰ࡴࠬর"))
        self.bstack1llll1ll1_opy_.append(bstack1ll1ll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡲ࡯ࡹ࡬࡯࡮ࠨ঱"))
        self.bstack1llll1ll1_opy_.append(bstack1ll1ll1_opy_ (u"ࠫ࠲࠳ࡤࡳ࡫ࡹࡩࡷ࠭ল"))
        self.bstack1llll1ll1_opy_.append(bstack1ll1ll1_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬ঳"))
        if self.bstack111l1l11_opy_ > 1:
            self.bstack1llll1ll1_opy_.append(bstack1ll1ll1_opy_ (u"࠭࠭࡯ࠩ঴"))
            self.bstack1llll1ll1_opy_.append(str(self.bstack111l1l11_opy_))
    def bstack1llll1111_opy_(self):
        if bstack1llll111l_opy_.bstack11l1l11l_opy_(self.bstack1111l1ll_opy_):
             self.bstack1llll1ll1_opy_ += [
                bstack1llll1l1l_opy_.get(bstack1ll1ll1_opy_ (u"ࠧࡳࡧࡵࡹࡳ࠭঵")), str(bstack1llll111l_opy_.bstack111111l1_opy_(self.bstack1111l1ll_opy_)),
                bstack1llll1l1l_opy_.get(bstack1ll1ll1_opy_ (u"ࠨࡦࡨࡰࡦࡿࠧশ")), str(bstack1llll1l1l_opy_.get(bstack1ll1ll1_opy_ (u"ࠩࡵࡩࡷࡻ࡮࠮ࡦࡨࡰࡦࡿࠧষ")))
            ]
    def bstack1llll11l1_opy_(self):
        bstack11l1l111_opy_ = []
        for spec in self.bstack1111l111_opy_:
            bstack11l11l1l_opy_ = [spec]
            bstack11l11l1l_opy_ += self.bstack1llll1ll1_opy_
            bstack11l1l111_opy_.append(bstack11l11l1l_opy_)
        self.bstack11l1l111_opy_ = bstack11l1l111_opy_
        return bstack11l1l111_opy_
    def bstack1111llll_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack1llllll1l_opy_ = True
            return True
        except Exception as e:
            self.bstack1llllll1l_opy_ = False
        return self.bstack1llllll1l_opy_
    def bstack111l11l1_opy_(self):
        bstack1ll1ll1_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡌ࡫ࡴࠡࡶ࡫ࡩࠥࡩ࡯ࡶࡰࡷࠤࡴ࡬ࠠࡵࡧࡶࡸࡸࠦࡷࡪࡶ࡫ࡳࡺࡺࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡶ࡫ࡩࡲࠦࡵࡴ࡫ࡱ࡫ࠥࡶࡹࡵࡧࡶࡸࠬࡹࠠ࠮࠯ࡦࡳࡱࡲࡥࡤࡶ࠰ࡳࡳࡲࡹࠡࡨ࡯ࡥ࡬࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࡬ࡲࡹࡀࠠࡕࡪࡨࠤࡹࡵࡴࡢ࡮ࠣࡲࡺࡳࡢࡦࡴࠣࡳ࡫ࠦࡴࡦࡵࡷࡷࠥࡩ࡯࡭࡮ࡨࡧࡹ࡫ࡤ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨস")
        try:
            self.logger.info(bstack1ll1ll1_opy_ (u"ࠦࡈࡵ࡬࡭ࡧࡦࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࡹࠠࡶࡵ࡬ࡲ࡬ࠦࡰࡺࡶࡨࡷࡹࠦ࠭࠮ࡥࡲࡰࡱ࡫ࡣࡵ࠯ࡲࡲࡱࡿࠢহ"))
            bstack1111ll11_opy_ = [bstack1ll1ll1_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸࠧ঺"), *self.bstack1llll1ll1_opy_, bstack1ll1ll1_opy_ (u"ࠨ࠭࠮ࡥࡲࡰࡱ࡫ࡣࡵ࠯ࡲࡲࡱࡿࠢ঻"), bstack1ll1ll1_opy_ (u"ࠢ࠮ࡳ়ࠥ")]
            result = subprocess.run(
                bstack1111ll11_opy_,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            if result.returncode not in (0, 5) and result.stdout:
                self.logger.error(bstack1ll1ll1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡣࡰ࡮࡯ࡩࡨࡺࡩ࡯ࡩࠣࡸࡪࡹࡴࡴ࠼ࠣࡿࢂࠨঽ").format(result.stderr))
                return 0
            self.logger.info(bstack1ll1ll1_opy_ (u"ࠤ࡞ࡸࡴࡺࡡ࡭ࡡࡷࡩࡸࡺࡳ࡞ࠢࡕࡥࡼࠦ࡯ࡶࡶࡳࡹࡹࠦࡦࡳࡱࡰࠤࡵࡿࡴࡦࡵࡷࠤ࠲࠳ࡣࡰ࡮࡯ࡩࡨࡺ࠭ࡰࡰ࡯ࡽ࠿ࡢ࡮ࡼࡿࠥা").format(result.stdout))
            test_count = 0
            for line in result.stdout.splitlines():
                line = line.strip()
                if line and bstack1ll1ll1_opy_ (u"ࠪ࠾࠿࠭ি") in line and not line.startswith(bstack1ll1ll1_opy_ (u"ࠫࡁ࠭ী")) and not line.endswith(bstack1ll1ll1_opy_ (u"ࠬࡩ࡯࡭࡮ࡨࡧࡹ࡫ࡤࠨু")):
                    test_count += 1
            self.logger.info(bstack1ll1ll1_opy_ (u"ࠨࡔࡰࡶࡤࡰࠥࡺࡥࡴࡶࡶࠤࡨࡵ࡬࡭ࡧࡦࡸࡪࡪ࠺ࠡࡽࢀࠦূ").format(test_count))
            return test_count
        except Exception as e:
            self.logger.error(bstack1ll1ll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡥࡲࡹࡳࡺ࠺ࠡࡽࢀࠦৃ").format(e))
            return 0
    def bstack111llll1_opy_(self, bstack111ll11l_opy_, bstack1111lll1_opy_):
        bstack1111lll1_opy_[bstack1ll1ll1_opy_ (u"ࠨࡅࡒࡒࡋࡏࡇࠨৄ")] = self.bstack1111l1ll_opy_
        multiprocessing.set_start_method(bstack1ll1ll1_opy_ (u"ࠩࡶࡴࡦࡽ࡮ࠨ৅"))
        bstack111lll11_opy_ = []
        manager = multiprocessing.Manager()
        bstack11l111ll_opy_ = manager.list()
        if bstack1ll1ll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭৆") in self.bstack1111l1ll_opy_:
            for index, platform in enumerate(self.bstack1111l1ll_opy_[bstack1ll1ll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧে")]):
                bstack111lll11_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack111ll11l_opy_,
                                                            args=(self.bstack1llll1ll1_opy_, bstack1111lll1_opy_, bstack11l111ll_opy_)))
            bstack1llll11ll_opy_ = len(self.bstack1111l1ll_opy_[bstack1ll1ll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨৈ")])
        else:
            bstack111lll11_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack111ll11l_opy_,
                                                        args=(self.bstack1llll1ll1_opy_, bstack1111lll1_opy_, bstack11l111ll_opy_)))
            bstack1llll11ll_opy_ = 1
        i = 0
        for t in bstack111lll11_opy_:
            os.environ[bstack1ll1ll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭৉")] = str(i)
            if bstack1ll1ll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ৊") in self.bstack1111l1ll_opy_:
                os.environ[bstack1ll1ll1_opy_ (u"ࠨࡅࡘࡖࡗࡋࡎࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡉࡇࡔࡂࠩো")] = json.dumps(self.bstack1111l1ll_opy_[bstack1ll1ll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬৌ")][i % bstack1llll11ll_opy_])
            i += 1
            t.start()
        for t in bstack111lll11_opy_:
            t.join()
        return list(bstack11l111ll_opy_)
    @staticmethod
    def bstack1lll1ll1l_opy_(driver, bstack1lllll111_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳ্ࠧ"), None)
        if item and getattr(item, bstack1ll1ll1_opy_ (u"ࠫࡤࡧ࠱࠲ࡻࡢࡸࡪࡹࡴࡠࡥࡤࡷࡪ࠭ৎ"), None) and not getattr(item, bstack1ll1ll1_opy_ (u"ࠬࡥࡡ࠲࠳ࡼࡣࡸࡺ࡯ࡱࡡࡧࡳࡳ࡫ࠧ৏"), False):
            logger.info(
                bstack1ll1ll1_opy_ (u"ࠨࡁࡶࡶࡲࡱࡦࡺࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴࠠࡩࡣࡶࠤࡪࡴࡤࡦࡦ࠱ࠤࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡨࡲࡶࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡺࡥࡴࡶ࡬ࡲ࡬ࠦࡩࡴࠢࡸࡲࡩ࡫ࡲࡸࡣࡼ࠲ࠧ৐"))
            bstack1llllll11_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack11111ll1_opy_.bstack111l111l_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)
    def bstack1lllll1l1_opy_(self):
        bstack1ll1ll1_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷࠥࡺࡨࡦࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹࠠࡵࡱࠣࡦࡪࠦࡥࡹࡧࡦࡹࡹ࡫ࡤࠡࡤࡼࠤࡵࡧࡲࡴ࡫ࡱ࡫ࠥࡺࡨࡦࠢࡲࡹࡹࡶࡵࡵࠢࡲࡪࠥࡶࡹࡵࡧࡶࡸࠥ࠳࠭ࡤࡱ࡯ࡰࡪࡩࡴ࠮ࡱࡱࡰࡾ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦ৑")
        try:
            bstack1111ll11_opy_ = [
                bstack1ll1ll1_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࠣ৒"),
                *self.bstack1llll1ll1_opy_,
                bstack1ll1ll1_opy_ (u"ࠤ࠰࠱ࡨࡵ࡬࡭ࡧࡦࡸ࠲ࡵ࡮࡭ࡻࠥ৓"),
                bstack1ll1ll1_opy_ (u"ࠥ࠱ࡶࠨ৔")  # bstack11l11ll1_opy_ mode for bstack111ll1l1_opy_ output
            ]
            result = subprocess.run(
                bstack1111ll11_opy_,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            if result.returncode not in (0, 5) and result.stdout:
                self.logger.error(bstack1ll1ll1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࡷࠥ࡬ࡩ࡭ࡧ࠽ࠤࢀࢃࠧ৕").format(result.stderr))
                return []
            self.logger.info(bstack1ll1ll1_opy_ (u"ࠧࡡࡧࡦࡶࡢࡸࡪࡹࡴࡠࡨ࡬ࡰࡪࡹ࡝ࠡࡔࡤࡻࠥࡵࡵࡵࡲࡸࡸࠥ࡬ࡲࡰ࡯ࠣࡴࡾࡺࡥࡴࡶࠣ࠱࠲ࡩ࡯࡭࡮ࡨࡧࡹ࠳࡯࡯࡮ࡼ࠾ࡡࡴࡻࡾࠤ৖").format(result.stdout))
            file_paths = set()
            for line in result.stdout.splitlines():
                line = line.strip()
                if line and bstack1ll1ll1_opy_ (u"࠭࠺࠻ࠩৗ") in line and not line.startswith(bstack1ll1ll1_opy_ (u"ࠧ࠽ࠩ৘")):
                    file_path = line.split(bstack1ll1ll1_opy_ (u"ࠨ࠼࠽ࠫ৙"), 1)[0]
                    if file_path.endswith(bstack1ll1ll1_opy_ (u"ࠩ࠱ࡴࡾ࠭৚")):
                        file_paths.add(file_path)
            test_files = sorted(file_paths)
            if test_files:
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠥࡇࡴࡲ࡬ࡦࡥࡷࡩࡩࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵ࠽ࠤࢀࢃࠢ৛").format(len(test_files)))
            elif result.returncode == 5:
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡓࡵࠠࡵࡧࡶࡸࡸࠦࡦࡪ࡮ࡨࡷࠥࡩ࡯࡭࡮ࡨࡧࡹ࡫ࡤࠣড়"))
            return test_files
        except Exception as e:
            self.logger.error(bstack1ll1ll1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠧঢ়").format(e))
            return []