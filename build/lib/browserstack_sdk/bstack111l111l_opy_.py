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
import multiprocessing
import os
import json
from time import sleep
import time
import bstack_utils.accessibility as bstack1111ll11_opy_
from browserstack_sdk.bstack1111llll_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack1lll1l1ll_opy_
from bstack_utils.bstack11111lll_opy_ import bstack111ll1ll_opy_
from bstack_utils.constants import bstack111111l1_opy_
from bstack_utils.bstack1lll11l11_opy_ import bstack1lll1l11l_opy_
class bstack1lll11lll_opy_:
    def __init__(self, args, logger, bstack1lll111l1_opy_, bstack1lll1l111_opy_):
        self.args = args
        self.logger = logger
        self.bstack1lll111l1_opy_ = bstack1lll111l1_opy_
        self.bstack1lll1l111_opy_ = bstack1lll1l111_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack111ll111_opy_ = []
        self.bstack1llll1ll1_opy_ = []
        self.bstack1lll1ll11_opy_ = []
        self.bstack1lll11ll1_opy_ = self.bstack1lll1111l_opy_()
        self.bstack1llllll11_opy_ = -1
    def bstack1lllll1ll_opy_(self, bstack1111l11l_opy_):
        self.parse_args()
        self.bstack111l1l11_opy_()
        self.bstack1lll11l1l_opy_(bstack1111l11l_opy_)
        self.bstack1llll1l11_opy_()
    def bstack1llll1lll_opy_(self):
        bstack1lll11l11_opy_ = bstack1lll1l11l_opy_.bstack11111ll1_opy_(self.bstack1lll111l1_opy_, self.logger)
        if bstack1lll11l11_opy_ is None:
            self.logger.warn(bstack11ll_opy_ (u"ࠥࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣ࡬ࡦࡴࡤ࡭ࡧࡵࠤ࡮ࡹࠠ࡯ࡱࡷࠤ࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࢀࡥࡥ࠰ࠣࡗࡰ࡯ࡰࡱ࡫ࡱ࡫ࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠳ࠨস"))
            return
        bstack1lllll111_opy_ = False
        bstack1lll11l11_opy_.bstack1lllll11l_opy_(bstack11ll_opy_ (u"ࠦࡪࡴࡡࡣ࡮ࡨࡨࠧহ"), bstack1lll11l11_opy_.bstack1111111l_opy_())
        start_time = time.time()
        if bstack1lll11l11_opy_.bstack1111111l_opy_():
            test_files = self.bstack1llll11l1_opy_()
            bstack1lllll111_opy_ = True
            bstack11111l11_opy_ = bstack1lll11l11_opy_.bstack1lll1ll1l_opy_(test_files)
            if bstack11111l11_opy_:
                self.bstack111ll111_opy_ = [os.path.normpath(item).replace(bstack11ll_opy_ (u"ࠬࡢ࡜ࠨ঺"), bstack11ll_opy_ (u"࠭࠯ࠨ঻")) for item in bstack11111l11_opy_]
                self.__1111ll1l_opy_()
                bstack1lll11l11_opy_.bstack111l11l1_opy_(bstack1lllll111_opy_)
                self.logger.info(bstack11ll_opy_ (u"ࠢࡕࡧࡶࡸࡸࠦࡲࡦࡱࡵࡨࡪࡸࡥࡥࠢࡸࡷ࡮ࡴࡧࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠻ࠢࡾࢁ়ࠧ").format(self.bstack111ll111_opy_))
            else:
                self.logger.info(bstack11ll_opy_ (u"ࠣࡐࡲࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡹࡨࡶࡪࠦࡲࡦࡱࡵࡨࡪࡸࡥࡥࠢࡥࡽࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠳ࠨঽ"))
        bstack1lll11l11_opy_.bstack1lllll11l_opy_(bstack11ll_opy_ (u"ࠤࡷ࡭ࡲ࡫ࡔࡢ࡭ࡨࡲ࡙ࡵࡁࡱࡲ࡯ࡽࠧা"), int((time.time() - start_time) * 1000)) # bstack111ll11l_opy_ to bstack1lll1llll_opy_
    def __1111ll1l_opy_(self):
        bstack11ll_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡇࡱࡵࠤࡪࡧࡣࡩࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࠥ࡯࡮ࠡࡵࡨࡰ࡫࠴ࡳࡱࡧࡦࡣ࡫࡯࡬ࡦࡵ࠯ࠤࡨࡵ࡬࡭ࡧࡦࡸࠥࡧ࡬࡭ࠢࡱࡳࡩ࡫ࡩࡥࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣি")
        bstack1llll11ll_opy_ = []
        try:
            from browserstack_sdk.bstack11ll11l1_opy_ import bstack11l1ll11_opy_
            results = bstack11l1ll11_opy_(bstack11l1lll1_opy_=self.bstack111ll111_opy_, bstack11ll11ll_opy_=True)
            if not results.get(bstack11ll_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬী"), False):
                self.logger.error(bstack11ll_opy_ (u"࡚ࠧࡥࡴࡶࠣࡧࡴࡲ࡬ࡦࡥࡷ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪ࠺ࠡࡽࢀࠦু").format(results.get(bstack11ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬূ"), bstack11ll_opy_ (u"ࠧࡖࡰ࡮ࡲࡴࡽ࡮ࠡࡧࡵࡶࡴࡸࠧৃ"))))
                return 0
            bstack1llll11ll_opy_ = results.get(bstack11ll_opy_ (u"ࠨࡰࡲࡨࡪ࡯ࡤࡴࠩৄ"), [])
            if bstack1llll11ll_opy_:
                os.environ[bstack11ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡑࡕࡇࡍࡋࡓࡕࡔࡄࡘࡊࡊ࡟ࡔࡇࡏࡉࡈ࡚ࡏࡓࡕࠪ৅")] = json.dumps(bstack1llll11ll_opy_)
                self.logger.info(bstack11ll_opy_ (u"ࠥࡇࡴࡲ࡬ࡦࡥࡷࡩࡩࠦࡻࡾࠢࡷࡩࡸࡺࠠ࡯ࡱࡧࡩ࡮ࡪࡳࠡࡨࡲࡶࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠧ৆").format(len(bstack1llll11ll_opy_)))
            else:
                self.logger.warn(bstack11ll_opy_ (u"ࠦࡓࡵࠠࡵࡧࡶࡸࡸࠦࡣࡰ࡮࡯ࡩࡨࡺࡥࡥࠢࡩࡶࡴࡳࠠࡴࡲࡨࡧࠥ࡬ࡩ࡭ࡧࡶ࠾ࠥࢁࡽࠣে").format(self.bstack111ll111_opy_))
        except Exception as e:
            self.logger.error(bstack11ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡰࡲࡨࡪࠦࡳࡦ࡮ࡨࡧࡹࡵࡲࡴ࠼ࠣࡿࢂࠨৈ").format(str(e)))
            import traceback
            self.logger.error(bstack11ll_opy_ (u"ࠨࡔࡳࡣࡦࡩࡧࡧࡣ࡬࠼ࠣࡿࢂࠨ৉").format(traceback.format_exc()))
            return 0
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack1lll111ll_opy_():
        import importlib
        if getattr(importlib, bstack11ll_opy_ (u"ࠧࡧ࡫ࡱࡨࡤࡲ࡯ࡢࡦࡨࡶࠬ৊"), False):
            bstack1llll1111_opy_ = importlib.find_loader(bstack11ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡵࡨࡰࡪࡴࡩࡶ࡯ࠪো"))
        else:
            bstack1llll1111_opy_ = importlib.util.find_spec(bstack11ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡶࡩࡱ࡫࡮ࡪࡷࡰࠫৌ"))
    def bstack11111l1l_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1llllll11_opy_ = -1
        if self.bstack1lll1l111_opy_ and bstack11ll_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯্ࠪ") in self.bstack1lll111l1_opy_:
            self.bstack1llllll11_opy_ = int(self.bstack1lll111l1_opy_[bstack11ll_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫৎ")])
        try:
            bstack1llll111l_opy_ = [bstack11ll_opy_ (u"ࠬ࠳࠭ࡥࡴ࡬ࡺࡪࡸࠧ৏"), bstack11ll_opy_ (u"࠭࠭࠮ࡲ࡯ࡹ࡬࡯࡮ࡴࠩ৐"), bstack11ll_opy_ (u"ࠧ࠮ࡲࠪ৑")]
            if self.bstack1llllll11_opy_ >= 0:
                bstack1llll111l_opy_.extend([bstack11ll_opy_ (u"ࠨ࠯࠰ࡲࡺࡳࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩ৒"), bstack11ll_opy_ (u"ࠩ࠰ࡲࠬ৓")])
            for arg in bstack1llll111l_opy_:
                self.bstack11111l1l_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack111l1l11_opy_(self):
        bstack1llll1ll1_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack1llll1ll1_opy_ = bstack1llll1ll1_opy_
        return self.bstack1llll1ll1_opy_
    def bstack1llllll1l_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack1lll111ll_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack1lll1l1ll_opy_)
    def bstack1lll11l1l_opy_(self, bstack1111l11l_opy_):
        bstack1111l111_opy_ = Config.bstack11111ll1_opy_()
        if bstack1111l11l_opy_:
            self.bstack1llll1ll1_opy_.append(bstack11ll_opy_ (u"ࠪ࠱࠲ࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ৔"))
            self.bstack1llll1ll1_opy_.append(bstack11ll_opy_ (u"࡙ࠫࡸࡵࡦࠩ৕"))
        if bstack1111l111_opy_.bstack111111ll_opy_():
            self.bstack1llll1ll1_opy_.append(bstack11ll_opy_ (u"ࠬ࠳࠭ࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫ৖"))
            self.bstack1llll1ll1_opy_.append(bstack11ll_opy_ (u"࠭ࡔࡳࡷࡨࠫৗ"))
        self.bstack1llll1ll1_opy_.append(bstack11ll_opy_ (u"ࠧ࠮ࡲࠪ৘"))
        self.bstack1llll1ll1_opy_.append(bstack11ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡰ࡭ࡷࡪ࡭ࡳ࠭৙"))
        self.bstack1llll1ll1_opy_.append(bstack11ll_opy_ (u"ࠩ࠰࠱ࡩࡸࡩࡷࡧࡵࠫ৚"))
        self.bstack1llll1ll1_opy_.append(bstack11ll_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪ৛"))
        if self.bstack1llllll11_opy_ > 1:
            self.bstack1llll1ll1_opy_.append(bstack11ll_opy_ (u"ࠫ࠲ࡴࠧড়"))
            self.bstack1llll1ll1_opy_.append(str(self.bstack1llllll11_opy_))
    def bstack1llll1l11_opy_(self):
        if bstack111ll1ll_opy_.bstack111l1l1l_opy_(self.bstack1lll111l1_opy_):
             self.bstack1llll1ll1_opy_ += [
                bstack111111l1_opy_.get(bstack11ll_opy_ (u"ࠬࡸࡥࡳࡷࡱࠫঢ়")), str(bstack111ll1ll_opy_.bstack1111l1ll_opy_(self.bstack1lll111l1_opy_)),
                bstack111111l1_opy_.get(bstack11ll_opy_ (u"࠭ࡤࡦ࡮ࡤࡽࠬ৞")), str(bstack111111l1_opy_.get(bstack11ll_opy_ (u"ࠧࡳࡧࡵࡹࡳ࠳ࡤࡦ࡮ࡤࡽࠬয়")))
            ]
    def bstack111l1111_opy_(self):
        bstack1lll1ll11_opy_ = []
        for spec in self.bstack111ll111_opy_:
            bstack1lllll1l1_opy_ = [spec]
            bstack1lllll1l1_opy_ += self.bstack1llll1ll1_opy_
            bstack1lll1ll11_opy_.append(bstack1lllll1l1_opy_)
        self.bstack1lll1ll11_opy_ = bstack1lll1ll11_opy_
        return bstack1lll1ll11_opy_
    def bstack1lll1111l_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack1lll11ll1_opy_ = True
            return True
        except Exception as e:
            self.bstack1lll11ll1_opy_ = False
        return self.bstack1lll11ll1_opy_
    def bstack1lll1lll1_opy_(self):
        bstack11ll_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡍࡥࡵࠢࡷ࡬ࡪࠦࡣࡰࡷࡱࡸࠥࡵࡦࠡࡶࡨࡷࡹࡹࠠࡸ࡫ࡷ࡬ࡴࡻࡴࠡࡴࡸࡲࡳ࡯࡮ࡨࠢࡷ࡬ࡪࡳࠠࡶࡵ࡬ࡲ࡬ࠦࡰࡺࡶࡨࡷࡹࠦࡣࡰ࡮࡯ࡩࡨࡺࡩࡰࡰ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡯࡮ࡵ࠼ࠣࡘ࡭࡫ࠠࡵࡱࡷࡥࡱࠦ࡮ࡶ࡯ࡥࡩࡷࠦ࡯ࡧࠢࡷࡩࡸࡺࡳࠡࡥࡲࡰࡱ࡫ࡣࡵࡧࡧ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤৠ")
        try:
            from browserstack_sdk.bstack11ll11l1_opy_ import bstack11l1ll11_opy_
            bstack1llll1l1l_opy_ = bstack11l1ll11_opy_(bstack11ll1l1l_opy_=self.bstack1llll1ll1_opy_, bstack11ll11ll_opy_=True)
            if not bstack1llll1l1l_opy_.get(bstack11ll_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪৡ"), False):
                self.logger.error(bstack11ll_opy_ (u"ࠥࡘࡪࡹࡴࠡࡥࡲࡹࡳࡺࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡱࡱࠤ࡫ࡧࡩ࡭ࡧࡧ࠾ࠥࢁࡽࠣৢ").format(bstack1llll1l1l_opy_.get(bstack11ll_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪৣ"), bstack11ll_opy_ (u"࡛ࠬ࡮࡬ࡰࡲࡻࡳࠦࡥࡳࡴࡲࡶࠬ৤"))))
                return 0
            count = bstack1llll1l1l_opy_.get(bstack11ll_opy_ (u"࠭ࡣࡰࡷࡱࡸࠬ৥"), 0)
            test_files = bstack1llll1l1l_opy_.get(bstack11ll_opy_ (u"ࠧࡵࡧࡶࡸࡤ࡬ࡩ࡭ࡧࡶࠫ০"), [])
            self.logger.info(bstack11ll_opy_ (u"ࠣࡅࡲࡰࡱ࡫ࡣࡵࡧࡧࠤࢀࢃࠠࡵࡧࡶࡸࡸࠦࡦࡳࡱࡰࠤࢀࢃࠠࡧ࡫࡯ࡩࡸࠨ১").format(count, len(test_files)))
            return count
        except Exception as e:
            self.logger.error(bstack11ll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡧࡴࡻ࡮ࡵ࠼ࠣࡿࢂࠨ২").format(e))
            import traceback
            self.logger.error(bstack11ll_opy_ (u"ࠥࡘࡷࡧࡣࡦࡤࡤࡧࡰࡀࠠࡼࡿࠥ৩").format(traceback.format_exc()))
            return 0
    def bstack111l1lll_opy_(self, bstack1111l1l1_opy_, bstack1lllll1ll_opy_):
        bstack1lllll1ll_opy_[bstack11ll_opy_ (u"ࠫࡈࡕࡎࡇࡋࡊࠫ৪")] = self.bstack1lll111l1_opy_
        multiprocessing.set_start_method(bstack11ll_opy_ (u"ࠬࡹࡰࡢࡹࡱࠫ৫"))
        bstack1111lll1_opy_ = []
        manager = multiprocessing.Manager()
        bstack1lllllll1_opy_ = manager.list()
        if bstack11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ৬") in self.bstack1lll111l1_opy_:
            for index, platform in enumerate(self.bstack1lll111l1_opy_[bstack11ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ৭")]):
                bstack1111lll1_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack1111l1l1_opy_,
                                                            args=(self.bstack1llll1ll1_opy_, bstack1lllll1ll_opy_, bstack1lllllll1_opy_)))
            bstack111l11ll_opy_ = len(self.bstack1lll111l1_opy_[bstack11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ৮")])
        else:
            bstack1111lll1_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack1111l1l1_opy_,
                                                        args=(self.bstack1llll1ll1_opy_, bstack1lllll1ll_opy_, bstack1lllllll1_opy_)))
            bstack111l11ll_opy_ = 1
        i = 0
        for t in bstack1111lll1_opy_:
            os.environ[bstack11ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩ৯")] = str(i)
            if bstack11ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ৰ") in self.bstack1lll111l1_opy_:
                os.environ[bstack11ll_opy_ (u"ࠫࡈ࡛ࡒࡓࡇࡑࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡅࡃࡗࡅࠬৱ")] = json.dumps(self.bstack1lll111l1_opy_[bstack11ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ৲")][i % bstack111l11ll_opy_])
            i += 1
            t.start()
        for t in bstack1111lll1_opy_:
            t.join()
        return list(bstack1lllllll1_opy_)
    @staticmethod
    def bstack11111111_opy_(driver, bstack1lll1l1l1_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack11ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪ৳"), None)
        if item and getattr(item, bstack11ll_opy_ (u"ࠧࡠࡣ࠴࠵ࡾࡥࡴࡦࡵࡷࡣࡨࡧࡳࡦࠩ৴"), None) and not getattr(item, bstack11ll_opy_ (u"ࠨࡡࡤ࠵࠶ࡿ࡟ࡴࡶࡲࡴࡤࡪ࡯࡯ࡧࠪ৵"), False):
            logger.info(
                bstack11ll_opy_ (u"ࠤࡄࡹࡹࡵ࡭ࡢࡶࡨࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡦࡺࡨࡧࡺࡺࡩࡰࡰࠣ࡬ࡦࡹࠠࡦࡰࡧࡩࡩ࠴ࠠࡑࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤ࡫ࡵࡲࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢ࡬ࡷࠥࡻ࡮ࡥࡧࡵࡻࡦࡿ࠮ࠣ৶"))
            bstack1llllllll_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack1111ll11_opy_.bstack111ll1l1_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)
    def bstack1llll11l1_opy_(self):
        bstack11ll_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳࠡࡶ࡫ࡩࠥࡲࡩࡴࡶࠣࡳ࡫ࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡸࡴࠦࡢࡦࠢࡨࡼࡪࡩࡵࡵࡧࡧ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤ৷")
        try:
            from browserstack_sdk.bstack11ll11l1_opy_ import bstack11l1ll11_opy_
            bstack111l1ll1_opy_ = bstack11l1ll11_opy_(bstack11ll1l1l_opy_=self.bstack1llll1ll1_opy_, bstack11ll11ll_opy_=True)
            if not bstack111l1ll1_opy_.get(bstack11ll_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬ৸"), False):
                self.logger.error(bstack11ll_opy_ (u"࡚ࠧࡥࡴࡶࠣࡪ࡮ࡲࡥࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨ࠿ࠦࡻࡾࠤ৹").format(bstack111l1ll1_opy_.get(bstack11ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ৺"), bstack11ll_opy_ (u"ࠧࡖࡰ࡮ࡲࡴࡽ࡮ࠡࡧࡵࡶࡴࡸࠧ৻"))))
                return []
            test_files = bstack111l1ll1_opy_.get(bstack11ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࠬৼ"), [])
            count = bstack111l1ll1_opy_.get(bstack11ll_opy_ (u"ࠩࡦࡳࡺࡴࡴࠨ৽"), 0)
            self.logger.debug(bstack11ll_opy_ (u"ࠥࡇࡴࡲ࡬ࡦࡥࡷࡩࡩࠦࡻࡾࠢࡷࡩࡸࡺࡳࠡ࡫ࡱࠤࢀࢃࠠࡧ࡫࡯ࡩࡸࠨ৾").format(count, len(test_files)))
            return test_files
        except Exception as e:
            self.logger.error(bstack11ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡧࡴࡲ࡬ࡦࡥࡷ࡭ࡴࡴ࠺ࠡࡽࢀࠦ৿").format(e))
            import traceback
            self.logger.error(bstack11ll_opy_ (u"࡚ࠧࡲࡢࡥࡨࡦࡦࡩ࡫࠻ࠢࡾࢁࠧ਀").format(traceback.format_exc()))
            return []