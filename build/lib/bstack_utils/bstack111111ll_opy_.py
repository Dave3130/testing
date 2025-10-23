# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
import os
from bstack_utils.constants import *
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.bstack11ll1lll11l_opy_ import bstack11ll1ll11ll_opy_
from bstack_utils.bstack1lll1l1l1_opy_ import bstack11111lll_opy_
from bstack_utils.helper import bstack11lllll1l1_opy_
import json
class bstack111l11ll_opy_:
    _1ll1l1lll11_opy_ = None
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.bstack11111lllll1_opy_ = bstack11ll1ll11ll_opy_(self.config, logger)
        self.bstack1lll1l1l1_opy_ = bstack11111lll_opy_.bstack111ll1l1_opy_(config=self.config)
        self.bstack11111llllll_opy_ = {}
        self.bstack1111l111_opy_ = False
        self.bstack11111lll1l1_opy_ = (
            self.__11111lll11l_opy_()
            and self.bstack1lll1l1l1_opy_ is not None
            and self.bstack1lll1l1l1_opy_.bstack1111l11l_opy_()
            and config.get(bstack11lll1_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪấ"), None) is not None
            and config.get(bstack11lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩẦ"), os.path.basename(os.getcwd())) is not None
        )
    @classmethod
    def bstack111ll1l1_opy_(cls, config, logger):
        if cls._1ll1l1lll11_opy_ is None and config is not None:
            cls._1ll1l1lll11_opy_ = bstack111l11ll_opy_(config, logger)
        return cls._1ll1l1lll11_opy_
    def bstack1111l11l_opy_(self):
        bstack11lll1_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡉࡵࠠ࡯ࡱࡷࠤࡦࡶࡰ࡭ࡻࠣࡸࡪࡹࡴࠡࡱࡵࡨࡪࡸࡩ࡯ࡩࠣࡻ࡭࡫࡮࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡐ࠳࠴ࡽࠥ࡯ࡳࠡࡰࡲࡸࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡔࡸࡤࡦࡴ࡬ࡲ࡬ࠦࡩࡴࠢࡱࡳࡹࠦࡥ࡯ࡣࡥࡰࡪࡪࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠣ࡭ࡸࠦࡎࡰࡰࡨࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠥ࡯ࡳࠡࡐࡲࡲࡪࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥầ")
        return self.bstack11111lll1l1_opy_ and self.bstack1111l11111l_opy_()
    def bstack1111l11111l_opy_(self):
        bstack11111llll1l_opy_ = os.getenv(bstack11lll1_opy_ (u"ࠨࡈࡕࡅࡒࡋࡗࡐࡔࡎࡣ࡚࡙ࡅࡅࠩẨ"), self.config.get(bstack11lll1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬẩ"), None))
        return bstack11111llll1l_opy_ in bstack11l11l1l1ll_opy_
    def __11111lll11l_opy_(self):
        bstack11ll11lll11_opy_ = False
        for fw in bstack11l11lll1ll_opy_:
            if fw in self.config.get(bstack11lll1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭Ẫ"), bstack11lll1_opy_ (u"ࠫࠬẫ")):
                bstack11ll11lll11_opy_ = True
        return bstack11lllll1l1_opy_(self.config.get(bstack11lll1_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩẬ"), bstack11ll11lll11_opy_))
    def bstack1111l111111_opy_(self):
        return (not self.bstack1111l11l_opy_() and
                self.bstack1lll1l1l1_opy_ is not None and self.bstack1lll1l1l1_opy_.bstack1111l11l_opy_())
    def bstack11111lll1ll_opy_(self):
        if not self.bstack1111l111111_opy_():
            return
        if self.config.get(bstack11lll1_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫậ"), None) is None or self.config.get(bstack11lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪẮ"), os.path.basename(os.getcwd())) is None:
            self.logger.info(bstack11lll1_opy_ (u"ࠣࡖࡨࡷࡹࠦࡒࡦࡱࡵࡨࡪࡸࡩ࡯ࡩࠣࡧࡦࡴࠧࡵࠢࡺࡳࡷࡱࠠࡢࡵࠣࡦࡺ࡯࡬ࡥࡐࡤࡱࡪࠦ࡯ࡳࠢࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠠࡪࡵࠣࡲࡺࡲ࡬࠯ࠢࡓࡰࡪࡧࡳࡦࠢࡶࡩࡹࠦࡡࠡࡰࡲࡲ࠲ࡴࡵ࡭࡮ࠣࡺࡦࡲࡵࡦ࠰ࠥắ"))
        if not self.__11111lll11l_opy_():
            self.logger.info(bstack11lll1_opy_ (u"ࠤࡗࡩࡸࡺࠠࡓࡧࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡨࡧ࡮ࠨࡶࠣࡻࡴࡸ࡫ࠡࡣࡶࠤࡹ࡫ࡳࡵࡔࡨࡴࡴࡸࡴࡪࡰࡪࠤ࡮ࡹࠠࡥ࡫ࡶࡥࡧࡲࡥࡥ࠰ࠣࡔࡱ࡫ࡡࡴࡧࠣࡩࡳࡧࡢ࡭ࡧࠣ࡭ࡹࠦࡦࡳࡱࡰࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡲࡲࠠࡧ࡫࡯ࡩ࠳ࠨẰ"))
    def bstack11111lll111_opy_(self):
        return self.bstack1111l111_opy_
    def bstack1111l1l1_opy_(self, bstack11111llll11_opy_):
        self.bstack1111l111_opy_ = bstack11111llll11_opy_
        self.bstack1111ll11_opy_(bstack11lll1_opy_ (u"ࠥࡥࡵࡶ࡬ࡪࡧࡧࠦằ"), bstack11111llll11_opy_)
    def bstack1llllllll_opy_(self, test_files):
        try:
            if test_files is None:
                self.logger.debug(bstack11lll1_opy_ (u"ࠦࡠࡸࡥࡰࡴࡧࡩࡷࡥࡴࡦࡵࡷࡣ࡫࡯࡬ࡦࡵࡠࠤࡓࡵࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩࠦࡦࡰࡴࠣࡳࡷࡪࡥࡳ࡫ࡱ࡫࠳ࠨẲ"))
                return None
            orchestration_strategy = None
            orchestration_metadata = self.bstack1lll1l1l1_opy_.bstack111llll1ll1_opy_()
            if self.bstack1lll1l1l1_opy_ is not None:
                orchestration_strategy = self.bstack1lll1l1l1_opy_.bstack11l1llll1l_opy_()
            if orchestration_strategy is None:
                self.logger.error(bstack11lll1_opy_ (u"ࠧࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡹࡴࡳࡣࡷࡩ࡬ࡿࠠࡪࡵࠣࡒࡴࡴࡥ࠯ࠢࡆࡥࡳࡴ࡯ࡵࠢࡳࡶࡴࡩࡥࡦࡦࠣࡻ࡮ࡺࡨࠡࡶࡨࡷࡹࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴ࠮ࠣẳ"))
                return None
            self.logger.info(bstack11lll1_opy_ (u"ࠨࡒࡦࡱࡵࡨࡪࡸࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹࠠࡸ࡫ࡷ࡬ࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡹࡴࡳࡣࡷࡩ࡬ࡿ࠺ࠡࡽࢀࠦẴ").format(orchestration_strategy))
            if cli.is_running():
                self.logger.debug(bstack11lll1_opy_ (u"ࠢࡖࡵ࡬ࡲ࡬ࠦࡃࡍࡋࠣࡪࡱࡵࡷࠡࡨࡲࡶࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥẵ"))
                ordered_test_files = cli.test_orchestration_session(test_files, orchestration_strategy, json.dumps(orchestration_metadata))
            else:
                self.logger.debug(bstack11lll1_opy_ (u"ࠣࡗࡶ࡭ࡳ࡭ࠠࡴࡦ࡮ࠤ࡫ࡲ࡯ࡸࠢࡩࡳࡷࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦẶ"))
                self.bstack11111lllll1_opy_.bstack11ll1llll11_opy_(test_files, orchestration_strategy, orchestration_metadata)
                ordered_test_files = self.bstack11111lllll1_opy_.bstack11lll1111l1_opy_()
            if not ordered_test_files:
                return None
            self.bstack1111ll11_opy_(bstack11lll1_opy_ (u"ࠤࡸࡴࡱࡵࡡࡥࡧࡧࡘࡪࡹࡴࡇ࡫࡯ࡩࡸࡉ࡯ࡶࡰࡷࠦặ"), len(test_files))
            self.bstack1111ll11_opy_(bstack11lll1_opy_ (u"ࠥࡲࡴࡪࡥࡊࡰࡧࡩࡽࠨẸ"), int(os.environ.get(bstack11lll1_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡒࡔࡊࡅࡠࡋࡑࡈࡊ࡞ࠢẹ")) or bstack11lll1_opy_ (u"ࠧ࠶ࠢẺ")))
            self.bstack1111ll11_opy_(bstack11lll1_opy_ (u"ࠨࡴࡰࡶࡤࡰࡓࡵࡤࡦࡵࠥẻ"), int(os.environ.get(bstack11lll1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡎࡐࡆࡈࡣࡈࡕࡕࡏࡖࠥẼ")) or bstack11lll1_opy_ (u"ࠣ࠳ࠥẽ")))
            self.bstack1111ll11_opy_(bstack11lll1_opy_ (u"ࠤࡧࡳࡼࡴ࡬ࡰࡣࡧࡩࡩ࡚ࡥࡴࡶࡉ࡭ࡱ࡫ࡳࡄࡱࡸࡲࡹࠨẾ"), len(ordered_test_files))
            self.bstack1111ll11_opy_(bstack11lll1_opy_ (u"ࠥࡷࡵࡲࡩࡵࡖࡨࡷࡹࡹࡁࡑࡋࡆࡥࡱࡲࡃࡰࡷࡱࡸࠧế"), self.bstack11111lllll1_opy_.bstack11ll1l1l11l_opy_())
            return ordered_test_files
        except Exception as e:
            self.logger.debug(bstack11lll1_opy_ (u"ࠦࡠࡸࡥࡰࡴࡧࡩࡷࡥࡴࡦࡵࡷࡣ࡫࡯࡬ࡦࡵࡠࠤࡊࡸࡲࡰࡴࠣ࡭ࡳࠦ࡯ࡳࡦࡨࡶ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡣ࡭ࡣࡶࡷࡪࡹ࠺ࠡࡽࢀࠦỀ").format(e))
        return None
    def bstack1111ll11_opy_(self, key, value):
        self.bstack11111llllll_opy_[key] = value
    def bstack1l111lllll_opy_(self):
        return self.bstack11111llllll_opy_