# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
import os
from uuid import uuid4
from bstack_utils.helper import bstack1lllll11_opy_, bstack111l111llll_opy_
from bstack_utils.bstack1l111lll1l_opy_ import bstack11l111l1l1l_opy_
class bstack1ll1l1ll_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack1111111lll1_opy_=None, bstack111111l111l_opy_=True, bstack1ll111lll11_opy_=None, bstack1l1l11l1ll_opy_=None, result=None, duration=None, bstack1l1llll1_opy_=None, meta={}):
        self.bstack1l1llll1_opy_ = bstack1l1llll1_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack111111l111l_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack1111111lll1_opy_ = bstack1111111lll1_opy_
        self.bstack1ll111lll11_opy_ = bstack1ll111lll11_opy_
        self.bstack1l1l11l1ll_opy_ = bstack1l1l11l1ll_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack1ll1llll_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11l11111_opy_(self, meta):
        self.meta = meta
    def bstack11l1l1ll_opy_(self, hooks):
        self.hooks = hooks
    def bstack111111l1111_opy_(self):
        bstack111111lll11_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack11l1l11_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬἄ"): bstack111111lll11_opy_,
            bstack11l1l11_opy_ (u"ࠪࡰࡴࡩࡡࡵ࡫ࡲࡲࠬἅ"): bstack111111lll11_opy_,
            bstack11l1l11_opy_ (u"ࠫࡻࡩ࡟ࡧ࡫࡯ࡩࡵࡧࡴࡩࠩἆ"): bstack111111lll11_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack11l1l11_opy_ (u"࡛ࠧ࡮ࡦࡺࡳࡩࡨࡺࡥࡥࠢࡤࡶ࡬ࡻ࡭ࡦࡰࡷ࠾ࠥࠨἇ") + key)
            setattr(self, key, val)
    def bstack111111ll111_opy_(self):
        return {
            bstack11l1l11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫἈ"): self.name,
            bstack11l1l11_opy_ (u"ࠧࡣࡱࡧࡽࠬἉ"): {
                bstack11l1l11_opy_ (u"ࠨ࡮ࡤࡲ࡬࠭Ἂ"): bstack11l1l11_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩἋ"),
                bstack11l1l11_opy_ (u"ࠪࡧࡴࡪࡥࠨἌ"): self.code
            },
            bstack11l1l11_opy_ (u"ࠫࡸࡩ࡯ࡱࡧࡶࠫἍ"): self.scope,
            bstack11l1l11_opy_ (u"ࠬࡺࡡࡨࡵࠪἎ"): self.tags,
            bstack11l1l11_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩἏ"): self.framework,
            bstack11l1l11_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫἐ"): self.started_at
        }
    def bstack111111ll1l1_opy_(self):
        return {
         bstack11l1l11_opy_ (u"ࠨ࡯ࡨࡸࡦ࠭ἑ"): self.meta
        }
    def bstack111111l1lll_opy_(self):
        return {
            bstack11l1l11_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡔࡨࡶࡺࡴࡐࡢࡴࡤࡱࠬἒ"): {
                bstack11l1l11_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࡡࡱࡥࡲ࡫ࠧἓ"): self.bstack1111111lll1_opy_
            }
        }
    def bstack111111l11l1_opy_(self, bstack1111111llll_opy_, details):
        step = next(filter(lambda st: st[bstack11l1l11_opy_ (u"ࠫ࡮ࡪࠧἔ")] == bstack1111111llll_opy_, self.meta[bstack11l1l11_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫἕ")]), None)
        step.update(details)
    def bstack11l11ll1_opy_(self, bstack1111111llll_opy_):
        step = next(filter(lambda st: st[bstack11l1l11_opy_ (u"࠭ࡩࡥࠩ἖")] == bstack1111111llll_opy_, self.meta[bstack11l1l11_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭἗")]), None)
        step.update({
            bstack11l1l11_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬἘ"): bstack1lllll11_opy_()
        })
    def bstack1l1lll11_opy_(self, bstack1111111llll_opy_, result, duration=None):
        bstack1ll111lll11_opy_ = bstack1lllll11_opy_()
        if bstack1111111llll_opy_ is not None and self.meta.get(bstack11l1l11_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨἙ")):
            step = next(filter(lambda st: st[bstack11l1l11_opy_ (u"ࠪ࡭ࡩ࠭Ἒ")] == bstack1111111llll_opy_, self.meta[bstack11l1l11_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪἛ")]), None)
            step.update({
                bstack11l1l11_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪἜ"): bstack1ll111lll11_opy_,
                bstack11l1l11_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠨἝ"): duration if duration else bstack111l111llll_opy_(step[bstack11l1l11_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ἞")], bstack1ll111lll11_opy_),
                bstack11l1l11_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ἟"): result.result,
                bstack11l1l11_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪἠ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack111111l1l1l_opy_):
        if self.meta.get(bstack11l1l11_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩἡ")):
            self.meta[bstack11l1l11_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪἢ")].append(bstack111111l1l1l_opy_)
        else:
            self.meta[bstack11l1l11_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫἣ")] = [ bstack111111l1l1l_opy_ ]
    def bstack111111lll1l_opy_(self):
        return {
            bstack11l1l11_opy_ (u"࠭ࡵࡶ࡫ࡧࠫἤ"): self.bstack1ll1llll_opy_(),
            **self.bstack111111ll111_opy_(),
            **self.bstack111111l1111_opy_(),
            **self.bstack111111ll1l1_opy_()
        }
    def bstack111111llll1_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack11l1l11_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬἥ"): self.bstack1ll111lll11_opy_,
            bstack11l1l11_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩἦ"): self.duration,
            bstack11l1l11_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩἧ"): self.result.result
        }
        if data[bstack11l1l11_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪἨ")] == bstack11l1l11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫἩ"):
            data[bstack11l1l11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫἪ")] = self.result.bstack1111111l1l_opy_()
            data[bstack11l1l11_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧἫ")] = [{bstack11l1l11_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪἬ"): self.result.bstack1111lll11ll_opy_()}]
        return data
    def bstack111111ll1ll_opy_(self):
        return {
            bstack11l1l11_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭Ἥ"): self.bstack1ll1llll_opy_(),
            **self.bstack111111ll111_opy_(),
            **self.bstack111111l1111_opy_(),
            **self.bstack111111llll1_opy_(),
            **self.bstack111111ll1l1_opy_()
        }
    def bstack1l11l1ll_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack11l1l11_opy_ (u"ࠩࡖࡸࡦࡸࡴࡦࡦࠪἮ") in event:
            return self.bstack111111lll1l_opy_()
        elif bstack11l1l11_opy_ (u"ࠪࡊ࡮ࡴࡩࡴࡪࡨࡨࠬἯ") in event:
            return self.bstack111111ll1ll_opy_()
    def event_key(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1ll111lll11_opy_ = time if time else bstack1lllll11_opy_()
        self.duration = duration if duration else bstack111l111llll_opy_(self.started_at, self.bstack1ll111lll11_opy_)
        if result:
            self.result = result
class bstack1l11ll1l_opy_(bstack1ll1l1ll_opy_):
    def __init__(self, hooks=[], bstack1l1l1l1l_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1l1l1l1l_opy_ = bstack1l1l1l1l_opy_
        super().__init__(*args, **kwargs, bstack1l1l11l1ll_opy_=bstack11l1l11_opy_ (u"ࠫࡹ࡫ࡳࡵࠩἰ"))
    @classmethod
    def bstack111111l11ll_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11l1l11_opy_ (u"ࠬ࡯ࡤࠨἱ"): id(step),
                bstack11l1l11_opy_ (u"࠭ࡴࡦࡺࡷࠫἲ"): step.name,
                bstack11l1l11_opy_ (u"ࠧ࡬ࡧࡼࡻࡴࡸࡤࠨἳ"): step.keyword,
            })
        return bstack1l11ll1l_opy_(
            **kwargs,
            meta={
                bstack11l1l11_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࠩἴ"): {
                    bstack11l1l11_opy_ (u"ࠩࡱࡥࡲ࡫ࠧἵ"): feature.name,
                    bstack11l1l11_opy_ (u"ࠪࡴࡦࡺࡨࠨἶ"): feature.filename,
                    bstack11l1l11_opy_ (u"ࠫࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩἷ"): feature.description
                },
                bstack11l1l11_opy_ (u"ࠬࡹࡣࡦࡰࡤࡶ࡮ࡵࠧἸ"): {
                    bstack11l1l11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫἹ"): scenario.name
                },
                bstack11l1l11_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭Ἲ"): steps,
                bstack11l1l11_opy_ (u"ࠨࡧࡻࡥࡲࡶ࡬ࡦࡵࠪἻ"): bstack11l111l1l1l_opy_(test)
            }
        )
    def bstack111111l1l11_opy_(self):
        return {
            bstack11l1l11_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨἼ"): self.hooks
        }
    def bstack111111ll11l_opy_(self):
        if self.bstack1l1l1l1l_opy_:
            return {
                bstack11l1l11_opy_ (u"ࠪ࡭ࡳࡺࡥࡨࡴࡤࡸ࡮ࡵ࡮ࡴࠩἽ"): self.bstack1l1l1l1l_opy_
            }
        return {}
    def bstack111111ll1ll_opy_(self):
        return {
            **super().bstack111111ll1ll_opy_(),
            **self.bstack111111l1l11_opy_()
        }
    def bstack111111lll1l_opy_(self):
        return {
            **super().bstack111111lll1l_opy_(),
            **self.bstack111111ll11l_opy_()
        }
    def event_key(self):
        return bstack11l1l11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭Ἶ")
class bstack1l111l11_opy_(bstack1ll1l1ll_opy_):
    def __init__(self, hook_type, *args,bstack1l1l1l1l_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1l1111l1l1l_opy_ = None
        self.bstack1l1l1l1l_opy_ = bstack1l1l1l1l_opy_
        super().__init__(*args, **kwargs, bstack1l1l11l1ll_opy_=bstack11l1l11_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪἿ"))
    def bstack11lllll1_opy_(self):
        return self.hook_type
    def bstack111111l1ll1_opy_(self):
        return {
            bstack11l1l11_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩὀ"): self.hook_type
        }
    def bstack111111ll1ll_opy_(self):
        return {
            **super().bstack111111ll1ll_opy_(),
            **self.bstack111111l1ll1_opy_()
        }
    def bstack111111lll1l_opy_(self):
        return {
            **super().bstack111111lll1l_opy_(),
            bstack11l1l11_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡ࡬ࡨࠬὁ"): self.bstack1l1111l1l1l_opy_,
            **self.bstack111111l1ll1_opy_()
        }
    def event_key(self):
        return bstack11l1l11_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࠪὂ")
    def bstack111lllll_opy_(self, bstack1l1111l1l1l_opy_):
        self.bstack1l1111l1l1l_opy_ = bstack1l1111l1l1l_opy_