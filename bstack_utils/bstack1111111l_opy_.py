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
import os
from bstack_utils.constants import *
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.bstack11ll1llll1l_opy_ import bstack11lll111lll_opy_
from bstack_utils.bstack111l1lll_opy_ import bstack1llll111l_opy_
from bstack_utils.helper import bstack1ll1l1llll_opy_
import json
class bstack1lll1lll1_opy_:
    _1ll1ll1lll1_opy_ = None
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.bstack1111l11l111_opy_ = bstack11lll111lll_opy_(self.config, logger)
        self.bstack111l1lll_opy_ = bstack1llll111l_opy_.bstack1llllllll_opy_(config=self.config)
        self.bstack1111l111l1l_opy_ = {}
        self.bstack1111l1l1_opy_ = False
        self.bstack1111l11l11l_opy_ = (
            self.__1111l11l1ll_opy_()
            and self.bstack111l1lll_opy_ is not None
            and self.bstack111l1lll_opy_.bstack1lllll1ll_opy_()
            and config.get(bstack1ll1ll1_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬẋ"), None) is not None
            and config.get(bstack1ll1ll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫẌ"), os.path.basename(os.getcwd())) is not None
        )
    @classmethod
    def bstack1llllllll_opy_(cls, config, logger):
        if cls._1ll1ll1lll1_opy_ is None and config is not None:
            cls._1ll1ll1lll1_opy_ = bstack1lll1lll1_opy_(config, logger)
        return cls._1ll1ll1lll1_opy_
    def bstack1lllll1ll_opy_(self):
        bstack1ll1ll1_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡄࡰࠢࡱࡳࡹࠦࡡࡱࡲ࡯ࡽࠥࡺࡥࡴࡶࠣࡳࡷࡪࡥࡳ࡫ࡱ࡫ࠥࡽࡨࡦࡰ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡒ࠵࠶ࡿࠠࡪࡵࠣࡲࡴࡺࠠࡦࡰࡤࡦࡱ࡫ࡤࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡏࡳࡦࡨࡶ࡮ࡴࡧࠡ࡫ࡶࠤࡳࡵࡴࠡࡧࡱࡥࡧࡲࡥࡥࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠥ࡯ࡳࠡࡐࡲࡲࡪࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠠࡪࡵࠣࡒࡴࡴࡥࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧẍ")
        return self.bstack1111l11l11l_opy_ and self.bstack1111l11l1l1_opy_()
    def bstack1111l11l1l1_opy_(self):
        bstack1111l11ll11_opy_ = os.getenv(bstack1ll1ll1_opy_ (u"ࠪࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࡥࡕࡔࡇࡇࠫẎ"), self.config.get(bstack1ll1ll1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧẏ"), None))
        return bstack1111l11ll11_opy_ in bstack11l1l11lll1_opy_
    def __1111l11l1ll_opy_(self):
        bstack11ll1l11ll1_opy_ = False
        for fw in bstack11l1l1l11l1_opy_:
            if fw in self.config.get(bstack1ll1ll1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨẐ"), bstack1ll1ll1_opy_ (u"࠭ࠧẑ")):
                bstack11ll1l11ll1_opy_ = True
        return bstack1ll1l1llll_opy_(self.config.get(bstack1ll1ll1_opy_ (u"ࠧࡵࡧࡶࡸࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫẒ"), bstack11ll1l11ll1_opy_))
    def bstack1111l111lll_opy_(self):
        return (not self.bstack1lllll1ll_opy_() and
                self.bstack111l1lll_opy_ is not None and self.bstack111l1lll_opy_.bstack1lllll1ll_opy_())
    def bstack1111l11ll1l_opy_(self):
        if not self.bstack1111l111lll_opy_():
            return
        if self.config.get(bstack1ll1ll1_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ẓ"), None) is None or self.config.get(bstack1ll1ll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬẔ"), os.path.basename(os.getcwd())) is None:
            self.logger.info(bstack1ll1ll1_opy_ (u"ࠥࡘࡪࡹࡴࠡࡔࡨࡳࡷࡪࡥࡳ࡫ࡱ࡫ࠥࡩࡡ࡯ࠩࡷࠤࡼࡵࡲ࡬ࠢࡤࡷࠥࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠡࡱࡵࠤࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠢ࡬ࡷࠥࡴࡵ࡭࡮࠱ࠤࡕࡲࡥࡢࡵࡨࠤࡸ࡫ࡴࠡࡣࠣࡲࡴࡴ࠭࡯ࡷ࡯ࡰࠥࡼࡡ࡭ࡷࡨ࠲ࠧẕ"))
        if not self.__1111l11l1ll_opy_():
            self.logger.info(bstack1ll1ll1_opy_ (u"࡙ࠦ࡫ࡳࡵࠢࡕࡩࡴࡸࡤࡦࡴ࡬ࡲ࡬ࠦࡣࡢࡰࠪࡸࠥࡽ࡯ࡳ࡭ࠣࡥࡸࠦࡴࡦࡵࡷࡖࡪࡶ࡯ࡳࡶ࡬ࡲ࡬ࠦࡩࡴࠢࡧ࡭ࡸࡧࡢ࡭ࡧࡧ࠲ࠥࡖ࡬ࡦࡣࡶࡩࠥ࡫࡮ࡢࡤ࡯ࡩࠥ࡯ࡴࠡࡨࡵࡳࡲࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠢࡩ࡭ࡱ࡫࠮ࠣẖ"))
    def bstack1111l111l11_opy_(self):
        return self.bstack1111l1l1_opy_
    def bstack11l11lll_opy_(self, bstack1111l111ll1_opy_):
        self.bstack1111l1l1_opy_ = bstack1111l111ll1_opy_
        self.bstack111ll111_opy_(bstack1ll1ll1_opy_ (u"ࠧࡧࡰࡱ࡮࡬ࡩࡩࠨẗ"), bstack1111l111ll1_opy_)
    def bstack111l1ll1_opy_(self, test_files):
        try:
            if test_files is None:
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨ࡛ࡳࡧࡲࡶࡩ࡫ࡲࡠࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࡢࠦࡎࡰࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦࡰࡳࡱࡹ࡭ࡩ࡫ࡤࠡࡨࡲࡶࠥࡵࡲࡥࡧࡵ࡭ࡳ࡭࠮ࠣẘ"))
                return None
            orchestration_strategy = None
            orchestration_metadata = self.bstack111l1lll_opy_.bstack111lll1l1l1_opy_()
            if self.bstack111l1lll_opy_ is not None:
                orchestration_strategy = self.bstack111l1lll_opy_.bstack1lll11ll11_opy_()
            if orchestration_strategy is None:
                self.logger.error(bstack1ll1ll1_opy_ (u"ࠢࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡴࡶࡵࡥࡹ࡫ࡧࡺࠢ࡬ࡷࠥࡔ࡯࡯ࡧ࠱ࠤࡈࡧ࡮࡯ࡱࡷࠤࡵࡸ࡯ࡤࡧࡨࡨࠥࡽࡩࡵࡪࠣࡸࡪࡹࡴࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡵࡨࡷࡸ࡯࡯࡯࠰ࠥẙ"))
                return None
            self.logger.info(bstack1ll1ll1_opy_ (u"ࠣࡔࡨࡳࡷࡪࡥࡳ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴࠢࡺ࡭ࡹ࡮ࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡴࡶࡵࡥࡹ࡫ࡧࡺ࠼ࠣࡿࢂࠨẚ").format(orchestration_strategy))
            if cli.is_running():
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠤࡘࡷ࡮ࡴࡧࠡࡅࡏࡍࠥ࡬࡬ࡰࡹࠣࡪࡴࡸࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱ࠲ࠧẛ"))
                ordered_test_files = cli.test_orchestration_session(test_files, orchestration_strategy, json.dumps(orchestration_metadata))
            else:
                self.logger.debug(bstack1ll1ll1_opy_ (u"࡙ࠥࡸ࡯࡮ࡨࠢࡶࡨࡰࠦࡦ࡭ࡱࡺࠤ࡫ࡵࡲࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠳ࠨẜ"))
                self.bstack1111l11l111_opy_.bstack11lll11111l_opy_(test_files, orchestration_strategy, orchestration_metadata)
                ordered_test_files = self.bstack1111l11l111_opy_.bstack11ll1lll1l1_opy_()
            if not ordered_test_files:
                return None
            self.bstack111ll111_opy_(bstack1ll1ll1_opy_ (u"ࠦࡺࡶ࡬ࡰࡣࡧࡩࡩ࡚ࡥࡴࡶࡉ࡭ࡱ࡫ࡳࡄࡱࡸࡲࡹࠨẝ"), len(test_files))
            self.bstack111ll111_opy_(bstack1ll1ll1_opy_ (u"ࠧࡴ࡯ࡥࡧࡌࡲࡩ࡫ࡸࠣẞ"), int(os.environ.get(bstack1ll1ll1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡔࡏࡅࡇࡢࡍࡓࡊࡅ࡙ࠤẟ")) or bstack1ll1ll1_opy_ (u"ࠢ࠱ࠤẠ")))
            self.bstack111ll111_opy_(bstack1ll1ll1_opy_ (u"ࠣࡶࡲࡸࡦࡲࡎࡰࡦࡨࡷࠧạ"), int(os.environ.get(bstack1ll1ll1_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡐࡒࡈࡊࡥࡃࡐࡗࡑࡘࠧẢ")) or bstack1ll1ll1_opy_ (u"ࠥ࠵ࠧả")))
            self.bstack111ll111_opy_(bstack1ll1ll1_opy_ (u"ࠦࡩࡵࡷ࡯࡮ࡲࡥࡩ࡫ࡤࡕࡧࡶࡸࡋ࡯࡬ࡦࡵࡆࡳࡺࡴࡴࠣẤ"), len(ordered_test_files))
            self.bstack111ll111_opy_(bstack1ll1ll1_opy_ (u"ࠧࡹࡰ࡭࡫ࡷࡘࡪࡹࡴࡴࡃࡓࡍࡈࡧ࡬࡭ࡅࡲࡹࡳࡺࠢấ"), self.bstack1111l11l111_opy_.bstack11ll1lll11l_opy_())
            return ordered_test_files
        except Exception as e:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨ࡛ࡳࡧࡲࡶࡩ࡫ࡲࡠࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࡢࠦࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡱࡵࡨࡪࡸࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡥ࡯ࡥࡸࡹࡥࡴ࠼ࠣࡿࢂࠨẦ").format(e))
        return None
    def bstack111ll111_opy_(self, key, value):
        self.bstack1111l111l1l_opy_[key] = value
    def bstack1ll11l11l_opy_(self):
        return self.bstack1111l111l1l_opy_