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
import json
import time
import os
import threading
import asyncio
from browserstack_sdk.sdk_cli.bstack1llll1l1lll_opy_ import (
    bstack1llllll1111_opy_,
    bstack1lllll11l11_opy_,
    bstack1llll1ll111_opy_,
    bstack1llll111l1l_opy_,
)
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1ll1lll_opy_, bstack1ll1l1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllllll1l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1llllll_opy_, bstack1lll1l1lll1_opy_, bstack1lll1l1llll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1l111_opy_ import bstack1lll1ll11ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1111_opy_ import bstack1lll11l1lll_opy_
from typing import Tuple, List, Any
from bstack_utils.bstack1l1ll1lll1_opy_ import bstack1l11lll11_opy_, bstack11lllll11_opy_, bstack11111lll1l_opy_
from browserstack_sdk import sdk_pb2 as structs
class bstack1lll1l11ll1_opy_(bstack1lll11l1lll_opy_):
    bstack1lll1ll1ll1_opy_ = bstack1l111ll_opy_ (u"ࠣࡶࡨࡷࡹࡥࡤࡳ࡫ࡹࡩࡷࡹࠢᄟ")
    bstack1lll11llll1_opy_ = bstack1l111ll_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࡳࠣᄠ")
    bstack1lll1ll11l1_opy_ = bstack1l111ll_opy_ (u"ࠥࡲࡴࡴ࡟ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡷࡪࡹࡳࡪࡱࡱࡷࠧᄡ")
    bstack1lll1l111ll_opy_ = bstack1l111ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡶࡩࡸࡹࡩࡰࡰࡶࠦᄢ")
    bstack1lll11l1l1l_opy_ = bstack1l111ll_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡣࡷ࡫ࡦࡴࠤᄣ")
    bstack1llll111lll_opy_ = bstack1l111ll_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡨࡸࡥࡢࡶࡨࡨࠧᄤ")
    bstack1lll1lllll1_opy_ = bstack1l111ll_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡴࡡ࡮ࡧࠥᄥ")
    bstack1lll1llll11_opy_ = bstack1l111ll_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡳࡵࡣࡷࡹࡸࠨᄦ")
    def __init__(self):
        super().__init__(bstack1lll1l1l11l_opy_=self.bstack1lll1ll1ll1_opy_, frameworks=[bstack1lllllll1l1_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1lllll1l111_opy_((bstack1lll1llllll_opy_.BEFORE_EACH, bstack1lll1l1lll1_opy_.POST), self.bstack1lll11ll111_opy_)
        if bstack1ll1l1ll1_opy_():
            TestFramework.bstack1lllll1l111_opy_((bstack1lll1llllll_opy_.TEST, bstack1lll1l1lll1_opy_.POST), self.bstack1lll1lll11l_opy_)
        else:
            TestFramework.bstack1lllll1l111_opy_((bstack1lll1llllll_opy_.TEST, bstack1lll1l1lll1_opy_.PRE), self.bstack1lll1lll11l_opy_)
        TestFramework.bstack1lllll1l111_opy_((bstack1lll1llllll_opy_.TEST, bstack1lll1l1lll1_opy_.POST), self.bstack1lll1l1ll1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll11ll111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1lllll1l1l1_opy_: Tuple[bstack1lll1llllll_opy_, bstack1lll1l1lll1_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll11l1ll1_opy_ = self.bstack1lll1llll1l_opy_(instance.context)
        if not bstack1lll11l1ll1_opy_:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠤࡶࡩࡹࡥࡡࡤࡶ࡬ࡺࡪࡥࡰࡢࡩࡨ࠾ࠥࡴ࡯ࠡࡲࡤ࡫ࡪࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࠢᄧ") + str(bstack1lllll1l1l1_opy_) + bstack1l111ll_opy_ (u"ࠥࠦᄨ"))
            return
        f.bstack1lllll1ll1l_opy_(instance, bstack1lll1l11ll1_opy_.bstack1lll11llll1_opy_, bstack1lll11l1ll1_opy_)
    def bstack1lll1llll1l_opy_(self, context: bstack1llll111l1l_opy_, bstack1lll1l11l1l_opy_= True):
        if bstack1lll1l11l1l_opy_:
            bstack1lll11l1ll1_opy_ = self.bstack1lll11lll11_opy_(context, reverse=True)
        else:
            bstack1lll11l1ll1_opy_ = self.bstack1lll1lll1ll_opy_(context, reverse=True)
        return [f for f in bstack1lll11l1ll1_opy_ if f[1].state != bstack1llllll1111_opy_.QUIT]
    def bstack1lll1lll11l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1lllll1l1l1_opy_: Tuple[bstack1lll1llllll_opy_, bstack1lll1l1lll1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11ll111_opy_(f, instance, bstack1lllll1l1l1_opy_, *args, **kwargs)
        if not bstack1lll1ll1lll_opy_:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᄩ") + str(kwargs) + bstack1l111ll_opy_ (u"ࠧࠨᄪ"))
            return
        bstack1lll11l1ll1_opy_ = f.get_state(instance, bstack1lll1l11ll1_opy_.bstack1lll11llll1_opy_, [])
        if not bstack1lll11l1ll1_opy_:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᄫ") + str(kwargs) + bstack1l111ll_opy_ (u"ࠢࠣᄬ"))
            return
        if len(bstack1lll11l1ll1_opy_) > 1:
            self.logger.debug(
                bstack1lll11lllll_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡿࡱ࡫࡮ࠩࡲࡤ࡫ࡪࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࡽ࡮ࡻࡦࡸࡧࡴࡿࠥᄭ"))
        bstack1llll111111_opy_, bstack1llll11111l_opy_ = bstack1lll11l1ll1_opy_[0]
        page = bstack1llll111111_opy_()
        if not page:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡱࡣࡪࡩࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᄮ") + str(kwargs) + bstack1l111ll_opy_ (u"ࠥࠦᄯ"))
            return
        bstack11ll11l111_opy_ = getattr(args[0], bstack1l111ll_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦᄰ"), None)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1l111ll_opy_ (u"ࠧࡺࡥࡴࡶࡆࡳࡳࡺࡥࡹࡶࡒࡴࡹ࡯࡯࡯ࡵࠥᄱ")).get(bstack1l111ll_opy_ (u"ࠨࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣᄲ")):
            try:
                page.evaluate(bstack1l111ll_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣᄳ"),
                            bstack1l111ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠬᄴ") + json.dumps(
                                bstack11ll11l111_opy_) + bstack1l111ll_opy_ (u"ࠤࢀࢁࠧᄵ"))
            except Exception as e:
                self.logger.debug(bstack1l111ll_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥࢁࡽࠣᄶ"), e)
    def bstack1lll1l1ll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1lllll1l1l1_opy_: Tuple[bstack1lll1llllll_opy_, bstack1lll1l1lll1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11ll111_opy_(f, instance, bstack1lllll1l1l1_opy_, *args, **kwargs)
        if not bstack1lll1ll1lll_opy_:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᄷ") + str(kwargs) + bstack1l111ll_opy_ (u"ࠧࠨᄸ"))
            return
        bstack1lll11l1ll1_opy_ = f.get_state(instance, bstack1lll1l11ll1_opy_.bstack1lll11llll1_opy_, [])
        if not bstack1lll11l1ll1_opy_:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᄹ") + str(kwargs) + bstack1l111ll_opy_ (u"ࠢࠣᄺ"))
            return
        if len(bstack1lll11l1ll1_opy_) > 1:
            self.logger.debug(
                bstack1lll11lllll_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡿࡱ࡫࡮ࠩࡲࡤ࡫ࡪࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࡽ࡮ࡻࡦࡸࡧࡴࡿࠥᄻ"))
        bstack1llll111111_opy_, bstack1llll11111l_opy_ = bstack1lll11l1ll1_opy_[0]
        page = bstack1llll111111_opy_()
        if not page:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡱࡣࡪࡩࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᄼ") + str(kwargs) + bstack1l111ll_opy_ (u"ࠥࠦᄽ"))
            return
        status = f.get_state(instance, TestFramework.bstack1lll1l111l1_opy_, None)
        if not status:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠦࡳࡵࠠࡴࡶࡤࡸࡺࡹࠠࡧࡱࡵࠤࡹ࡫ࡳࡵ࠮ࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࠢᄾ") + str(bstack1lllll1l1l1_opy_) + bstack1l111ll_opy_ (u"ࠧࠨᄿ"))
            return
        bstack1lll1ll1l11_opy_ = {bstack1l111ll_opy_ (u"ࠨࡳࡵࡣࡷࡹࡸࠨᅀ"): status.lower()}
        bstack1lll1ll1l1l_opy_ = f.get_state(instance, TestFramework.bstack1llll111ll1_opy_, None)
        if status.lower() == bstack1l111ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᅁ") and bstack1lll1ll1l1l_opy_ is not None:
            bstack1lll1ll1l11_opy_[bstack1l111ll_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨᅂ")] = bstack1lll1ll1l1l_opy_[0][bstack1l111ll_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬᅃ")][0] if isinstance(bstack1lll1ll1l1l_opy_, list) else str(bstack1lll1ll1l1l_opy_)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1l111ll_opy_ (u"ࠥࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠣᅄ")).get(bstack1l111ll_opy_ (u"ࠦࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣᅅ")):
            try:
                page.evaluate(
                        bstack1l111ll_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨᅆ"),
                        bstack1l111ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࠫᅇ")
                        + json.dumps(bstack1lll1ll1l11_opy_)
                        + bstack1l111ll_opy_ (u"ࠢࡾࠤᅈ")
                    )
            except Exception as e:
                self.logger.debug(bstack1l111ll_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥࢁࡽࠣᅉ"), e)
    def bstack1lll1l1ll11_opy_(
        self,
        instance: bstack1lll1l1llll_opy_,
        f: TestFramework,
        bstack1lllll1l1l1_opy_: Tuple[bstack1lll1llllll_opy_, bstack1lll1l1lll1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11ll111_opy_(f, instance, bstack1lllll1l1l1_opy_, *args, **kwargs)
        if not bstack1lll1ll1lll_opy_:
            self.logger.debug(
                bstack1lll11lllll_opy_ (u"ࠤࡰࡥࡷࡱ࡟ࡰ࠳࠴ࡽࡤࡹࡹ࡯ࡥ࠽ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࡽ࡮ࡻࡦࡸࡧࡴࡿࠥᅊ"))
            return
        bstack1lll11l1ll1_opy_ = f.get_state(instance, bstack1lll1l11ll1_opy_.bstack1lll11llll1_opy_, [])
        if not bstack1lll11l1ll1_opy_:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᅋ") + str(kwargs) + bstack1l111ll_opy_ (u"ࠦࠧᅌ"))
            return
        if len(bstack1lll11l1ll1_opy_) > 1:
            self.logger.debug(
                bstack1lll11lllll_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠࡼ࡮ࡨࡲ࠭ࡶࡡࡨࡧࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࢁ࡫ࡸࡣࡵ࡫ࡸࢃࠢᅍ"))
        bstack1llll111111_opy_, bstack1llll11111l_opy_ = bstack1lll11l1ll1_opy_[0]
        page = bstack1llll111111_opy_()
        if not page:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠨ࡭ࡢࡴ࡮ࡣࡴ࠷࠱ࡺࡡࡶࡽࡳࡩ࠺ࠡࡰࡲࠤࡵࡧࡧࡦࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᅎ") + str(kwargs) + bstack1l111ll_opy_ (u"ࠢࠣᅏ"))
            return
        timestamp = int(time.time() * 1000)
        data = bstack1l111ll_opy_ (u"ࠣࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࡔࡻࡱࡧ࠿ࠨᅐ") + str(timestamp)
        try:
            page.evaluate(
                bstack1l111ll_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥᅑ"),
                bstack1l111ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨᅒ").format(
                    json.dumps(
                        {
                            bstack1l111ll_opy_ (u"ࠦࡦࡩࡴࡪࡱࡱࠦᅓ"): bstack1l111ll_opy_ (u"ࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢᅔ"),
                            bstack1l111ll_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤᅕ"): {
                                bstack1l111ll_opy_ (u"ࠢࡵࡻࡳࡩࠧᅖ"): bstack1l111ll_opy_ (u"ࠣࡃࡱࡲࡴࡺࡡࡵ࡫ࡲࡲࠧᅗ"),
                                bstack1l111ll_opy_ (u"ࠤࡧࡥࡹࡧࠢᅘ"): data,
                                bstack1l111ll_opy_ (u"ࠥࡰࡪࡼࡥ࡭ࠤᅙ"): bstack1l111ll_opy_ (u"ࠦࡩ࡫ࡢࡶࡩࠥᅚ")
                            }
                        }
                    )
                )
            )
        except Exception as e:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠧ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡱ࠴࠵ࡾࠦࡡ࡯ࡰࡲࡸࡦࡺࡩࡰࡰࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࢀࢃࠢᅛ"), e)
    def bstack1llll111l11_opy_(
        self,
        instance: bstack1lll1l1llll_opy_,
        f: TestFramework,
        bstack1lllll1l1l1_opy_: Tuple[bstack1lll1llllll_opy_, bstack1lll1l1lll1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11ll111_opy_(f, instance, bstack1lllll1l1l1_opy_, *args, **kwargs)
        if f.get_state(instance, bstack1lll1l11ll1_opy_.bstack1llll111lll_opy_, False):
            return
        self.bstack1lllll1111l_opy_()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llll1l1l11_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll11ll1l1_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1l11111_opy_)
        req.test_framework_state = bstack1lllll1l1l1_opy_[0].name
        req.test_hook_state = bstack1lllll1l1l1_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1llll1111ll_opy_)
        for bstack1lll1l1l1ll_opy_ in bstack1lll1ll11ll_opy_.bstack1lll1l1111l_opy_.values():
            session = req.automation_sessions.add()
            session.provider = (
                bstack1l111ll_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠧᅜ")
                if bstack1lll1ll1lll_opy_
                else bstack1l111ll_opy_ (u"ࠢࡶࡰ࡮ࡲࡴࡽ࡮ࡠࡩࡵ࡭ࡩࠨᅝ")
            )
            session.ref = bstack1lll1l1l1ll_opy_.ref()
            session.hub_url = bstack1lll1ll11ll_opy_.get_state(bstack1lll1l1l1ll_opy_, bstack1lll1ll11ll_opy_.bstack1lll1lll1l1_opy_, bstack1l111ll_opy_ (u"ࠣࠤᅞ"))
            session.framework_name = bstack1lll1l1l1ll_opy_.framework_name
            session.framework_version = bstack1lll1l1l1ll_opy_.framework_version
            session.framework_session_id = bstack1lll1ll11ll_opy_.get_state(bstack1lll1l1l1ll_opy_, bstack1lll1ll11ll_opy_.bstack1llll1111l1_opy_, bstack1l111ll_opy_ (u"ࠤࠥᅟ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1ll111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1lllll1l1l1_opy_: Tuple[bstack1lll1llllll_opy_, bstack1lll1l1lll1_opy_],
        *args,
        **kwargs
    ):
        bstack1lll11l1ll1_opy_ = f.get_state(instance, bstack1lll1l11ll1_opy_.bstack1lll11llll1_opy_, [])
        if not bstack1lll11l1ll1_opy_:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡩࡸࡩࡷࡧࡵ࠾ࠥࡴ࡯ࠡࡲࡤ࡫ࡪࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᅠ") + str(kwargs) + bstack1l111ll_opy_ (u"ࠦࠧᅡ"))
            return
        if len(bstack1lll11l1ll1_opy_) > 1:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡤࡳ࡫ࡹࡩࡷࡀࠠࡼ࡮ࡨࡲ࠭ࡶࡡࡨࡧࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᅢ") + str(kwargs) + bstack1l111ll_opy_ (u"ࠨࠢᅣ"))
        bstack1llll111111_opy_, bstack1llll11111l_opy_ = bstack1lll11l1ll1_opy_[0]
        page = bstack1llll111111_opy_()
        if not page:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠢࡨࡧࡷࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡱࡳࠥࡶࡡࡨࡧࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᅤ") + str(kwargs) + bstack1l111ll_opy_ (u"ࠣࠤᅥ"))
            return
        return page
    def bstack1lll1l11l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1lllll1l1l1_opy_: Tuple[bstack1lll1llllll_opy_, bstack1lll1l1lll1_opy_],
        *args,
        **kwargs
    ):
        caps = {}
        bstack1lll11ll1ll_opy_ = {}
        for bstack1lll1l1l1ll_opy_ in bstack1lll1ll11ll_opy_.bstack1lll1l1111l_opy_.values():
            caps = bstack1lll1ll11ll_opy_.get_state(bstack1lll1l1l1ll_opy_, bstack1lll1ll11ll_opy_.bstack1lll1lll111_opy_, bstack1l111ll_opy_ (u"ࠤࠥᅦ"))
        bstack1lll11ll1ll_opy_[bstack1l111ll_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠣᅧ")] = caps.get(bstack1l111ll_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࠧᅨ"), bstack1l111ll_opy_ (u"ࠧࠨᅩ"))
        bstack1lll11ll1ll_opy_[bstack1l111ll_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧᅪ")] = caps.get(bstack1l111ll_opy_ (u"ࠢࡰࡵࠥᅫ"), bstack1l111ll_opy_ (u"ࠣࠤᅬ"))
        bstack1lll11ll1ll_opy_[bstack1l111ll_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦᅭ")] = caps.get(bstack1l111ll_opy_ (u"ࠥࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠢᅮ"), bstack1l111ll_opy_ (u"ࠦࠧᅯ"))
        bstack1lll11ll1ll_opy_[bstack1l111ll_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳࠨᅰ")] = caps.get(bstack1l111ll_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣᅱ"), bstack1l111ll_opy_ (u"ࠢࠣᅲ"))
        return bstack1lll11ll1ll_opy_
    def bstack1lll1l11lll_opy_(self, page: object, bstack1lll11lll1l_opy_, args={}):
        try:
            bstack1lll1l1l1l1_opy_ = bstack1l111ll_opy_ (u"ࠣࠤࠥࠬ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࠨ࠯࠰࠱ࡦࡸࡺࡡࡤ࡭ࡖࡨࡰࡇࡲࡨࡵࠬࠤࢀࢁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡵࡩࡹࡻࡲ࡯ࠢࡱࡩࡼࠦࡐࡳࡱࡰ࡭ࡸ࡫ࠨࠩࡴࡨࡷࡴࡲࡶࡦ࠮ࠣࡶࡪࡰࡥࡤࡶࠬࠤࡂࡄࠠࡼࡽࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡥࡷࡹࡧࡣ࡬ࡕࡧ࡯ࡆࡸࡧࡴ࠰ࡳࡹࡸ࡮ࠨࡳࡧࡶࡳࡱࡼࡥࠪ࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡾࡪࡳࡥࡢࡰࡦࡼࢁࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾࡿࠬ࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࢂ࠯ࠨࡼࡣࡵ࡫ࡤࡰࡳࡰࡰࢀ࠭ࠧࠨࠢᅳ")
            bstack1lll11lll1l_opy_ = bstack1lll11lll1l_opy_.replace(bstack1l111ll_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧᅴ"), bstack1l111ll_opy_ (u"ࠥࡦࡸࡺࡡࡤ࡭ࡖࡨࡰࡇࡲࡨࡵࠥᅵ"))
            script = bstack1lll1l1l1l1_opy_.format(fn_body=bstack1lll11lll1l_opy_, arg_json=json.dumps(args))
            return page.evaluate(script)
        except Exception as e:
            self.logger.error(bstack1l111ll_opy_ (u"ࠦࡦ࠷࠱ࡺࡡࡶࡧࡷ࡯ࡰࡵࡡࡨࡼࡪࡩࡵࡵࡧ࠽ࠤࡊࡸࡲࡰࡴࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡥ࠶࠷ࡹࠡࡵࡦࡶ࡮ࡶࡴ࠭ࠢࠥᅶ") + str(e) + bstack1l111ll_opy_ (u"ࠧࠨᅷ"))